"""
Entities used in templates.
"""

from collections import OrderedDict
from datetime import datetime
from typing import NamedTuple

from .constants import ThemeColor, FlashMessageLevel


class FlashedMessage(object):
    """A message pop-up on the page."""

    COLOR = {
        FlashMessageLevel.DEBUG: ThemeColor.SECONDARY,
        FlashMessageLevel.ERROR: ThemeColor.DANGER,
        FlashMessageLevel.WARNING: ThemeColor.WARNING,
        FlashMessageLevel.INFO: ThemeColor.INFO,
        FlashMessageLevel.MESSAGE: ThemeColor.INFO,
        FlashMessageLevel.SUCCESS: ThemeColor.SUCCESS,
    }

    ICONS = {
        FlashMessageLevel.DEBUG: 'fas fa-bug',
        FlashMessageLevel.ERROR: 'fas fa-ban',
        FlashMessageLevel.WARNING: 'fas fa-exclamation-triangle',
        FlashMessageLevel.INFO: 'fas fa-info',
        FlashMessageLevel.MESSAGE: 'fas fa-info',
        FlashMessageLevel.SUCCESS: 'fas fa-check',
    }

    def __init__(self, title, text, level=FlashMessageLevel.INFO, icon=None, color=None, message_class=''):
        self.title = title
        self.text = text
        self.level = level
        self._icon = icon
        self._color = color
        self.message_class = message_class

    @property
    def color(self):
        if self._color is None:
            self._color = self.COLOR.get(self.level)
        return self._color

    @property
    def icon(self):
        if self._icon is None:
            self._icon = self.ICONS.get(self.level)
        return self._icon


class MenuItem(object):
    """Application menu item."""

    TYPE_LINK = 'link'
    TYPE_HEADER = 'header'
    TYPE_DROPDOWN_DIVIDER = 'dropdown divider'

    def __init__(self, id_item, title, url, parent=None,
                 item_type=TYPE_LINK, icon=False, help=None, badge=None):
        """
        Arguments:
            id_item (int|str): the unique identifier of the menu item.
            title (str): item title.
            url (str): the URL that the menu item refers to.
            parent (MenuItem): link to the parent menu item.
            item_type (str): type of menu item, see MenuItem.TYPE_ *.
            icon (str): CSS classes for the icon.
            help (str): hover hint.
            badge (tuple): text label, the first element is text, the second element is style.
        """
        self._active = False
        self._children = []

        self.id = id_item
        self.title = title
        self.url = url
        self.parent = parent
        self.type = item_type
        self.icon = icon
        self.help = help
        self.badge = badge

    def add_badge(self, text, color):
        """Adds a text label to a menu item."""
        self.badge = (text, color)

    def append_child(self, child):
        """Adds a child menu item."""
        child.parent = self
        self._children.append(child)

    @property
    def children(self):
        yield from self._children

    @children.setter
    def children(self, children):
        for child in children:
            self.append_child(child)

    def has_children(self):
        """Returns true if the menu item has a submenu."""
        return bool(self._children)

    def has_parent(self):
        """Returns true if the menu item is a child."""
        return self.parent is not None

    def is_active(self):
        """Returns true if the menu item is selected, otherwise false."""
        return self._active

    def remove_child(self, child):
        # fixme: родитель и исключение
        if child in self.children:
            self._children.remove(child)

    def set_active(self, state):
        """Sets the status of a menu item as active or not."""
        self._active = bool(state)

        if self.has_parent():
            self.parent.set_active(state)


class Menu(object):
    """Application menu."""

    def __init__(self):
        self._items = OrderedDict()

    def __iter__(self):
        for id_item, item in self._items.items():
            if not item.has_parent():
                yield item

    def activate_by_path(self, path):
        """Makes active a menu item whose URL matches the one specified in the argument."""
        for item in self._items.values():
            if item.url == path:
                item.set_active(True)
                return True
        return False

    def add_item(self, item: MenuItem):
        if item.has_parent():
            item.parent.append_child(item)
        self._items[item.id] = item

    def get_item(self, id_item):
        return self._items.get(id_item)


class PageItem(object):
    """Элемент постраничной навигации."""
    def __init__(self, text, url='#', is_active=False, disabled=False, responsive=None):
        self.text = text
        self.url = url
        self.is_active = is_active
        self.disabled = disabled
        self.responsive_text = responsive

    @property
    def responsive(self):
        if not self.responsive_text:
            return self.text
        return self.responsive_text


class Collection(object):
    def __init__(self):
        self.items = []

    def __iter__(self):
        return iter(self.items)

    def add(self, item):
        self.items.append(item)

    def get_total(self):
        return len(self.items)


class Dropdown(Collection):
    """Drop-down list in the upper navbar."""

    def __init__(self, url, total_items=None):
        """
        Arguments:
            url (str): he URL of the page where you can see all the elements of the collection.
            total_items (int): the total number of elements in the storage.
        """
        super().__init__()
        self.url = url
        self.total_items = total_items

    def get_total(self):
        """
        Returns the total number of elements in the storage,
        if the value was passed in the constructor,
        or the number of elements in the collection.
        """
        if self.total_items is None:
            return super().get_total()
        return self.total_items

    def get_url(self):
        """
        Returns the URL of the page where you can see all the elements of the collection.
        """
        return self.url


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

    def __init__(self, sender, subject, url, sent_at=None, icon='fas fa-star', color=ThemeColor.SECONDARY):
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

    def __init__(self, text, sent_at=None, url='#', icon=None, color=ThemeColor.GRAY_DARK):
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
    Dropdown.__name__,
    Menu.__name__,
    MenuItem.__name__,
    Message.__name__,
    Notification.__name__,
    Task.__name__,
)
