# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Set up Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "\
server {
    listen 80;
    server_name _;

    location / {
        add_header Content-Type text/html;
        return 200 'Hello World!';
    }

    location /redirect_me {
        return 301 https://www.example.com;
    }
}",
  notify  => Service['nginx'],
}

# Symbolic link for enabling the site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
