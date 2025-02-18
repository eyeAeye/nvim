local M = {}

--- Safely requires a module and handles errors.
-- @param module_name (string) The module name to require.
-- @return any The required module or nil if it fails.
function M.safe_require(module_name)
	local success, result = pcall(require, module_name)

	if not success then
		-- Delay the notification to avoid UI issues on startup
		vim.schedule(function()
			local message = string.format("⚠️ [utils.safe_require] Failed to load: %s\n%s", module_name, result)
			vim.notify(message, vim.log.levels.WARN)

			-- Attempt to sync plugins if module is missing
			-- if vim.fn.exists(":PaqSync") == 2 then
			-- 	vim.cmd("PaqSync")
			-- end
		end)

		return nil -- Ensure nil is returned if the module fails
	end

	return result
end

--- Safely sets up an LSP server and handles errors.
-- @param server (string) The LSP server name.
-- @param config (table|nil) The LSP configuration.
-- @return boolean, string If successful, returns `true`; otherwise, returns `false` and an error message.
function M.safe_lspconfig_setup(server, config)
	local lspconfig = M.safe_require("lspconfig")

	-- If lspconfig failed to load, return false immediately
	if not lspconfig then
		return false, string.format("⚠️ [LSP] Failed to load lspconfig for '%s'", server)
	end

	local success, err = pcall(function()
		lspconfig[server].setup(config or {})
	end)

	if not success then
		vim.schedule(function() -- Prevent UI issues on startup
			local message = string.format("⚠️ [LSP] Failed to start '%s': %s", server, err)
			vim.notify(message, vim.log.levels.WARN)
		end)
	end

	return success, err
end

return M
