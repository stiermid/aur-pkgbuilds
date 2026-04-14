# AUR [PKGBUILDs](https://wiki.archlinux.org/title/PKGBUILD)

This repository contains the packages I maintain in the
[AUR](https://aur.archlinux.org).

Powered by [aurpublish](https://github.com/eli-schwartz/aurpublish)!

## Checking for updates

Each package directory contains its own `.nvchecker.toml`. Run `check_updates.py`
to merge all per-package configs, invoke [nvchecker](https://github.com/lilydjwg/nvchecker)
once, and see which packages have a new upstream version available:

```sh
python check_updates.py
```

## License

GNU General Public License v3.0 only ([GPL-3.0-only](https://www.gnu.org/licenses/gpl.txt))
