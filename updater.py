#            ╔═════════════════════════HaZaRd═════════════════════════════╗
#            ║        Youtube: https://www.youtube.com/@IIIHaZaRd         ║
#            ║        Github: https://github.com/Pytholearn               ║
#            ║        Discord: https://discord.gg/YU7jYRkxwp              ║
#            ╚════════════════════════════════════════════════════════════╝

# This is a Python script for an automatic updating system using a library named autoupgrader

import urllib.request
import os
import shutil
import time
import sys

# Default URL for fetching the latest version information
url = ""

# Current version of the program
current = ""

# Default download link for the updated program
download_link = ""

# Function to set a new URL for fetching version information
def set_url(url_):
    global url
    url = url_

# Function to retrieve the latest version information from the specified URL
def get_latest_version():
    file = urllib.request.urlopen(url)
    lines = ""
    for line in file:
        lines += line.decode("utf-8")
    return lines

# Function to set the current version of the program
def set_current_version(current_):
    global current
    current = current_

# Function to set a new download link for the updated program
def set_download_link(link):
    global download_link
    download_link = link

# Function to check if the current program version is up to date
def is_up_to_date():
    return current + "\n" == get_latest_version()

# Function to download and save the updated program to a specified path
def download(path_to_file):
    urllib.request.urlretrieve(download_link, path_to_file)

# Function to perform full auto-update process
def update():
    import git

    cwd = os.getcwd()
    print(f"Working directory: {cwd}")

    temp_dir = os.path.join(cwd, "temp_repo")

    print("Cloning new version...")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    git.Repo.clone_from(download_link, temp_dir)

    print("Replacing old files...")

    for root, dirs, files in os.walk(temp_dir):
        relative_path = os.path.relpath(root, temp_dir)
        for file in files:
            source_file = os.path.join(root, file)
            dest_file = os.path.join(cwd, relative_path, file)

            # Create destination directory if not exists
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)

            # Try to remove old file if exists
            try:
                if os.path.exists(dest_file):
                    os.remove(dest_file)
                shutil.move(source_file, dest_file)
            except Exception as e:
                print(f"Failed to replace {dest_file} - {e}")

    shutil.rmtree(temp_dir)
    print("Update complete! Please restart the program.")

    # Optional: Restart the program automatically
    time.sleep(2)
    print("Restarting...")
    python = sys.executable
    os.execl(python, python, *sys.argv)
