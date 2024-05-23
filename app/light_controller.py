"""
This module will contain the light controller code
Since developing on a Windows PC there is also a mock implementation

The mock needs to be fleshed out with any used functions
The real code needs to be added
"""


# Mock the Neopixel module
from typing import List
from unittest.mock import Mock
# import sys
# neopixel = Mock()
# board = Mock()
# sys.modules['neopixel'] = neopixel
# sys.modules['board'] = board
# # these imports have to go after the mock exampples other wise they throw an error
# import board
# import neopixel

class MockLEDStrip:
    """
    Mock LED Strip Class
    This supports the functionality that would be present on the Raspberry Pi.
    """

    def __init__(self, num_leds, brightness=1):
        """
        Initialize the mock LED strip.

        Args:
            num_leds (int): The number of LEDs in the strip.
            brightness (int, optional): The brightness level of the LEDs. Defaults to 1.
        """
        self.num_leds = num_leds
        self.leds = [(0, 0, 0)] * num_leds  # Assume LEDs are off initially
        self.brightness = brightness

    def __getitem__(self, index):
        """
        Get the color value of the LED at the specified index.

        Args:
            index (int): The index of the LED.

        Returns:
            tuple: The color value of the LED at the specified index.
        """
        return self.leds[index]

    def __setitem__(self, index, value):
        """
        Set the color value of the LED at the specified index.

        Args:
            index (int): The index of the LED.
            value (tuple): The color value to set (e.g., (0, 25, 255)).
        """
        self.leds[index] = value

    def show(self):
        """
        Print the current state of all LEDs in the strip.
        """
        print(f"LED states: {self.leds}")

    def fill(self, value):
        """
        Fill all LEDs in the strip with the specified color value.

        Args:
            value (tuple): The color value to set (e.g., (0, 25, 255)).
        """
        self.leds = [value] * self.num_leds
        print(f"fill used to: {value}")

    @classmethod
    def NeoPixel(cls, board, num_leds, brightness): # pylint: disable=C0103
        """
        Create a new instance of the mock LED strip.

        Args:
            board (str): The board pin identifier (e.g., board.D18).
            num_leds (int): The number of LEDs in the strip.
            brightness (int): The brightness level of the LEDs.

        Returns:
            MockLEDStrip: A new instance of the mock LED strip.
        """
        print("just to use board", board)
        return cls(num_leds, brightness)


neopixel = MockLEDStrip # pylint: disable=C0103


def turn_on_lights(led_positions: List[int]):
    """
    Turn on the LEDs for the provided list of positions
    """
    print("we are turning on lights")
    # enable board strip
    board = Mock()
    board.D18 = "D18"
    # should turn this into a global at somepoint
    lights = neopixel.NeoPixel(board.D18, 200, 1)
    for pos in led_positions:
        # turn the lights on, can change to whatever color
        # hardcoded color for now
        lights[pos] = (0,25,255)
    print("lights on")

def turn_off_lights():
    """
    Turn off all LEDs
    """
    board = Mock()
    board.D18 = "D18"
    lights = neopixel.NeoPixel(board.D18, 200, 1)
    lights.fill((0,0,0))
