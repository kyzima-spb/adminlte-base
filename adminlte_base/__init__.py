"""
A basic package to simplify the integration of AdminLTE with other frameworks.
"""

from abc import ABCMeta, abstractmethod

from .constants import *
from .data_types import *
from .decorators import *
from .exceptions import *
from .mixins import *


class MenuLoader(metaclass=ABCMeta):
    __slots__ = ('manager',)

    def __init__(self, manager):
        self.manager = manager

    def _create(self, data, active_path=None):
        """Creates and returns a menu object."""
        menu = Menu()
        items = sorted(
            data.get_items(),
            key=lambda v: (v.get_parent_id() or 0, v.get_pos(), v.get_id())
        )

        for i in items:
            menu.add_item(MenuItem(
                id_item=i.get_id(),
                title=i.get_title(),
                url=i.get_url() or self.manager.create_url(
                    i.get_endpoint(), *i.get_endpoint_args(), **i.get_endpoint_kwargs()
                ),
                parent=menu.get_item(i.get_parent_id()),
                item_type=i.get_type(),
                icon=i.get_icon(),
                help=i.get_hint()
            ))

        if active_path is not None:
            menu.activate_by_path(active_path)

        return menu

    def get(self, program_name, active_path=None):
        """Creates and returns a menu with the specified program name."""
        data = self.load(program_name)

        if data is None:
            raise exceptions.MenuNotFound(program_name)

        return self._create(data, active_path)

    @abstractmethod
    def load(self, program_name):
        """Returns data for building a menu from an external source."""

    def navbar_menu(self, active_path=None):
        """Creates and returns a navbar menu."""

    def sidebar_menu(self, active_path=None):
        """Creates and returns a sidebar menu."""


class AbstractManager(metaclass=ABCMeta):
    __slots__ = (
        '_available_languages_callback',
        '_home_page_callback',
        '_locale_callback',
        '_menu_loader',
        '_messages_callback',
        '_notifications_callback',
        '_tasks_callback',
        '_user_callback',
        'home_page',
    )

    def __init__(self):
        self._available_languages_callback = None
        self._home_page_callback = None
        self._locale_callback = None
        self._menu_loader = None
        self._messages_callback = None
        self._notifications_callback = None
        self._tasks_callback = None
        self._user_callback = None
        self.home_page = None

    def available_languages_loader(self, callback):
        """
        This sets the callback for loading available languages.

        Arguments:
            callback (callable): callback to get available languages.

        Returns:
            a menu object, or ``None`` if the menu does not exist.
        """
        self._available_languages_callback = callback
        return callback

    @return_namedtuple('HomeUrl', 'url', 'title')
    def get_home_page(self):
        """Returns a link to the home page as a named tuple with url and title fields."""
        if self._home_page_callback is not None:
            return self._home_page_callback()

        if self.home_page is None:
            self.home_page = ('/', 'Home')

        return self.home_page

    @abstractmethod
    def create_url(self, endpoint, *endpoint_args, **endpoint_kwargs):
        """Creates and returns a URL using the address generation system of a specific framework."""

    @property
    def current_locale(self):
        """Returns the current language code for current locale if `locale_getter` is set."""
        if self._locale_callback is not None:
            return self._locale_callback()

    def current_locale_getter(self, callback):
        """
        This sets a callback function for current locale selection.

        The default behaves as if a function was registered that returns `None` all the time.

        Arguments:
            callback (callable): the callback to get the current locale.
        """
        self._locale_callback = callback
        return callback

    def get_available_languages(self, context=None, as_dict=False):
        """Normalizes and returns a dictionary with a list of available languages."""
        if self._available_languages_callback is None:
            raise exceptions.Error('Missing available_languages_loader.')

        if context is None:
            languages = self._available_languages_callback()
        else:
            languages = self._available_languages_callback(context)

        if isinstance(languages, dict):
            languages = languages.items()

        if as_dict:
            return {locale: name for locale, name in languages}

        return languages

    def get_flash_messages(self):
        """Creates and returns all pop-up messages by category."""
        raise NotImplementedError

    def get_incoming_messages(self, context=None):
        """Creates and returns a drop-down list of incoming messages."""
        if self._messages_callback is None:
            raise exceptions.Error('Missing messages_loader.')

        if context is None:
            messages = self._messages_callback()
        else:
            messages = self._messages_callback(context)

        if not isinstance(messages, Dropdown):
            raise exceptions.Error(f'{type(messages).__name__} unsupported return type for messages_loader; Dropdown required.')

        return messages

    def get_notifications(self, context=None):
        """Creates and returns a drop-down list of notifications."""
        if self._notifications_callback is None:
            raise exceptions.Error('Missing notifications_loader.')

        if context is None:
            notifications = self._notifications_callback()
        else:
            notifications = self._notifications_callback(context)

        if not isinstance(notifications, Dropdown):
            raise exceptions.Error(f'{type(notifications).__name__} unsupported return type for notifications_loader; Dropdown required.')

        return notifications

    def get_tasks(self, context=None):
        """Creates and returns a drop-down list of assigned or executable tasks."""
        if self._tasks_callback is None:
            raise exceptions.Error('Missing tasks_loader.')

        if context is None:
            tasks = self._tasks_callback()
        else:
            tasks = self._tasks_callback(context)

        if not isinstance(tasks, Dropdown):
            raise exceptions.Error(
                f'{type(tasks).__name__} unsupported return type for tasks_loader; Dropdown required.')

        return tasks

    def home_page_getter(self, callback):
        """
        This sets a callback to get the home page.

        Arguments:
            callback (callable): callback to get the home page.
        """
        self._home_page_callback = callback
        return callback

    @property
    def menu(self):
        """The loader for retrieving a menu object."""
        if self._menu_loader is None:
            raise exceptions.Error('Missing menu_loader.')
        return self._menu_loader(self)

    def menu_loader(self, loader: MenuLoader):
        """
        This sets the callback for loading a menu from the database or other source.
        The function you set should take a menu ID or program name.

        Arguments:
            loader (MenuLoader): the loader for retrieving a menu object.
        """
        self._menu_loader = loader
        return loader

    def messages_loader(self, callback):
        """
        This sets the callback for loading a messages from the database or other source.

        Arguments:
            callback (callable): callback to receive incoming messages.
        """
        self._messages_callback = callback
        return callback

    def notifications_loader(self, callback):
        """
        This sets the callback for loading a notifications from the database or other source.

        Arguments:
            callback (callable): callback to receive notifications.
        """
        self._notifications_callback = callback
        return callback

    def tasks_loader(self, callback):
        """
        This sets the callback for loading a tasks from the database or other source.

        Arguments:
            callback (callable): callback to receive tasks.
        """
        self._tasks_callback = callback
        return callback

    def static(self, filename):
        """Generates a URL to the given asset."""
        raise NotImplementedError

    @property
    def user(self):
        """Returns the current user if user_getter is set, otherwise returns None."""
        if self._user_callback is None:
            return None

        return User(*self._user_callback())

    def user_getter(self, callback):
        """
        This sets a callback to get the original user object.

        Callback should return a user object and, optionally,
        matching the properties of the original object with the properties of the facade.

        Arguments:
            callback (callable): callback to get the original user object.
        """
        self._user_callback = callback
        return callback
