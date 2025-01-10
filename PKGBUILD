pkgbase=python-nodejs-wheel
pkgname=(python-nodejs-wheel python-nodejs-wheel-binaries)
pkgver=22.13.0
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
sha256sums=('c56df577a119635a47ab3c4c8602a44b6254b0e4cb2041d10e0029764685314b'
            '8dff4e741b016af2ff7fbb1f42ebc9c15478846f322d4574646cb3647acc73c9')
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
