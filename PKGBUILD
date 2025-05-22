# Maintainer: Michał Wojdyła < micwoj9292 at gmail dot com >
# Contributor: Sidney Kuyateh <autinerd-arch@kuyateh.eu>

pkgname=python-extra-platforms
_name=${pkgname#python-}
pkgver=3.2.1
pkgrel=1
pkgdesc='Detect platforms and group them by family'
url='https://github.com/kdeldycke/extra-platforms'
makedepends=(uv)
depends=(python python-boltons python-distro)
#checkdepends=(python-pytest python-pytest-cov python-pytest-randomly)
license=('GPL2')
arch=('any')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/kdeldycke/${_name}/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('0d2509b3f1214cebe6e8c26720ef222d00e6f550b0edac65d998fc6942d650537f2afa3a2ea917a67737fdb67c3a602e64e26537438bcfc97aeddb10789c39fb')

build() {
    cd "$srcdir/$_name-$pkgver"
    uv build
}

package() {
    cd "$srcdir/$_name-$pkgver"
    uv pip install --system --link-mode=copy --no-deps --prefix="$pkgdir/usr" dist/*.whl
    rm "$pkgdir/usr/.lock"
    install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" license
}
