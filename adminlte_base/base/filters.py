"""
Provides ready-made implementations for filters used in templates.
"""

from string import Template

import arrow
from dateutil import tz

from .constants import ThemeColor


def humanize(dt, locale='en_us', time_zone=None):
    """The filter converts the date to human readable."""
    dt = arrow.get(dt, tz.gettz(time_zone))
    return dt.humanize(locale=locale, only_distance=True)


def navbar_skin(color):
    """Returns a collection of classes to style the navigation bar."""
    if color:
        light = {ThemeColor.LIGHT, ThemeColor.WARNING, ThemeColor.WHITE, ThemeColor.ORANGE}
        style = 'light' if color in light else f'dark'
        return f'navbar-{style} navbar-{color}'
    return ''


def sidebar_skin(color, light=False):
    """"""
    if color:
        style = 'light' if light else f'dark'
        return f'sidebar-{style}-{color}'
    return ''


def if_true(value, replace_with=None):
    if not value:
        return ''

    if replace_with is None:
        return value

    return Template(replace_with).safe_substitute(value=value)


__all__ = (
    humanize.__name__,
    navbar_skin.__name__,
    sidebar_skin.__name__,
    if_true.__name__,
)
