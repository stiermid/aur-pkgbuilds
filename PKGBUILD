# Maintainer: Michał Wojdyła < micwoj9292 at gmail dot com >
# Contributor: Sidney Kuyateh <autinerd-arch@kuyateh.eu>

pkgname=python-extra-platforms
_name=${pkgname#python-}
pkgver=7.0.0
pkgrel=1
pkgdesc='Detect platforms and group them by family'
url='https://github.com/kdeldycke/extra-platforms'
makedepends=(uv)
depends=(python python-distro)
#checkdepends=(python-pytest python-pytest-cov python-pytest-randomly)
license=('GPL2')
arch=('any')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/kdeldycke/${_name}/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('bbf4333e286c3d6fbd2c093e4c38da2eee7ef0630c5364d54b8eeb1a801e41be7932ff64dddcd2c175a83d9805d346d5c2b4724fab06dd0d6108841b2a8b2d26')

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
