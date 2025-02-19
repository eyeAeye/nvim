-- Create an augroup to avoid duplicate autocmds
vim.api.nvim_create_augroup("RestorePosition", { clear = true })
-- Return to last edit position when opening files
vim.api.nvim_create_autocmd("BufReadPost", {
	group = "RestorePosition",
	pattern = "*",
	callback = function()
		local mark = vim.api.nvim_buf_get_mark(0, '"')
		local lcount = vim.api.nvim_buf_line_count(0)
		if mark[1] > 0 and mark[1] <= lcount then
			vim.api.nvim_win_set_cursor(0, mark)
			vim.cmd("normal! zv")
		end
	end,
})

-- Turn on cursorline in normal mode
vim.api.nvim_create_augroup("ToggleCursorline", { clear = true })
-- Disable cursorline in Insert mode
vim.api.nvim_create_autocmd("InsertEnter", {
	group = "ToggleCursorline",
	pattern = "*",
	callback = function()
		vim.opt_local.cursorline = false
	end,
})

-- Enable cursorline when entering Normal mode or upon startup
vim.api.nvim_create_autocmd({ "InsertLeave", "VimEnter" }, {
	group = "ToggleCursorline",
	pattern = "*",
	callback = function()
		vim.opt_local.cursorline = true
	end,
})

-- clear autocmds
-- vim.api.nvim_clear_autocmds({ group = "RestorePosition" })
-- vim.api.nvim_clear_autocmds({ group = "ToggleCursorline" })
