# Maintainer: Alex Hirzel <alex at hirzel period us>

pkgname='python-strictdoc'
_name=${pkgname#python-}
pkgver='0.0.54'
pkgrel=1
pkgdesc="Software for writing technical requirements and specifications."
url="https://github.com/strictdoc-project/strictdoc"
depends=(
	'python-beautifulsoup4'
	'python-datauri'
	'python-docutils'
	'python-fastapi'
	'python-graphviz'
	'python-pybtex'
	'python-pygments'
	'python-reqif'
	'python-requests'
	'python-semantic-version'
	'python-textx'
	'python-toml'
	'python-xlrd'
	'python-xlsxwriter'
	'uvicorn'
)
optdepends=(
	'python-selenium'
	'python-webdriver-manager'
)
makedepends=('python-pipreqs' 'python-setuptools')
license=('Apache-2.0')
arch=('any')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha512sums=('e221d482e2e4e4f9b276f46e12678f31b42d4de2c8ad7a7da5bea64235249edbcd19fe47d7c95a55777d41a1307a06d6982fe3444680d99028a9a6d1ce0b4733')

build() {
	cd "${srcdir}/${_name}-${pkgver}"
	python -m build --wheel --no-isolation
}

package() {
	cd "${srcdir}/${_name}-${pkgver}"
	python -m installer --destdir="$pkgdir" dist/*.whl
}
