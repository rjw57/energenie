# Energenie

Python module to control the [Energenie](https://energenie4u.co.uk/) add-on board for the [Raspberry Pi](http://www.raspberrypi.org/) used for remotely turning power sockets on and off.

## Installation

On Raspberry Pi, install the `energenie` module in `pip`.

### Python 3:

```bash
sudo apt-get install python3-pip
sudo pip-3.2 install energenie
```

### Python 2:

```bash
sudo apt-get install python-pip
sudo pip install energenie
```

## Usage

```python
from energenie import switch_on, switch_off
from time import sleep

# turn all plug sockets on and off
switch_on()
switch_off()

# turn a plug socket on and off by number
switch_on(1)
switch_off(1)

switch_on(3)
switch_off(3)

# turn some plug sockets on, then turn them off after 10 seconds
switch_on(1)
switch_on(4)
sleep(10)
switch_off(1)
switch_off(4)
```

## Contributors

- [Ben Nuttall](https://github.com/bennuttall) (project maintainer)
- [Amy Mather](https://github.com/minigirlgeek)
- [Gordon Hollingworth](https://github.com/ghollingworth)

## Open Source

- The code is licensed under the [BSD Licence](http://opensource.org/licenses/BSD-3-Clause)
- The project source code is hosted on [GitHub](https://github.com/bennuttall/energenie)
- Please use [GitHub issues](https://github.com/bennuttall/energenie) to submit bugs and report issues
