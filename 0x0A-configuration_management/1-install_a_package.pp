#!/usr/bin/pup
# Install this package for sanbox
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
