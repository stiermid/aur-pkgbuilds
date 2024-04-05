# Maintainer: Sidney Kuyateh <autinerd-arch@kuyateh.eu>

pkgname=meta-package-manager
pkgver=5.15.0
pkgrel=1
pkgdesc='A wrapper around all package managers'
url='https://kdeldycke.github.io/meta-package-manager/'
makedepends=(python-build python-installer python-wheel python-poetry-core)
depends=('python>=3.7' python-boltons python-click 'python-click-extra>=3.10.0' python-packageurl python-tabulate python-tomli python-tomli-w python-typing_extensions python-xmltodict)
checkdepends=(python-pytest python-pytest-cov python-pytest-randomly python-pytest-xdist)
optdepends=('apt: support for apt packages'
            'rust: support for Rust packages'
            'composer: support for PHP composer packages'
            'dnf: support for RPM packages'
            'flatpak: support for Flatpak packages'
            'rubygems: support for Ruby packages'
            'npm: support for Node.js packages'
            'opkg: support for OPKG packages'
            'pacaur: support for AUR packages'
            'pacman: support for Pacman packages'
            'paru: support for AUR packages'
            'python-pip: support for Python packages'
            'python-pipx: support for Python pipx packages'
            'snapd: support for Snap packages'
            'steamcmd: support for Steam games'
            'code: support for VSCode extensions'
            'yarn: support for Node packages'
            'yay: support for AUR packages'
            'zypper: support for RPM packages')
license=('GPL2')
arch=('any')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/kdeldycke/${pkgname}/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('1a86f411a3e6d41f75a413c62edd242ec8c4d577fe44948f15d728e8b2f683b06b796d4699a6047bf3d21d1e9e780e4d58cf12a6840747f340ad8fb12de179a4')


build() {
    cd "$srcdir/$pkgname-$pkgver"
    GIT_DIR="$srcdir/$pkgname-$pkgver" python -m build --wheel --no-isolation
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" license
}
