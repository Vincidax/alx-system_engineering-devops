# File: 0-create_a_file.pp

# This Puppet manifest creates a file in /tmp/school with the specified requirements.

# First, we create the directory /tmp/school if it doesn't exist.
file { '/tmp/school':
  ensure => 'directory',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0744',
}

# Then, we create the file /tmp/school/0-create_a_file.pp with the specified content.
file { '/tmp/school/0-create_a_file.pp':
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet\n',
}
