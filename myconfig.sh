#! /bin/bash
#./configure --prefix=/usr/local/php --enable-fpm --with-pdo-mysql --enable-mbstring --with-mcrypt --enable-mysqlnd --enable-opcache --with-openssl --with-curl --enable-intl --with-icu-dir=/usr/local/Cellar/icu4c/55.1
./configure --prefix=/usr/local/php --enable-fpm --with-pdo-mysql --enable-mbstring --with-mcrypt --enable-mysqlnd --enable-opcache --with-openssl --with-curl --enable-intl --with-gd --with-jpeg-dir --with-png-dir --with-freetype-dir --with-zlib-dir --enable-phpdbg --enable-phpdbg-webhelper --enable-phpdbg-debug --enable-debug
make
sudo make install
cp php.ini-development /usr/local/php/php.ini
cp /usr/local/etc/php-fpm.conf.default /usr/local/etc/php-fpm.conf
cp sapi/fpm/php-fpm /usr/local/bin
