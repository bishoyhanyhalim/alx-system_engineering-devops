# this puppet file for fix our stack so that we get to 0

exec {'fix--for-nginx':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart-nginxS'],
}

exec {'restart-nginxS':  
  provider => shell,
  command  => 'sudo service nginx restart',
}
