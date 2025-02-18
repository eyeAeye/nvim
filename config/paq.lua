require("paq")({
	"savq/paq-nvim", -- Let Paq manage itself

	-- PLUGINS.LUALINE
	"nvim-tree/nvim-web-devicons",
	"nvim-lualine/lualine.nvim",

	-- PLUGINS.LAZYGIT
	"nvim-lua/plenary.nvim",
	"kdheepak/lazygit.nvim",

	-- PLUGINS.TELESCOPE
	{ "nvim-telescope/telescope.nvim", tag = "0.1.8" },
	{ "nvim-telescope/telescope-fzf-native.nvim", build = "make" },
	"nvim-telescope/telescope-ui-select.nvim",

	-- PLUGINS.CMP
	"rafamadriz/friendly-snippets",
	{ "L3MON4D3/LuaSnip", tag = "v2.*", build = "make install_jsregexp" },
	"hrsh7th/nvim-cmp",
	"hrsh7th/cmp-buffer",
	"hrsh7th/cmp-path",
	"hrsh7th/cmp-cmdline",
	"saadparwaiz1/cmp_luasnip",
	"windwp/nvim-autopairs",

	-- PLUGINS.TREESITTER
	{ "nvim-treesitter/nvim-treesitter", build = ":TSUpdate" },
	"nvim-treesitter/nvim-treesitter-textobjects",
	"nvim-treesitter/nvim-treesitter-refactor",
	"HiPhish/rainbow-delimiters.nvim",

	-- PLUGINS.TREESITTER-CONTEXT
	"nvim-treesitter/nvim-treesitter-context",

	-- PLUGINS.LSPCONFIG
	"neovim/nvim-lspconfig",
	"hrsh7th/cmp-nvim-lsp",

	-- PLUGINS.NVIM-TREE
	"nvim-tree/nvim-tree.lua",

	-- PLUGINS.BARBAR
	"romgrk/barbar.nvim",

	-- PLUGINS.NOICE
	"MunifTanjim/nui.nvim",
	"rcarriga/nvim-notify",
	"folke/noice.nvim",

	-- PLUGINS.TROUBLE
	"folke/trouble.nvim",

	-- PLUGINS.THEME
	"scottmckendry/cyberdream.nvim",

	-- VIM-REPEAT
	"tpope/vim-surround",
	"tpope/vim-repeat",
})
