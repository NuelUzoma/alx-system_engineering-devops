# Using strace, find out why Apache is returning a 500 error
file { '/etc/apache2/sites-available/default-ssl.conf':
  ensure  => present,
  content => 'new contents of the file',
}