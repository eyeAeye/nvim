import os
import subprocess
import sys
import shutil


def clear_screen():
    """Clear the terminal screen to ensure the menu appears at the top."""
    if os.name == "nt":
        subprocess.run(["pwsh", "-NoProfile", "-Command", "Clear-Host"])
    else:
        print("\033c", end="")  # ANSI escape sequence for Unix-like systems


def check_powershell():
    """Ensure the script is running in PowerShell or PowerShell 7 on Windows."""
    if sys.platform.startswith("win"):
        print("\n🔎 Checking PowerShell7 environment...")
        print("=" * 40)
        print(
            "⚠️ Please ensure you are running this script in PowerShell7(pwsh)."
        )

        choice = (
            input("👉 Do you need to open PowerShell7 now? (y/N): ")
            .strip()
            .lower()
        )
        if choice == "y":
            print("\n🖥️ Launching PowerShell7...\n")
            subprocess.run(["pwsh", "-NoProfile", "-NoExit"])
            sys.exit(0)
        else:
            print("✅ Continuing execution...\n")


def check_python():
    """Ensure Python and pip are installed."""
    print("\n🔎 Checking Python environment...")
    print("=" * 40)
    try:
        subprocess.run(["python", "--version"])
        print("")
        subprocess.run(["pip", "--version"])
        print("")
        print("✅ Python and pip are installed.\n")
    except subprocess.CalledProcessError:
        print("❌ Python or pip is missing.")
        choice = (
            input("👉 Do you want to install Python and pip? (y/N): ")
            .strip()
            .lower()
        )
        if choice == "y":
            if sys.platform.startswith("win"):
                print("\n📥 Installing Python via Winget...\n")
                subprocess.run(["winget", "install", "Python.Python.3"])
                print("")
            elif sys.platform.startswith("darwin"):
                print("\n📥 Installing Python via Homebrew...\n")
                subprocess.run(["brew", "install", "python"])
                print("")
            else:
                print("⚠️ Please install Python and pip manually.")
                sys.exit(1)
        else:
            print("❌ Python is required. Exiting.\n")
            sys.exit(1)


def install_nerd_font():
    """Prompt user for Nerd Font installation."""
    print("\n🎨 Enhancing Terminal Experience with Nerd Fonts!")
    print("=" * 40)
    print("🔤 Nerd Fonts provide better icon support for your terminal.\n")

    choice = (
        input("👉 Do you want a guide for a Nerd Font? (y/N): ").strip().lower()
    )
    if choice == "y":
        clear_screen()
        print(
            "\n🌐 Download a Nerd Font from: https://www.nerdfonts.com/font-downloads"
        )
        print(
            "💡 After installation, update your terminal settings to use the new font.\n"
        )

        input("🔹 Press Enter to continue...")
    else:
        print("✅ Skipping Nerd Font installation.\n")


def install_package_managers():
    """Ensure required package managers are installed."""
    print("\n📦 Checking for Package Managers...")
    print("=" * 40)

    if sys.platform.startswith("win"):
        # Check for Scoop
        if shutil.which("scoop") is None:
            print("❌ Scoop package manager is not installed.")
            choice = (
                input("👉 Do you want to install Scoop? (y/N): ")
                .strip()
                .lower()
            )
            if choice == "y":
                print("\n📥 Installing Scoop...")
                print(
                    f"💻> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"
                )
                subprocess.run(
                    [
                        "pwsh",
                        "-NoProfile",
                        "-Command",
                        "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser",
                    ]
                )
                print("")
                print(
                    f"💻> Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression"
                )
                subprocess.run(
                    [
                        "pwsh",
                        "-NoProfile",
                        "-Command",
                        "Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression",
                    ]
                )
                print("")
                print("✅ Scoop installed successfully!")
            else:
                print(
                    "⚠️ Package installation will require manual intervention."
                )
                input("🔹 Press Enter to continue...")
                return

        print(f"💻> scoop update")
        subprocess.run(["pwsh", "-NoProfile", "-Command", "scoop update"])
        print("")
        print(f"💻> scoop update main")
        subprocess.run(["pwsh", "-NoProfile", "-Command", "scoop update main"])
        print("")
        print(f"💻> scoop bucket add extras")
        subprocess.run(
            ["pwsh", "-NoProfile", "-Command", "scoop bucket add extras"]
        )
        print("")
        print(f"💻> scoop update extra")
        subprocess.run(["pwsh", "-NoProfile", "-Command", "scoop update extra"])
        print("")
        print("✅ Scoop updated successfully!")

    elif sys.platform.startswith("darwin"):
        # Check for Homebrew
        if shutil.which("brew") is None:
            print("❌ Homebrew is not installed.")
            choice = (
                input("👉 Do you want to install Homebrew? (y/N): ")
                .strip()
                .lower()
            )
            if choice == "y":
                print("\n📥 Installing Homebrew...")
                print(
                    f"💻> /bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'"
                )
                subprocess.run(
                    [
                        "/bin/bash",
                        "-c",
                        "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)",
                    ]
                )
                print("")
                print("✅ Homebrew installed successfully!")
            else:
                print(
                    "⚠️ Package installation will require manual intervention."
                )
                input("🔹 Press Enter to continue...")
                return

        print(f"💻> brew upgrade'")
        subprocess.run(["brew upgrade"])
        print("")
        print("✅ brew upgraded successfully!")
    else:
        print(
            "⚠️ This menu is for Windows/Mac users.\nPlease check your package manager installed (apt, yum, pacman, etc.)."
        )

    print("✅ Package manager check!\n")
    input("🔹 Press Enter to continue...")


def install_prerequisites():
    """Ensure required dependencies are installed. Assumes package manager is already set up."""
    print("\n🔧 Checking for Prerequisite Packages...")
    print("=" * 40)

    missing_packages = [
        "neovim",
        "gcc",
        "make",
        "git",
        "lazygit",
        "ripgrep",
        "lua-language-server",
    ]

    if sys.platform.startswith("win"):
        for package in missing_packages:
            print(f"📦 Installing {package} via Scoop...")
            print(f"💻> scoop install {package}")
            subprocess.run(
                ["pwsh", "-NoProfile", "-Command", f"scoop install {package}"]
            )
            print("")

    elif sys.platform.startswith("darwin"):
        for package in missing_packages:
            print(f"📦 Installing {package} via Homebrew...")
            print(f"💻> brew install {package}")
            subprocess.run(["brew", "install", package])
            print("")

    else:
        print("⚠️ Please install the following packages manually:")
        print(f"   {', '.join(missing_packages)}")

    print("\n✅ Installing Pyright for Python LSP...")
    print(f"💻> pip install pyright")
    subprocess.run(["pip", "install", "pyright"])
    print("")

    print("\n✅ All prerequisites installation excuted!\n")
    input("🔹 Press Enter to continue...")


def install_neovim_plugins():
    """Call the setup_plugin function"""
    from setup_plugin import setup_plugin

    setup_plugin()


def main():
    clear_screen()
    check_powershell()
    clear_screen()
    check_python()
    input("🔹 Press Enter to continue...")

    while True:
        clear_screen()
        print("\n" + "=" * 40)
        print("🚀 Neovim Auto-Setup | Main Menu ")
        print("=" * 40)
        print("📌 Select an option:\n")
        print("  [1] 🖋️ Install Nerd Font (Enhance terminal icons)")
        print(
            "  [2] ⚙️ Install Package Managers (Scoop/Homebrew for Windows/Mac users)"
        )
        print("  [3] 🔧 Install Prerequisites (Compilers, tools, etc.)")
        print("  [4] 🔌 Install Neovim Plugins (Auto-setup plugins)")
        print("  [x] ❌ Exit\n")
        print("-" * 40)

        choice = input("👉 Enter your choice (1-4, x): ").strip()

        if choice == "1":
            clear_screen()
            print("\n✨ About Nerd Font...\n")
            install_nerd_font()
        elif choice == "2":
            clear_screen()
            print("\n📦 Installing package managers...\n")
            install_package_managers()
        elif choice == "3":
            clear_screen()
            print("\n🔧 Installing prerequisites...\n")
            install_prerequisites()
        elif choice == "4":
            clear_screen()
            print("\n📦 Setting up Neovim plugins...\n")
            install_neovim_plugins()
            print("")
            input("🔹 Press Enter to continue...")
        elif choice.lower() == "x":
            print("\n👋 Exiting. Happy coding with Neovim! 🚀\n")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()
