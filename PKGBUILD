# Maintainer: Agil Mammadov <mammadovagil@tutamail.com>
pkgname=lamb-git
_pkgname=${pkgname%-git}
pkgver=r68.b5f6c02
pkgrel=1
pkgdesc="Tiny Pure Functional Programming Language in C"
arch=('x86_64')
url="https://github.com/tsoding/lamb"
license=('MIT')
groups=()
depends=()
makedepends=('git' 'gcc')
provides=("$_pkgname")
conflicts=("$_pkgname")
replaces=()
backup=()
options=('!strip')
install=
source=('git+https://github.com/tsoding/lamb.git')
noextract=()
sha256sums=('SKIP')

pkgver() {
	cd "$_pkgname"

	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
	cd "$_pkgname"

	gcc -o lamb lamb.c
}

package() {
	cd "$_pkgname"

	install -Dm755 "$_pkgname" "$pkgdir/usr/bin/lamb"
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$_pkgname/LICENSE"
}
