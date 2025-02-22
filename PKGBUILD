# Contributor: Sidney Kuyateh <autinerd-arch@kuyateh.eu>

pkgname=python-extra-platforms
_name=${pkgname#python-}
pkgver=2.1.0
pkgrel=1
pkgdesc='Detect platforms and group them by family'
url='https://kdeldycke.github.io/extra-platforms/'
makedepends=(uv)
depends=(python python-boltons python-distro)
#checkdepends=(python-pytest python-pytest-cov python-pytest-randomly)
license=('GPL2')
arch=('any')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/kdeldycke/${_name}/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('bd3fda523679d816662edb4a2f853fc1f177caf57fcc9dbfff900b2dcf0128f61372d1cccda70df57a4ea38dfb6faca2b5ae76f49e4a35f01ffc03f52d3c62f8')

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
