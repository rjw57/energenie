# Energenie Demo

Python module to control the [Energenie](https://energenie4u.co.uk/) add-on board for the [Raspberry Pi](http://www.raspberrypi.org/) used for remotely turning power sockets on and off.

## Usage

```python
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
```
## Contributors

- [Amy Mather](https://github.com/minigirlgeek)
- [Ben Nuttall](https://github.com/bennuttall)
- [Gordon Hollingworth](https://github.com/ghollingworth)
