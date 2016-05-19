# -*- coding: utf-8 -*-

from __future__ import division, print_function
from __future__ import unicode_literals, absolute_import

from scipy.interpolate import UnivariateSpline
import numpy as np
import colorsys
import random


class Color(object):
    """
    Color is a class which stores commonly used colors.

    Default color space is RGB.
    """
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)

    LEGO_BLUE = (0, 50, 150)
    LEGO_ORANGE = (255, 150, 40)

    VIOLET = (181, 126, 220)
    ORANGE = (255, 165, 0)
    GREEN = (0, 128, 0)
    GRAY = (128, 128, 128)

    # Extended Colors
    IVORY = (255, 255, 240)
    BEIGE = (245, 245, 220)
    WHEAT = (245, 222, 179)
    TAN = (210, 180, 140)
    KHAKI = (195, 176, 145)
    SILVER = (192, 192, 192)
    CHARCOAL = (70, 70, 70)
    NAVYBLUE = (0, 0, 128)
    ROYALBLUE = (8, 76, 158)
    MEDIUMBLUE = (0, 0, 205)
    AZURE = (0, 127, 255)
    CYAN = (0, 255, 255)
    AQUAMARINE = (127, 255, 212)
    TEAL = (0, 128, 128)
    FORESTGREEN = (34, 139, 34)
    OLIVE = (128, 128, 0)
    LIME = (191, 255, 0)
    GOLD = (255, 215, 0)
    SALMON = (250, 128, 114)
    HOTPINK = (252, 15, 192)
    FUCHSIA = (255, 119, 255)
    PUCE = (204, 136, 153)
    PLUM = (132, 49, 121)
    INDIGO = (75, 0, 130)
    MAROON = (128, 0, 0)
    CRIMSON = (220, 20, 60)
    DEFAULT = (0, 0, 0)
    # These are for the grab cut / findBlobsSmart
    BACKGROUND = (0, 0, 0)
    MAYBE_BACKGROUND = (64, 64, 64)
    MAYBE_FOREGROUND = (192, 192, 192)
    FOREGROUND = (255, 255, 255)
    WATERSHED_FG = (255, 255, 255)  # Watershed foreground
    WATERSHED_BG = (128, 128, 128)  # Watershed background
    WATERSHED_UNSURE = (0, 0, 0)

    colors = [
        BLACK, WHITE, BLUE, YELLOW, RED, VIOLET, ORANGE, GREEN, GRAY, IVORY,
        BEIGE, WHEAT, TAN, KHAKI, SILVER, CHARCOAL, NAVYBLUE, ROYALBLUE,
        MEDIUMBLUE, AZURE, CYAN, AQUAMARINE, TEAL, FORESTGREEN, OLIVE, LIME,
        GOLD, SALMON, HOTPINK, FUCHSIA, PUCE, PLUM, INDIGO, MAROON, CRIMSON,
        DEFAULT,
    ]

    @classmethod
    def random(cls):
        """
        Generate a random RGB color.

        Returns:
            (tuple) a color.

        Examples:
            >>> color = Color.random()
        """
        r = random.randint(1, len(cls.colors) - 1)
        return cls.colors[r]

    @classmethod
    def rgb2hsv(cls, color):
        """
        Convert a RGB color to HSV color.

        Args:
            color (tuple): RGB color

        Returns:
            (tuple) a color in HSV

        Examples:
            >>> color = Color.random()
            >>> print(color)
            >>> color = Color.rgb2hsv(color)
            >>> print(color)
        """
        hsv = colorsys.rgb_to_hsv(*color)
        return hsv[0] * 180, hsv[1] * 255, hsv[2]

    @classmethod
    def hue(cls, color):
        """
        Get corresponding Hue value of the given RGB value.

        Args:
            color (tuple): an RGB color to be converted

        Returns:
            (tuple) a color in HSV

        Examples:
            >>> color = Color.random()
            >>> print(color)
            >>> hue = Color.hue(color)
            >>> print(hue)
        """
        hue = colorsys.rgb_to_hsv(*color)[0]
        return hue * 180

    @classmethod
    def hue2rgb(cls, hue):
        """
        Get corresponding RGB value of the given hue.

        Args:
            hue (int, float): the hue to be convert

        Returns:
            (tuple) a color in RGB

        Examples:
            >>> color = Color.random()
            >>> print(color)
            >>> hue = Color.hue(color)
            >>> color1 = Color.hue2rgb(hue)
            >>> print(color1)
        """
        hue /= 180.0
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)

        return round(255.0 * r), round(255.0 * g), round(255.0 * b)

    @classmethod
    def hue2bgr(cls, hue):
        """
        Get corresponding BGR value of the given hue

        Args:
            hue (int, float): the hue to be convert

        Returns:
            (tuple) a color in BGR

        Examples:
            >>> color = Color.random()
            >>> print(color)
            >>> hue = Color.hue(color)
            >>> print(hue)
            >>> color_bgr = Color.hue2bgr(hue)
            >>> print(color_bgr)
        """
        return reversed(cls.hue2rgb(hue))

    @classmethod
    def average(cls, color):
        """
        Averaging a color.

        Args:
            color (tuple): the color to be averaged.

        Returns:
            (tuple) averaged color.

        Examples:
            >>> color = Color.random()
            >>> print(color)
            >>> color_averaged = Color.average(color)
        """
        return int((color[0] + color[1] + color[2]) / 3)

    @classmethod
    def lightness(cls, rgb):
        """
        Calculate the grayscale value of R, G, B according to lightness method.

        Args:
            rgb (tuple): RGB values

        Returns:
            (int) grayscale value

        Examples:
            >>> color = Color.random()
            >>> print(color)
            >>> lightness = Color.lightness(color)
            >>> print(lightness)
        """
        return int((max(rgb) + min(rgb)) / 2)

    @classmethod
    def luminosity(cls, rgb):
        """
        Calculate the grayscale value of R, G, B according to luminosity method.

        Args:
            rgb (tuple): RGB values

        Returns:
            (int) grayscale value

        Examples:
            >>> color = Color.random()
            >>> print(color)
            >>> luminosity = Color.luminosity(color)
            >>> print(luminosity)
        """
        return int((0.21 * rgb[0] + 0.71 * rgb[1] + 0.07 * rgb[2]))


class ColorCurve(object):
    """
    ColorCurve is a color spline class for performing color correction.
    It can takes a Scipy Univariate spline as parameter, or an array with
    at least 4 point pairs.
    Either of these must map in a 255x255 space.  The curve can then be
    used in the applyRGBCurve, applyHSVCurve, and applyIntensityCurve functions.

    Note:
    The points should be in strictly increasing order of their first elements
    (X-coordinates)

    the only property, curve is a linear array with 256 elements from 0 to 255
    """
    curve = ''

    def __init__(self, vals):
        interval = np.linspace(0, 255, 256)
        if type(vals) == UnivariateSpline:
            self.curve = vals(interval)
        else:
            vals = np.array(vals)
            spline = UnivariateSpline(vals[:, 0], vals[:, 1], s=1)
            self.curve = np.maximum(np.minimum(spline(interval), 255), 0)


class ColorMap(object):
    """
    ColorMap takes a tuple of colors along with the start and end points
    ant it lets you map colors with a range of numbers.
    """
    color = ()
    end_color = ()
    start_map = 0
    end_map = 0
    color_distance = 0
    value_range = 0

    def __init__(self, color, start_map, end_map):
        """
        :param color: tuple of colors which need to be mapped.
        :param start_map: starting of the range of number with which we map
                          the colors.
        :param end_map: end of the range of the number with which we map
                        the colors.
        """
        self.color = np.array(color)
        if self.color.ndim == 1:  # To check if only one color was passed.
            color = ((color[0], color[1], color[2]), Color.WHITE)
            self.color = np.array(color)
        self.start_map = float(start_map)
        self.end_map = float(end_map)
        self.value_range = float(end_map - start_map)  # delta
        self.color_distance = self.value_range / float(len(self.color) - 1)

    def __getitem__(self, val):
        if val > self.end_map:
            val = self.end_map
        elif val < self.start_map:
            val = self.start_map
        value = (val - self.start_map) / self.color_distance
        alpha = float(value - int(value))
        index = int(value)
        if index == len(self.color) - 1:
            color = tuple(self.color[index])
            return int(color[0]), int(color[1]), int(color[2])
        color = tuple(self.color[index]*(1-alpha) + self.color[index+1]*alpha)

        return int(color[0]), int(color[1]), int(color[2])
