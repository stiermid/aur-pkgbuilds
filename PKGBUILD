# Contributor: Sidney Kuyateh <autinerd-arch@kuyateh.eu>

pkgname=meta-package-manager
pkgver=5.20.0
pkgrel=1
pkgdesc='A wrapper around all package managers'
url='https://kdeldycke.github.io/meta-package-manager/'
makedepends=(git uv)
depends=(python python-boltons python-click-extra python-cyclonedx-lib python-packageurl python-spdx-tools python-tabulate python-tomli-w python-xmltodict)
checkdepends=(python-pytest python-pytest-cov python-pytest-randomly python-pytest-xdist)
optdepends=('apt: support for apt packages'
            'rust: support for Rust packages'
            'composer: support for PHP composer packages'
            'dnf: support for RPM packages'
            'portage: support for Gentoo packages'
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
            'uv: support for Python packages'
            'code: support for VSCode extensions'
            'yarn: support for Node packages'
            'yay: support for AUR packages'
            'zypper: support for RPM packages')
license=('GPL2')
arch=('any')
source=("git+https://github.com/kdeldycke/${pkgname}.git#commit=479d9aa5c1ee3a839af19819ba2961fbeb868c75"
	"click-extra-4.15.0.patch")
sha512sums=('f9b1603355be203195b5ceeab8e3ce49f0d29fb5213a0cb97d43e35b9ecb22ebe18ae552fd48930e7aead82aca539d674e43bd619e27fdec7d288c0668b9ec31'
            'db4bc2e5aaad5e6f2e1db8d4abaff0e4eaeee40fccd10834e8261dbf6234e122d3be68aa92354ce3aa457561a1fd7b62cf72bf4d5896e4f785e17a69b6ed4b04')

pkgver() {
  cd "$srcdir/$pkgname"
  git describe --tags | sed 's/^v//;s/[^-]*-g/r&/;s/-/+/g'
}

prepare(){
    cd "$srcdir/$pkgname"
    patch -p1 -i ../click-extra-4.15.0.patch
}

build() {
    cd "$srcdir/$pkgname"
    uv build
}

package() {
    cd "$srcdir/$pkgname"
    uv pip install --system --link-mode=copy --no-deps --prefix="$pkgdir/usr" dist/*.whl
    rm "$pkgdir/usr/.lock"
    install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" license
}
