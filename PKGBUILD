# Maintainer: Agil Mammadov <mammadovagil@tutamail.com>
pkgname=nodejs-ramadan-cli
_pkgname=${pkgname#nodejs-}
pkgver=6.0.1
pkgrel=1
pkgdesc="CLI to check Sehar and Iftar times in Ramadan"
arch=('any')
url="https://github.com/ahmadawais/ramadan-cli"
license=('MIT')
depends=('nodejs')
makedepends=('npm' 'jq')
source=("https://registry.npmjs.org/$_pkgname/-/$_pkgname-$pkgver.tgz")
noextract=("${_pkgname}-${pkgver}.tgz")
sha256sums=('e4fba6746fcd7be25a5ab724e73452e036f1358054f144b4fe0f27725d659327')

package() {
	npm install -g --prefix "${pkgdir}/usr" "${srcdir}/${_pkgname}-${pkgver}.tgz"

	# remove references to $pkgdir
	find "$pkgdir" -type f -name package.json -print0 | xargs -0 sed -i "/_where/d"

	# remove references to $srcdir
	local tmppackage="$(mktemp)"
	local pkgjson="$pkgdir/usr/lib/node_modules/$_pkgname/package.json"
	jq '.|=with_entries(select(.key|test("_.+")|not))' "$pkgjson" > "$tmppackage"
	mv "$tmppackage" "$pkgjson"
	chmod 644 "$pkgjson"

}
