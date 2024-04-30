# Maintainer: Alex Hirzel <alex at hirzel period us>

pkgname='python-strictdoc'
_name=${pkgname#python-}
pkgver='0.0.55'
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
sha512sums=('081b626e43cbe006220e8a3ee2e639a73808266e006c7760a9168c01c7dc947cb88ecca550b4924a9f49557a357ba17e4411db4eb67804bb810e45d6c7e7c8ce')

build() {
	cd "${srcdir}/${_name}-${pkgver}"
	python -m build --wheel --no-isolation
}

package() {
	cd "${srcdir}/${_name}-${pkgver}"
	python -m installer --destdir="$pkgdir" dist/*.whl
}
