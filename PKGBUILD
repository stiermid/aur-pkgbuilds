pkgbase=python-nodejs-wheel
pkgname=(python-nodejs-wheel python-nodejs-wheel-binaries)
pkgver=20.18.0
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
sha256sums=('e8a3ae7026f64d303d0240f006a9de23cca135d96dbccf41299fcf1018d307c3'
            '651bb82f6af18084070893559643759165ce050b5839f830d4cc098130d3ad89')
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
