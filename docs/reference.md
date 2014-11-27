# Function Reference

## switch_on

`energenie.switch_on(socket)`

Switches on a power socket by number. Default is `0` (all).

Using the four-way Energenie, provide the socket number (`1-4`) or `0` for all sockets.

Using the single Energenie unit, provide `0`.

If the socket provided is already switched on, it will stay on.

## switch_off

`energenie.switch_off(socket)`. Default is `0` (all).

Switches off a power socket by number.

Using the four-way Energenie, provide the socket number (`1-4`) or `0` for all sockets.

If the socket provided is already switched off, it will stay off.
