=========
energenie
=========

Python module to control the `Energenie`_ add-on board for the `Raspberry Pi`_ used for remotely turning power sockets on and off.

Installation
============

On Raspberry Pi, install the energenie module in pip.

Python 3::

    sudo apt-get install python3-pip
    sudo pip-3.2 install energenie

Python 2::

    sudo apt-get install python-pip
    sudo pip install energenie

Usage
=====

Example usage::

    from energenie import switch_on, switch_off
    from time import sleep

    # turn a plug socket on and off by number
    switch_on(1)
    switch_off(1)

    switch_on(3)
    switch_off(3)

    # turn all plug sockets on and off
    switch_on(0)
    switch_off(0)

    # turn some plug sockets on, then turn them off after 10 seconds
    switch_on(1)
    switch_on(4)
    sleep(10)
    switch_off(1)
    switch_off(4)

Contributors
============

* `Ben Nuttall`_
* `Amy Mather`_
* `Gordon Hollingworth`_

Open Source
===========

* The code is licensed under the `BSD Licence`_
* The project source code is hosted on `GitHub`_
* Please use `GitHub issues`_ to submit bugs and report issues


.. _Energenie: https://energenie4u.co.uk/
.. _Raspberry Pi: http://www.raspberrypi.org/
.. _Ben Nuttall: https://github.com/bennuttall
.. _Amy Mather: https://github.com/minigirlgeek
.. _Gordon Hollingworth: https://github.com/ghollingworth
.. _BSD Licence: http://opensource.org/licenses/BSD-3-Clause
.. _GitHub Issues: https://github.com/bennuttall/energenie
.. _GitHub: https://github.com/bennuttall/energenie/issues

