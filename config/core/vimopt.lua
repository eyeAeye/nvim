-- Set the color column at 80 characters
vim.opt.colorcolumn = "80"
-- Set text width to 80 characters
vim.opt.textwidth = 80
-- Set format options
vim.opt.formatoptions = "q"

-- Line number display
vim.opt.number = true
vim.opt.relativenumber = true
-- Display cursorline
vim.opt.cursorline = true

-- Always show the status line
vim.opt.laststatus = 2
-- Disable default mode indicator (use statusline instead)
vim.opt.showmode = false

-- Enable mouse support in all modes
vim.opt.mouse = "a"

-- Allow hidden buffers without saving
vim.opt.hidden = true

-- Enable system clipboard support
vim.opt.clipboard:append({ "unnamed", "unnamedplus" })

-- Reduce time before triggering CursorHold events (faster UI updates)
vim.opt.updatetime = 250

-- Always show the sign column
vim.opt.signcolumn = "yes"

-- Tab & Indentation configuration
vim.opt.tabstop = 4 -- Display width of a tab character (in spaces)
vim.opt.shiftwidth = 4 -- Indentation width for >> and <<
vim.opt.softtabstop = 4 -- How many spaces a tab counts for in insert mode
-- vim.opt.expandtab = true  -- Convert tabs to spaces
vim.opt.smarttab = true -- Insert appropriate number of spaces when using <Tab>
vim.opt.autoindent = true -- Copy indentation from the previous line
vim.opt.smartindent = true -- Auto-indent new lines in code
vim.opt.list = true
vim.opt.listchars = { tab = "▸ " } -- , trail = "·", space = "·" }
