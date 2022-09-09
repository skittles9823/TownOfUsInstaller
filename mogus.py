# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.

import zipfile
from glob import glob
from os import remove
from pathlib import Path
from shutil import copytree, move, rmtree

from requests import get

# find the download URL and filename of the latest ToU release
release = get(
    'https://api.github.com/repos/eDonnes124/Town-Of-Us-R/releases/latest'
)
release = release.json()
filename = Path(release['assets'][0]['name'])

# Download latest version of ToU and name the zip after it's github release zip
print(f"Downloading {filename}, please wait.")
mogus = get(release['assets'][0]['browser_download_url'])
filename.write_bytes(mogus.content)

# Extract the zip
mogus_zip = zipfile.ZipFile(filename)
mogus_zip.extractall(Path("ToU"))
mogus_zip.close()

# Clone the mogus folder
print('Paste your Among Us install dir, example: C:\Games\Steam\steamapps\common\Among Us')
mogus_dir = input('Among Us dir: ')
modded_dir = f"{mogus_dir} - ToU"
copytree(mogus_dir, modded_dir)

# move ToU files to cloned mogus dir
for file in glob('ToU/**/**'):
    move(file, modded_dir)

# Clean up
remove(filename)
rmtree('ToU')
