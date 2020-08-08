from adminlte_base.core import AbstractQuery, AbstractMenuModelFactory

from .forms import *
from .mixins import *


class Query(AbstractQuery):
    def __init__(self, session, model_class):
        self.session = session
        self.model_class = model_class

    def get(self, pk):
        return self.session.query(self.model_class).get(pk)

    def all(self):
        return self.session.query(self.model_class).all()


class MenuModelFactory(AbstractMenuModelFactory):
    def __init__(self, session, link_model, menu_model, item_model):
        self.session = session

        self.link_model = link_model
        self.menu_model = menu_model
        self.item_model = item_model

        self.link_model.session = session
        self.menu_model.session = session
        self.item_model.session = session

    def _create(self, model_class, attributes):
        return model_class(**attributes)

    def _create_query(self, model_class):
        return Query(self.session, model_class)

    def create_link(self, **attributes):
        return self._create(self.link_model, attributes)

    def create_link_query(self):
        return self._create_query(self.link_model)

    def create_menu(self, **attributes):
        return self._create(self.menu_model, attributes)

    def create_menu_query(self):
        return self._create_query(self.menu_model)

    def create_item(self, **attributes):
        return self._create(self.item_model, attributes)

    def create_item_query(self):
        return self._create_query(self.item_model)
