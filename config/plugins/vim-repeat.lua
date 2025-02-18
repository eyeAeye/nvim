vim.keymap.set("n", "<Plug>MyWonderfulMap", function()
	local count = vim.v.count -- Get the count value
	if count == 0 then
		count = 1
	end -- Ensure at least 1
	require("repeat").set("<Plug>MyWonderfulMap", count)
end, { silent = true })
