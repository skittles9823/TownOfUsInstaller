# Town of Us - R Installer

## Usage

To use, either download and run the exe from [releases](https://github.com/skittles9823/TownOfUsInstaller/releases/latest), or run `python mogus.py`

 - The only needed user input is the game path.

- I'd recommend adding the cloned 'Among Us - ToU' game as a non-steam game in steam for quick access to launch the mod.

## Note
Literally as soon as I published this repo, I found out that I've essentially rewritten an existing installer, Go check out the less jank version of this installer, [Modinstaller](https://github.com/whichtwix/Modinstaller) by Twix

After reading their code I updated my installer to address possible user error, reusability issues, and github api responses.

## Differences from [Modinstaller](https://github.com/whichtwix/Modinstaller)
Currently, the only differences (aside the fact they're written in different languages) are that my installer will clone the Among Us game path and install the mod to the cloned game, while theirs assumes you've done so already, or it will install the mod to the base game directory.
