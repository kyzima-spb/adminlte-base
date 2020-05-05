from datetime import datetime

from .constants import ThemeColor


class MenuItemmixin(object):
    """Mixin for the database model, which describes the menu item."""

    def get_endpoint(self):
        """Returns the name of the entry point / route."""
        return self.endpoint

    def get_endpoint_args(self):
        """Returns the nameless arguments to the route."""
        return self.endpoint_args.split()

    def get_endpoint_kwargs(self):
        """Returns the named arguments to the route."""
        return dict(p.split('=') for p in self.endpoint_kwargs.splitlines())

    def get_hint(self):
        """Returns a hint to the user."""
        return self.help

    def get_icon(self):
        """Returns the css class of the icon."""
        return self.icon

    def get_id(self):
        """Returns a unique identifier for a menu item."""
        return self.id

    def get_parent_id(self):
        """Returns the unique identifier of the parent menu item."""
        return self.parent and self.parent.get_id()

    def get_title(self):
        """Returns the title of a menu item."""
        return self.title

    def get_type(self):
        """Returns the type of menu item."""
        return self.type

    def get_url(self):
        """Returns the URL that this menu item refers to."""
        return self.url


class MenuMixin(object):
    """Mixin for the database model that describes the menu."""

    def get_items(self):
        """Returns menu items strictly sorted in ascending order by parent and position."""
        return self.items

    def get_program_name(self):
        """Returns a unique menu name to display on the page."""
        return self.program_name

    def get_title(self):
        """Returns the title of the menu."""
        return self.title


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
    MenuItemmixin.__name__,
    MenuMixin.__name__,
    Collection.__name__,
    Message.__name__,
    Notification.__name__,
    Task.__name__,
)
