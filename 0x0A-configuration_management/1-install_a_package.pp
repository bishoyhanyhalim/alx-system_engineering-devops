#!/usr/bin/pup
# Install this package for sanbox
package {'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3'
}

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
