# Using Puppet, install Flask from pip3
exec { 'flask':
    command => 'pip3 install flask',
    path    => ['/usr/local/bin', '/usr/bin', '/bin'],
    unless  => 'pip3 show flask'
}
