# fix for HTTP requests limits to server
exec { 'replace_softlimit':
  command  => 'sed -i "s|ULIMIT=\"-n 15\"|ULIMIT=\"-n 10000\"|" /etc/default/nginx',
  provider => 'shell',
}
-> exec { 'nginx_restart':
  command  => 'service nginx restart',
  provider => 'shell',
}
