# Maintainer: Rafael Dominiquini <rafaeldominiquini at gmail dot com>

_upstreamver='1.0.0'
_upstreamver_regex='^[0-9]+\.[0-9]+\.[0-9]+$'
_source_type='pypi-releases'
_pypi_package='textual-fspicker'

pkgname="python-${_pypi_package}"
pkgver="${_upstreamver}"
pkgrel=1
pkgdesc="A simple Textual filesystem picker dialog library"
arch=('any')
url='https://github.com/davep/textual-fspicker'
license=('MIT')
depends=('python' 'python-textual')
optdepends=()
makedepends=('python-setuptools' 'python-wheel' 'python-build' 'python-uv-build' 'python-installer')
source=("https://files.pythonhosted.org/packages/source/${_pypi_package::1}/${_pypi_package//-/_}/${_pypi_package//-/_}-${pkgver}.tar.gz"
        "https://raw.githubusercontent.com/davep/${_pypi_package}/v${pkgver}/LICENSE")
sha256sums=('462608dbe6a14edff679fc6116addcf288f4a79f8e4fffd240f9ce2caaf9e655'
            '9a3f784f2f73961691644b9f24eee2a82f761d9a0220e66786feadde9a38c124')


build() {
    cd "${srcdir}/${_pypi_package//-/_}-${pkgver}/"

    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pypi_package//-/_}-${pkgver}/"

    python -m installer --destdir="${pkgdir}" dist/*.whl

    install -Dm644 "README.md" "${pkgdir}/usr/share/doc/${pkgname}/README.md"

    install -Dm644 "../LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
