local lib_path = "config.plugins" .. "." -- current library
local utils = require("config.utils")

--LUALINE
utils.safe_require(lib_path .. "nvim-web-devicon")
utils.safe_require(lib_path .. "lualine")

--LAZYGIT
utils.safe_require(lib_path .. "lazygit")

--THEME
utils.safe_require(lib_path .. "theme")

-- NOICE
utils.safe_require(lib_path .. "noice")

--TREESITTER
utils.safe_require(lib_path .. "treesitter")
utils.safe_require(lib_path .. "treesitter-context")

--LSP related
utils.safe_require(lib_path .. "cmp")
utils.safe_require("nvim-autopairs").setup({})
utils.safe_require(lib_path .. "lspconfig")
utils.safe_require(lib_path .. "trouble")

-- TELESCOPE
utils.safe_require(lib_path .. "telescope")

-- NVIM-TREE
utils.safe_require(lib_path .. "nvim-tree")

-- BARBAR
utils.safe_require(lib_path .. "barbar")

-- VIM-REPEAT
utils.safe_require(lib_path .. "vim-repeat")
