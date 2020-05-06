from abc import ABCMeta, abstractmethod
import pkg_resources # import importlib.resources


from .constants import *
from .data_types import *
from .exceptions import *
from .menu import *


def get_template_path():
    """Returns the path to the template directory."""
    return pkg_resources.resource_filename(__name__, 'templates')


def get_static_path():
    """Returns the path to the asset directory."""
    return pkg_resources.resource_filename(__name__, 'static')


class AbstractManager(metaclass=ABCMeta):
    def __init__(self):
        self._menu_callback = None

    @abstractmethod
    def create_url(self, endpoint, endpoint_args=None, endpoint_kwargs=None):
        """Creates and returns a URL using the address generation system of a specific framework."""

    def get_menu(self, program_name, active_path=None):
        """Creates and returns a menu with the specified program name."""
        if self._menu_callback is None:
            raise exceptions.Error('Missing menu_loader.')

        data = self._menu_callback(program_name)

        if data is None:
            raise exceptions.MenuNotFound(program_name)

        menu = Menu()

        for i in data.get_items():
            menu.add_item(MenuItem(
                id_item=i.get_id(),
                title=i.get_title(),
                url=i.get_url() or self.create_url(
                    i.get_endpoint(), i.get_endpoint_args(), i.get_endpoint_kwargs()
                ),
                parent=menu.get_item(i.get_parent_id()),
                item_type=i.get_type(),
                icon=i.get_icon(),
                help=i.get_hint()
            ))

        if active_path is not None:
            menu.activate_by_path(active_path)

        return menu

    def menu_loader(self, callback):
        """
        This sets the callback for loading a menu from the database or other source.
        The function you set should take a menu ID or program name.

        Arguments:
            callback (callable): the callback for retrieving a menu object.

        Returns:
            a menu object, or ``None`` if the menu does not exist.
        """
        self._menu_callback = callback
        return callback

    @abstractmethod
    def static(self, filename):
        """Generates a URL to the given asset."""
