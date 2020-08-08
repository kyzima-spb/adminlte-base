from adminlte_base.data_types import MenuItem
from adminlte_base import mixins
from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr


__all__ = (
    'MenuLinkMixin', 'MenuMixin', 'MenuItemMixin',
    'create_entity_menu', 'create_entity_menu_item', 'create_entity_menu_link',
)


class ActionMixin(object):
    def delete(self):
        self.session.delete(self)
        self.session.commit()

    def save(self):
        self.session.add(self)
        self.session.commit()


class MenuLinkMixin(ActionMixin, mixins.MenuLinkMixin):
    __tablename__ = 'menu_link'

    id = Column(Integer, primary_key=True)
    type = Column(String(20), default=MenuItem.TYPE_LINK, nullable=False)
    title = Column(String(500), nullable=False)
    endpoint = Column(String(255), default='', nullable=False)
    endpoint_args = Column(Text, default='', nullable=False)
    endpoint_kwargs = Column(Text, default='', nullable=False)
    url = Column(Text, default='#', nullable=False)
    icon = Column(String(50), default='', nullable=False)
    help = Column(String(500), default='', nullable=False)


class MenuMixin(ActionMixin, mixins.MenuMixin):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    title = Column(String(500), nullable=False)

    @declared_attr
    def items(cls):
        return relationship('MenuItem', backref='menu')


class MenuItemMixin(ActionMixin, mixins.MenuItemMixin):
    __tablename__ = 'menu_item'

    @declared_attr
    def menu_id(cls):
        return Column(
            ForeignKey('menu.id', onupdate='CASCADE', ondelete='RESTRICT'), primary_key=True
        )

    @declared_attr
    def link_id(cls):
        return Column(
            ForeignKey('menu_link.id', onupdate='CASCADE', ondelete='RESTRICT'), primary_key=True
        )

    @declared_attr
    def parent_id(cls):
        return Column(ForeignKey('menu_link.id', onupdate='CASCADE', ondelete='RESTRICT'))

    @declared_attr
    def before_id(cls):
        return Column(ForeignKey('menu_link.id', onupdate='CASCADE', ondelete='RESTRICT'))

    @property
    def pos(self):
        return self.before_id or 0

    @declared_attr
    def link(cls):
        return relationship('MenuLink', foreign_keys=[cls.menu_id, cls.link_id], lazy='joined')

    @declared_attr
    def parent(cls):
        return relationship('MenuLink', foreign_keys=cls.parent_id, lazy='joined', backref='children')

    @declared_attr
    def before(cls):
        return relationship('MenuLink', foreign_keys=cls.before_id, lazy='joined')


def create_entity_menu(db):
    return type('Menu', (db.Model, MenuMixin), {})


def create_entity_menu_item(db):
    return type('MenuItem', (db.Model, MenuItemMixin), {})


def create_entity_menu_link(db):
    return type('MenuLink', (db.Model, MenuLinkMixin), {})
