#!/usr/bin/expect
set timeout 30

spawn sudo nginx
expect {
	"Password:" {
		send "light\r"
		exp_continue
	} eof {
		send_user "eof\r"
	}
}

spawn sudo php-fpm
expect {
	"Password:" {
		send "light\r"
	} eof {
		send_user "success start nginx&&php-fpm\n"
	}
}
