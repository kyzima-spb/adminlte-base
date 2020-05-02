from collections import OrderedDict


class MenuItem(object):
    """Application menu item."""

    TYPE_LINK = 'link'
    TYPE_HEADER = 'header'

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

    def add_item(self, item: MenuItem):
        if item.has_parent():
            item.parent.append_child(item)
        self._items[item.id] = item

    def get_item(self, id_item):
        return self._items.get(id_item)
