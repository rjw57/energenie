# Reference

## Functions

### switch_on

```python
energenie.switch_on(socket)
```

Switches on a power socket by number. Default is `0` (all).

Using the four-way Energenie, provide the socket number (`1-4`) or `0` for all sockets.

Using the single Energenie unit, provide `0`.

If the socket provided is already switched on, it will stay on.

### switch_off

```python
energenie.switch_off(socket)
```

Switches off a power socket by number. Default is `0` (all).

Using the four-way Energenie, provide the socket number (`1-4`) or `0` for all sockets.

If the socket provided is already switched off, it will stay off.

## Properties

### Version

```
energenie.__version__
```

Provides the version number of the `energenie` package.
