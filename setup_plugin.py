import os
import subprocess
from pathlib import Path
import sys
import shutil


def get_nvim_config_path():
    """Retrieve Neovim's stdpath('config') directly from Neovim."""
    try:
        result = subprocess.run(
            ["nvim", "--headless", "+echo stdpath('config')", "+qall"],
            capture_output=True,
            text=True,
            check=True,
        )
        output = (
            result.stdout.strip()
            if result.stdout.strip()
            else result.stderr.strip()
        )
        if Path(output).exists():
            raise Exception(
                f"stdpath('config'):{output} exists.\nRename it to {output}.backup"
            )
        return Path(output)
    except Exception as e:
        print(f"❌ config path from Neovim exists: {e}")
        return None


def get_nvim_data_path():
    """Retrieve Neovim's stdpath('config') directly from Neovim."""
    try:
        result = subprocess.run(
            ["nvim", "--headless", "+echo stdpath('data')", "+qall"],
            capture_output=True,
            text=True,
            check=True,
        )
        output = (
            result.stdout.strip()
            if result.stdout.strip()
            else result.stderr.strip()
        )
        if not Path(output).exists():
            raise Exception(f"stdpath('data'):{output} does not exist.")
        return Path(output)
    except Exception as e:
        print(f"❌ cannot find data path from Neovim: {e}")
        return None


def create_symlink(src_input, dst_input):
    """Create a symbolic link only if it doesn't exist."""
    src = Path(src_input)
    link_name = Path(dst_input)
    # Check if the link or file already exists
    if link_name.exists():
        raise RuntimeError(f"⚠️ Skipping: {link_name} already exists.")
        return

    try:
        os.symlink(src, link_name, src.is_dir())
        print(f"✅ Created symlink: {link_name} → {src}")
    except Exception as e:
        raise RuntimeError(f"❌ Failed to create symlink: {e}")


config_str = 'require(lib_path .. "plugins")'


def comment_config():
    # Define the relative path to the Lua file
    lua_file_path = os.path.join(
        os.path.dirname(__file__), "config", "init.lua"
    )

    # Read the Lua file
    with open(lua_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Modify the specific line containing config_str
    for i in range(len(lines)):
        if config_str in lines[i]:
            lines[i] = "-- " + lines[i]  # Comment out the line
            break  # Stop after finding and modifying the first occurrence
    else:
        print(f"Line containing `{config_str}` not found. No changes made.")
        return None
    # Write back the modified content
    with open(lua_file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"✅ Line containing `{config_str}` has been commented.")
    return 1


def uncomment_config():
    # Define the relative path to the Lua file
    lua_file_path = os.path.join(
        os.path.dirname(__file__), "config", "init.lua"
    )

    # Read the Lua file
    with open(lua_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find the index of the line containing config_str
    start_index = None
    for i, line in enumerate(lines):
        if config_str in line:
            start_index = i
            break

    # If found, keep only this line and everything after it
    if start_index is not None:
        lines[start_index] = config_str

        # Write back the modified content
        with open(lua_file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

        print(
            f"✅ plugin config enabled: Everything before `{config_str}` has been erased."
        )
        return 1
    else:
        print(f"❌ No `{config_str}` line found. No changes made.")
        return None


def install_paq(paq_path):
    """Create a symbolic link only if it doesn't exist."""
    paq_path.parent.mkdir(parents=True, exist_ok=True)

    # Check if the link or file already exists
    if paq_path.exists():
        print(f"⚠️ Skipping: {paq_path} already exists.")
        return

    try:
        subprocess.run(
            [
                "git",
                "clone",
                "--depth=1",
                "https://github.com/savq/paq-nvim.git",
                str(paq_path),
            ],
            check=True,
        )
        print(f"✅ Paq Cloned into: {paq_path}")
    except Exception as e:
        print(f"❌ Failed to install paq.nvim: {e}")

    try:
        result = subprocess.run(
            [
                "nvim",
                "--headless",
                "+PaqInstall",
                "-c",
                "autocmd User PaqDoneInstall qall",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        output = (
            result.stdout.strip()
            if result.stdout.strip()
            else result.stderr.strip()
        )
        print(f"✅ :PaqInstall success!")
    except Exception as e:
        print(f"❌ Failed to run :PaqInstall: {e}")


def make_jsregexp(target_directory):
    # Function to find sh.exe path dynamically
    sh_path = None
    if sys.platform.startswith("win"):
        # Try finding sh using where.exe (Windows native)
        sh_path = shutil.which("sh")
        if sh_path:
            pass
        else:
            # Fallback: Try using sh inside MSYS2 if installed
            possible_paths = [
                r"C:\Program Files\Git\bin\sh.exe",
                r"C:\msys64\usr\bin\sh.exe",
                r"C:\cygwin64\bin\sh.exe",
                r"C:\cygwin\bin\sh.exe",
            ]
            for path in possible_paths:
                if os.path.exists(path):
                    sh_path = path

        # Get the dynamically detected sh.exe path
        if not sh_path:
            print(
                "❌ Error: Unable to find sh.exe. Please install MSYS2, Git Bash, or Cygwin."
            )
            return None

        print(f"Using SHELL: {sh_path}")

        # Define the make command with the dynamically found sh.exe
        command = [
            "make",
            "install_jsregexp",
            "CC=gcc.exe",
            f"SHELL={sh_path}",  # Dynamically set SHELL
            ".SHELLFLAGS=-c",
        ]
    else:
        command = ["make", "install_jsregexp"]

    # Run the command
    try:
        result = subprocess.run(
            command,
            cwd=target_directory,
            shell=True,
            check=True,
            capture_output=True,
            text=True,
        )
        print("✅ Command Output:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("❌ Error Occurred:\n", e.stderr)
        return None
    return True


def setup_plugin():
    nvim_config_path = get_nvim_config_path()

    if not nvim_config_path:
        print(
            f"❌ Failed to get nvim config path from neovim!: {nvim_config_path}"
        )
        return
    if nvim_config_path.exists():
        print(
            f"❌ nvim config already exists!: {nvim_config_path}\nRename it to {nvim_config_path}.backup"
        )
        return

    nvim_data_path = get_nvim_data_path()
    if not nvim_data_path:
        print(f"❌ Failed to get nvim data path from neovim!: {nvim_data_path}")
        return

    if (nvim_data_path / "site").exists():
        print(
            f"❌ nvim data already exists!: {nvim_data_path}\nRename it to {nvim_data_path}.backup"
        )
        return

    # Define paths
    source_init = Path.cwd() / "nvim.init.lua"  # Current directory file
    link_init = nvim_config_path / "init.lua"  # Neovim config path

    source_config = Path.cwd() / "config"  # Current directory config folder
    link_config = nvim_config_path / "lua" / "config"  # Neovim config path

    # Ensure Neovim config directories exist
    nvim_config_path.mkdir(parents=True, exist_ok=True)
    (nvim_config_path / "lua").mkdir(parents=True, exist_ok=True)

    # Create symlinks only if they don’t already exist
    create_symlink(source_config, link_config)
    create_symlink(source_init, link_init)

    # Install paq package manager
    paq_path = nvim_data_path / "site" / "pack" / "paqs" / "start" / "paq-nvim"

    print(f"✅ Disabling plugin configuration temporarily")
    comment_config()
    try:
        install_paq(paq_path)
    except:
        return

    print(f"✅ Enabling plugin configuration")
    uncomment_config()

    print(f"✅ Building jsregexp")
    if make_jsregexp(
        nvim_data_path / "site" / "pack" / "paqs" / "start" / "LuaSnip"
    ):
        print(f"✅ Built jsregexp!")
    else:
        print(f"⚠️ Failed to build jsregexp")

    print(f"✅👌 READY TO GO!")

    print(f"💡 Don't forget to check \n\t:checkhealth in nvim!")
    input("🔹 Press Enter to continue...")


def main():
    setup_plugin()


if __name__ == "__main__":
    main()
