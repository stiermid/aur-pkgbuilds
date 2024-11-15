# Maintainer: Alex Hirzel <alex at hirzel period us>

pkgname='python-strictdoc'
_name=${pkgname#python-}
pkgver='0.2.1'
pkgrel=1
pkgdesc="Software for writing technical requirements and specifications."
url="https://github.com/strictdoc-project/strictdoc"
depends=(
	'python-beautifulsoup4'
	'python-datauri'
	'python-docutils'
	'python-fastapi'
	'python-html5lib'
	'python-jinja'
	'python-lxml'
	'python-multipart'
	'python-pybtex'
	'python-pygments'
	'python-reqif'
	'python-requests'
	'python-selenium'
	'python-semantic-version'
	'python-spdx-tools'
	'python-textx'
	'python-toml'
	'python-tree-sitter'
	'python-xlrd'
	'python-xlsxwriter'
	'uvicorn'
)
optdepends=(
	'python-graphviz'
	'python-webdriver-manager'
)
makedepends=('python-pipreqs' 'python-setuptools')
license=('Apache-2.0')
arch=('any')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha512sums=('cec299c36d5adc6c0135d5ba9cd09c39b9866f3ed90a0db2e180dba5e2ea5e0b2c7630dc39d0aaf7606be6eac312a4b3f5153af0e820e2d8f07858acc509724c')

build() {
	cd "${srcdir}/${_name}-${pkgver}"
	python -m build --wheel --no-isolation
}

package() {
	cd "${srcdir}/${_name}-${pkgver}"
	python -m installer --destdir="$pkgdir" dist/*.whl
}
