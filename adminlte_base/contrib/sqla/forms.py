from wtforms import Form
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import InputRequired


__all__ = ('menu_item_form_factory',)


def menu_item_form_factory(query_factory, form_class=Form):
    class MenuItemForm(form_class):
        parent = QuerySelectField(
            query_factory=query_factory,
            get_label='title',
            allow_blank=True,
            validators=[
            ]
        )
        link = QuerySelectField(
            query_factory=query_factory,
            get_label='title',
            validators=[
                InputRequired(),
            ]
        )
        before = QuerySelectField(
            query_factory=query_factory,
            get_label='title',
            allow_blank=True,
            validators=[
            ]
        )
    return MenuItemForm
