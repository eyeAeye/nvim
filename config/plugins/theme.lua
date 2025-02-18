-- vim.cmd("colorscheme cyberdream")
require("cyberdream").load()

-- require('onedark').setup {
--     style = 'darker'
-- }
-- require('onedark').load()

-- make sure cursorline and selection to have different colors
vim.api.nvim_set_hl(0, "Visual", { bg = "#3c3836", fg = "NONE" })
vim.api.nvim_set_hl(0, "CursorLine", { bg = "#44475a" })
