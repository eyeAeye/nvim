require("nvim-treesitter.configs").setup({
	ensure_installed = {
		"python",
		"vimdoc",
		"vim",
		"lua",
		"javascript",
		"html",
		"css",
		"cpp",
		"bash",
		"json",
		"markdown",
		"query",
		"regex",
	}, -- Install parsers
	highlight = { enable = true },
	indent = { enable = true },
	incremental_selection = {
		enable = true,
		keymaps = {
			init_selection = "gnn", -- set to `false` to disable
			node_incremental = "grn",
			scope_incremental = "grc",
			node_decremental = "grm",
		},
	},

	-- Text Objects (Better Motions)
	textobjects = {
		select = {
			enable = true,
			lookahead = true,
			keymaps = {
				["aa"] = "@parameter.outer",
				["ia"] = "@parameter.inner",
				["af"] = "@function.outer",
				["if"] = "@function.inner",
				["ac"] = "@class.outer",
				["ic"] = "@class.inner",
			},
		},
		move = {
			enable = true,
			set_jumps = true,
			goto_next_start = {
				["]m"] = "@function.outer",
				["]M"] = "@class.outer",
				-- ["]]"] = "@conditional.outer" or "@loop.outer" or "@block.outer" or "@function.outer" or "@class.outer" -- Any outer
			},
			-- goto_next_end = {
			-- ["]["] = "@conditional.outer" or "@loop.outer" or "@block.outer" or "@function.outer" or "@class.outer" -- Any outer end
			-- },
			goto_previous_start = {
				["[m"] = "@function.outer",
				["[M"] = "@class.outer",
				-- ["[["] = "@conditional.outer" or "@loop.outer" or "@block.outer" or "@function.outer" or "@class.outer" -- Any outer
			},
			-- goto_previous_end = {
			-- ["[]"] = "@conditional.outer" or "@loop.outer" or "@block.outer" or "@function.outer" or "@class.outer" -- Any outer end
			-- },
		},
		swap = {
			enable = true,
			swap_next = {
				["<leader>sp"] = "@parameter.inner",
			},
			swap_previous = {
				["<leader>sP"] = "@parameter.inner",
			},
		},
	},

	-- Refactoring
	refactor = {
		highlight_definitions = { enable = true, clear_on_cursor_move = true },
		-- highlight_current_scope = { enable = true },
		smart_rename = {
			enable = true,
			keymaps = { smart_rename = "grr" },
		},
		navigation = {
			enable = true,
			keymaps = {
				goto_definition = "gnd",
				-- 		list_definitions = "gnD",
				-- 		list_definitions_toc = "gO",
				-- goto_next_usage = "*",
				-- goto_previous_usage = "#",
			},
		},
	},
})

-- ADDITIONAL KEY MAPPINGS
local ts_utils = require("nvim-treesitter.ts_utils")

-- Helper function to find the first non-blank character column
local function first_non_blank_col(line)
	local col = vim.fn.match(vim.fn.getline(line), "\\S")
	return col == -1 and 0 or col
end

-- Helper function to check if a line is blank
local function is_blank_line(line)
	return vim.fn.getline(line):match("^%s*$") ~= nil
end

-- Jump to the next lower context (skipping blank lines)
local function jump_to_last_context()
	local node = ts_utils.get_node_at_cursor()
	if not node then
		return
	end

	local current_indent = vim.fn.indent(vim.fn.line("."))
	local last_line = vim.fn.line("$")

	for line = vim.fn.line(".") + 1, last_line do
		local next_indent = vim.fn.indent(line)
		if next_indent < current_indent and not is_blank_line(line) then
			vim.api.nvim_win_set_cursor(0, { line, first_non_blank_col(line) })
			return
		end
	end
	-- If no lower context is found, jump to the next block with the same indentation
	for line = vim.fn.line(".") + 1, last_line do
		local next_indent = vim.fn.indent(line)
		if next_indent == current_indent and not is_blank_line(line) then
			vim.api.nvim_win_set_cursor(0, { line, first_non_blank_col(line) })
			return
		end
	end
end

-- Jump to the previous higher context
local function jump_to_prev_context()
	local node = ts_utils.get_node_at_cursor()
	if not node then
		return
	end

	local current_indent = vim.fn.indent(vim.fn.line("."))

	for line = vim.fn.line(".") - 1, 1, -1 do
		local prev_indent = vim.fn.indent(line)
		if prev_indent < current_indent and not is_blank_line(line) then
			vim.api.nvim_win_set_cursor(0, { line, first_non_blank_col(line) })
			return
		end
	end
	-- If no higher context is found, jump to the previous block with the same indentation
	for line = vim.fn.line(".") - 1, 1, -1 do
		local prev_indent = vim.fn.indent(line)
		if prev_indent == current_indent and not is_blank_line(line) then
			vim.api.nvim_win_set_cursor(0, { line, first_non_blank_col(line) })
			return
		end
	end
end

vim.keymap.set("n", "<leader>j", jump_to_last_context, { desc = "Jump to last context" })
vim.keymap.set("n", "<leader>k", jump_to_prev_context, { desc = "Jump to previous context" })
