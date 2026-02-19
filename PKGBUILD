# Maintainer: Agil Mammadov <mammadovagil@tutamail.com>
pkgname=flag.h-git
_pkgname=${pkgname%-git}
pkgver=r53.7d36992
pkgrel=1
pkgdesc="Command-line flag parsing in C"
arch=('any')
url="https://github.com/tsoding/flag.h"
license=('MIT')
groups=()
depends=()
makedepends=('git')
provides=("$_pkgname")
conflicts=("$_pkgname")
replaces=()
backup=()
options=('!strip')
install=
source=('git+https://github.com/tsoding/flag.h.git')
noextract=()
sha256sums=('SKIP')

pkgver() {
	cd "$_pkgname"

	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
	cd "$_pkgname"

	install -Dm644 flag.h "$pkgdir/usr/include/flag.h"
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
