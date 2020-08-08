from abc import ABCMeta, abstractmethod


__all__ = (
    'AbstractQuery', 'AbstractMenuFormFactory', 'AbstractMenuModelFactory',
)


class AbstractMenuFormFactory(metaclass=ABCMeta):
    """An abstract factory that creates HTML forms for manipulating menus."""

    @abstractmethod
    def create_link_form(self, obj=None):
        """Returns an instance of the HTML form for editing menu links."""

    @abstractmethod
    def create_menu_form(self, obj=None):
        """Returns an instance of the HTML form for editing the menu."""

    @abstractmethod
    def create_item_form(self, obj=None):
        """Returns an instance of the HTML form for editing a menu item"""


class AbstractMenuModelFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_link(self, **attributes):
        """Returns a new instance of the link to be stored in the database."""

    @abstractmethod
    def create_link_query(self):
        """Returns a new instance of the menu link entities query object."""

    @abstractmethod
    def create_menu(self, **attributes):
        """Returns a new instance of the menu entity to be stored in the database."""

    @abstractmethod
    def create_menu_query(self):
        """Returns a new instance of the menu entities query object."""

    @abstractmethod
    def create_item(self, **attributes):
        """Returns a new instance of the entity menu item to be stored in the database."""

    @abstractmethod
    def create_item_query(self):
        """Returns a new instance of the menu item entities query object."""


class AbstractQuery(metaclass=ABCMeta):
    """Abstract database query."""

    @abstractmethod
    def get(self, pk):
        """Returns an entity from the database by primary key."""

    @abstractmethod
    def all(self):
        """Returns all entities from the database."""
