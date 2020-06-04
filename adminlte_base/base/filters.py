"""
Provides ready-made implementations for filters used in templates.
"""

import arrow
from dateutil import tz

from .constants import ThemeColor


def humanize(dt, locale='en_us', time_zone=None):
    """The filter converts the date to human readable."""
    dt = arrow.get(dt, tz.gettz(time_zone))
    return dt.humanize(locale=locale, only_distance=True)


def navbar_skin(color):
    """Returns a collection of classes to style the navigation bar."""
    light = {ThemeColor.LIGHT, ThemeColor.WARNING, ThemeColor.WHITE, ThemeColor.ORANGE}
    style = 'light' if color in light else f'dark'
    return f'navbar-{style} navbar-{color}'


def sidebar_skin(color, light=False):
    """"""
    style = 'light' if light else f'dark'
    return f'sidebar-{style}-{color}'


__all__ = (
    humanize.__name__,
    navbar_skin.__name__,
sidebar_skin.__name__,
)
