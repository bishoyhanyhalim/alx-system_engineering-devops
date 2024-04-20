# this is kill file

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
