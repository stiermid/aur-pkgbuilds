pkgbase=python-nodejs-wheel
pkgname=(python-nodejs-wheel python-nodejs-wheel-binaries)
pkgver=22.12.0
pkgrel=1
pkgdesc="Unoffical Node.js wheels"
arch=("x86_64")
url="https://pypi.org/project/nodejs-wheel/"
license=("MIT")
depends=("python")
options=(!lto)
makedepends=(
    "python-installer" "python-build" "python-scikit-build-core" "python-setuptools-scm" "python-wheel"
    "python-hatchling" "python-hatch-vcs")
source=(
    "$pkgname-$pkgver.tar.gz::https://github.com/njzjz/nodejs-wheel/archive/refs/tags/v$pkgver.tar.gz"
    "nodejs-$pkgver.tar.gz::https://github.com/nodejs/node/archive/refs/tags/v$pkgver.tar.gz"
)
sha256sums=('9595ac9c1befd0c598c311efbcd9d98a027b917dbef99131bfb62d152a972e3c'
            '635eb3e14a42ca33b65b80598c4d062e62507659a47b76e02a040d5e40295bba')
noextract=("nodejs-$pkgver.tar.gz")

prepare() {
    cd "$srcdir/nodejs-wheel-$pkgver"
    sed -i "s|https://github.com/nodejs/node/archive/refs/tags/v|file://$srcdir/nodejs-|g" \
        CMakeLists.txt
}
build() {
    cd "$srcdir/nodejs-wheel-$pkgver"
    echo "Building nodejs-wheel-binaries..."
    python -m build --wheel --no-isolation
    cd cmd
    echo "Building nodejs-wheel cli tools..."
    sed -i "s/source = \"vcs\"/source = \"vcs\"\nfallback-version = \"$pkgver\"/" \
        pyproject.toml
    python -m build --wheel --no-isolation
}
package_python-nodejs-wheel() {
    depends+=("python-nodejs-wheel-binaries")
    pkgdesc+=" (CLI tools)"
    conflicts=("nodejs" "npm")
    provides=("nodejs=$pkgver" "npm")

    cd "$srcdir/nodejs-wheel-$pkgver"
    python -m installer --destdir="$pkgdir" cmd/dist/*.whl
    install -Dm644 cmd/LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

}
package_python-nodejs-wheel-binaries() {
    cd "$srcdir/nodejs-wheel-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
