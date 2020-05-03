from datetime import datetime

from .constants import ThemeColor


class Collection(object):
    def __init__(self):
        self.items = []

    def __iter__(self):
        return iter(self.items)

    def add(self, item):
        self.items.append(item)

    @property
    def total(self):
        return len(self.items)


class DropdownItem(object):
    """Drop-down list item."""

    __slots__ = ('url', 'icon', 'color')

    def __init__(self, icon=None, color=None):
        """
        Arguments:
            icon (str): CSS classes for the icon.
            color (str): the color code from the theme.
        """
        self.icon = icon
        self.color = color


class Message(DropdownItem):
    """Messages sent to the user."""

    __slots__ = ('sender', 'subject', 'sent_at')

    def __init__(self, sender, subject, url, sent_at=None, icon='fas fa-star', color=ThemeColor.MUTED):
        """
        Arguments:
            sender (mixed): the one who sent the message.
            subject (str): message subject.
            url (str): URL to read the message.
            sent_at (datetime): message sending time.
        """
        super().__init__(icon, color)
        self.sender = sender
        self.subject = subject
        self.url = url
        self.sent_at = sent_at or datetime.now()


class Notification(DropdownItem):
    """Notifications sent to the user."""

    __slots__ = ('text', 'sent_at', 'url')

    def __init__(self, text, sent_at=None, url='#', icon=None, color=ThemeColor.DARK):
        """
        Arguments:
            text (str): notification text.
            sent_at (datetime): notification sending time.
            url (str): URL to read the notification.
        """
        super().__init__(icon, color)
        self.text = text
        self.sent_at = sent_at or datetime.now()
        self.url = url


class Task(DropdownItem):
    """Task in progress."""

    __slots__ = ('title', 'progress', 'url')

    def __init__(self, title, progress, url, icon=None, color=None):
        """
        Arguments:
            title (str): the title of the task to be performed.
            progress (float): progress of the task in percent.
            url (str): URL to show the task.
        """
        super().__init__(icon, color)
        self.title = title
        self.progress = progress
        self.url = url


__all__ = (
    Collection.__name__,
    Message.__name__,
    Notification.__name__,
    Task.__name__,
)
