-- local lib_path = "config.lsp" .. "." -- current library
local utils = require("config.utils")

-- Setup LSPs safely
local capabilities = require("cmp_nvim_lsp").default_capabilities()
-- the following part goes to config/lsp
-- require('lspconfig')['<YOUR_LSP_SERVER>'].setup {
--  capabilities = capabilities
-- }
utils.safe_lspconfig_setup("pyright", { capabilities = capabilities })
utils.safe_lspconfig_setup(
	"lua_ls",
	{ settings = { Lua = { diagnostics = { globals = { "vim" } } } }, capabilities = capabilities }
)
