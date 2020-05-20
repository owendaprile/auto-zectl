# Maintainer: Owen D'Aprile <owendaprile at gmail dot com>
pkgname='auto-zectl'
pkgver=1.0.0
pkgrel=1
pkgdesc='Automatically create zectl boot environments when installing, upgrading, or removing packages'
arch=('any')
url='https://github.com/owendaprile/auto-zectl'
license=('GPL3')
depends=('python' 'zectl')
backup=('etc/auto-zectl.conf')
source=("https://github.com/owendaprile/auto-zectl/archive/v$pkgver.zip")
sha256sums=('e624aab4d86345de74e32ca8605e1b8a6c702fbd796ac0e92ca12c3e19fb2cb5')

package() {
    cd "$pkgname-$pkgver"
    install -Dm644 src/create-environment.py $pkgdir/usr/lib/auto-zectl/create-environment.py
    install -Dm644 src/destroy-environments.py $pkgdir/usr/lib/auto-zectl/destroy-environments.py
    install -Dm644 src/hooks/auto-zectl-create-environment.hook $pkgdir/usr/share/libalpm/hooks/auto-zectl-create-environment.hook
    install -Dm644 src/hooks/auto-zectl-destroy-environments.hook $pkgdir/usr/share/libalpm/hooks/auto-zectl-destroy-environments.hook
    install -Dm644 src/auto-zectl.conf $pkgdir/etc/auto-zectl.conf
    install -Dm644 LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE
}