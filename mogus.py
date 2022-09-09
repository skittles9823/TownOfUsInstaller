# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.

import zipfile
from os import remove
from pathlib import Path
from shutil import copytree, rmtree

from requests import get

# find the download URL and filename of the latest ToU release
release = get(
    'https://api.github.com/repos/eDonnes124/Town-Of-Us-R/releases/latest'
)
release = release.json()
release_tag = release['name']

for i in release['assets']:
    if i['name'].endswith("zip"):
        filename = Path(i['name'])
        ziplink = i['browser_download_url']

# Download latest version of ToU and name the zip after it's github release zip
if not Path(filename).is_file():
    print(f"Downloading {filename}, please wait.")
    mogus = get(ziplink)
    filename.write_bytes(mogus.content)

# Extract the zip
mogus_zip = zipfile.ZipFile(filename)
mogus_zip.extractall(Path("ToU"))
mogus_zip.close()

# Clone the mogus folder
print('Paste your Among Us install dir, example: C:\Games\Steam\steamapps\common\Among Us')
validPath = False
while not validPath:
    mogus_dir = input('Among Us dir: ')
    if not Path(f"{mogus_dir}\Among Us.exe").is_file():
        print("Invalid Among Us path, please specify the directory with 'Among Us.exe'.")
    else:
        validPath = True
modded_dir = f"{mogus_dir} - ToU"
if Path(f"{modded_dir}\BepInEx").exists():
    print('Cleaning out modded files')
    rmtree(f"{modded_dir}\BepInEx")
if Path(f"{modded_dir}\mono").exists():
    rmtree(f"{modded_dir}\mono")

if not Path(modded_dir).exists():
    copytree(mogus_dir, modded_dir)

# move ToU files to cloned mogus dir
copytree(f'ToU\\ToU {release_tag}', modded_dir, dirs_exist_ok=True)

# Clean up
remove(filename)
rmtree('ToU')
