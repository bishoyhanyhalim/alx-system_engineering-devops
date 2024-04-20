#!/usr/bin/pup
# this command for instull flask

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
