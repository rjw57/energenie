from mock import patch, MagicMock, call
from nose.tools import assert_greater_equal, assert_equal

# Energenie I/O pins in bit 4, 3, 2 and 1 order
_IO_PINS = [27, 23, 22, 17]

# Energenie control pins
_ON_OFF = 24
_ENABLE = 25

# We need to explicitly create a mock for RPio.GPIO since we want to have the
# mock used at import time. Create a mocked RPi.GPIO module which we can use to
# test energenie without a) having to have the hardware installed and/or b)
# having to run on the pi.
_RPi_mock = MagicMock()
_RPi_mock.GPIO = MagicMock()

# This is the dict which should be patched into sys.modules to make imports
# work.
_mocked_modules = {
    'RPi': _RPi_mock,
    'RPi.GPIO': _RPi_mock.GPIO,
}

_GPIO_PATCHER = patch.dict('sys.modules', _mocked_modules)

@_GPIO_PATCHER
def test_energenie_initial_setup():
    """Tests that energenie initialises the module correctly at import time."""
    import energenie
    GPIO = _RPi_mock.GPIO

    GPIO.setmode.assert_called_once_with(GPIO.BCM)
    GPIO.setwarnings.assert_called_once_with(False)

    # Check pins are set up for output
    for pin in _IO_PINS + [_ON_OFF, _ENABLE]:
        GPIO.setup.assert_any_call(pin, GPIO.OUT)

    # Check all pins are low
    for pin in _IO_PINS + [_ON_OFF, _ENABLE]:
        GPIO.output.assert_any_call(pin, False)

def _assert_enabled_toggled():
    # The enable pin should've been toggled high and *then* low
    _RPi_mock.GPIO.output.assert_has_calls([
        call(_ENABLE, True),
        call(_ENABLE, False),
    ])

def _assert_one_on(socket_num):
    # Assert that a single socket was switched on
    code = [0b1111, 0b1110, 0b1101, 0b1100][socket_num - 1]
    for bit in range(4):
        value = True if code & (1<<bit) != 0 else False
        _RPi_mock.GPIO.output.assert_any_call(_IO_PINS[3-bit], value)

def _assert_one_off(socket_num):
    # Assert that a single socket was switched off
    code = [0b0111, 0b0110, 0b0101, 0b0100][socket_num - 1]
    for bit in range(4):
        value = True if code & (1<<bit) != 0 else False
        _RPi_mock.GPIO.output.assert_any_call(_IO_PINS[3-bit], value)

@_GPIO_PATCHER
def test_switch_all_on():
    from energenie import switch_on

    GPIO = _RPi_mock.GPIO
    GPIO.output.reset_mock()
    assert_equal(GPIO.output.call_count, 0)

    switch_on()

    # We should've set at least six pins
    assert_greater_equal(GPIO.output.call_count, 6)

    GPIO.output.assert_any_call(_IO_PINS[0], True)
    GPIO.output.assert_any_call(_IO_PINS[1], False)
    GPIO.output.assert_any_call(_IO_PINS[2], True)
    GPIO.output.assert_any_call(_IO_PINS[3], True)

    _assert_enabled_toggled()

@_GPIO_PATCHER
def test_switch_all_off():
    from energenie import switch_off

    GPIO = _RPi_mock.GPIO
    GPIO.output.reset_mock()
    assert_equal(GPIO.output.call_count, 0)

    switch_off()

    # We should've set at least six pins
    assert_greater_equal(GPIO.output.call_count, 6)

    GPIO.output.assert_any_call(_IO_PINS[0], False)
    GPIO.output.assert_any_call(_IO_PINS[1], False)
    GPIO.output.assert_any_call(_IO_PINS[2], True)
    GPIO.output.assert_any_call(_IO_PINS[3], True)

    _assert_enabled_toggled()

@_GPIO_PATCHER
def test_switch_on_individual():
    from energenie import switch_on

    # Test switching on each socket in turn
    for socket in range(1,5):
        print("Testing socket {0}".format(socket))
        _RPi_mock.GPIO.output.reset_mock()
        switch_on(socket)
        print(_RPi_mock.GPIO.output.mock_calls)
        _assert_one_on(socket)
        _assert_enabled_toggled()

@_GPIO_PATCHER
def test_switch_off_individual():
    from energenie import switch_off

    # Test switching off each socket in turn
    for socket in range(1,5):
        print("Testing socket {0}".format(socket))
        _RPi_mock.GPIO.output.reset_mock()
        switch_off(socket)
        print(_RPi_mock.GPIO.output.mock_calls)
        _assert_one_off(socket)
        _assert_enabled_toggled()
