file { '/etc/apache2/sites-available/default-ssl.conf':
  ensure  => present,
  content => 'new contents of the file',
}