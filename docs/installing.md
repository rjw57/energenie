# Installing, updating and removing

Manage your installation of the `energenie` package with `pip`.

## Installing

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

## Version checking

Check which version of `energenie` you have installed by inspecting `__version__`:

```python
import energenie

print(energenie.__version__)
```

or in one line from the command line (Python 3):

```bash
python3 -c "import energenie; print(energenie.__version__)"
```

or for Python 2:

```bash
python -c "import energenie; print(energenie.__version__)"
```

Be sure to check the right version of Python.

## Updating

Update to the latest version of `energenie` with:

```bash
sudo pip-3.2 install energenie --update
```

for Python 3.

or for Python 2:

```bash
sudo pip install energenie --update
```

## Removing

Uninstall the package with:

```bash
sudo pip-3.2 uninstall energenie
```

for Python 3.

or for Python 2:

```bash
sudo pip uninstall energenie
```
