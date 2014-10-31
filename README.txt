This module provides simple control of Energenie power sockets directly from Python.

Example usage:


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

