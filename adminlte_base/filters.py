import arrow
from dateutil import tz


def humanize(dt, locale='en_us', time_zone=None):
    """The filter converts the date to human readable."""
    dt = arrow.get(dt, tz.gettz(time_zone))
    return dt.humanize(locale=locale, only_distance=True)


__all__ = (
    humanize.__name__,
)
