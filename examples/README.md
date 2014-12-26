# Examples

## Simple examples

### [on.py](simple/on.py)

Simple script to switch socket(s) on

```python
from energenie import switch_on

switch_on()
```

### [off.py](simple/off.py)

Simple script to switch socket(s) off

```python
from energenie import switch_off

switch_off()
```

### [on_off.py](simple/on_off.py)

Simple script to switch socket(s) on and off every 2 seconds

```python
from energenie import switch_on, switch_off
from time import sleep

while True:
    print("switching on...")
    switch_on()
    sleep(2)
    print("switching off...")
    switch_off()
    sleep(2)
```

## Advanced examples

### [Web Interface](advanced/web.md)

Use Python web framework Flask to create a simple web interface to switch socket(s) on and off

[![](images/web.png)](advanced/web.md)
