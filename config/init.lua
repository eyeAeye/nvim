local lib_path = "config" .. "." -- current library

-- Enable experimental lazy loader
vim.loader.enable()

-- VIM options
require(lib_path .. "core")

-- Package Manager
require(lib_path .. "paq")

-- Package Configurations
require(lib_path .. "plugins")
