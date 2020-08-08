from wtforms import Form
from wtforms.fields import (
    StringField, PasswordField, BooleanField, HiddenField, FloatField,
    FieldList, FormField, TextAreaField, RadioField
)
import wtforms.validators as vd

from ..data_types import MenuItem


__all__ = (
    'MenuLinkForm', 'MenuForm',
    'LoginForm', 'ResetPasswordForm',
)


def trim(s):
    return s.strip() if s is not None else None


class MenuLinkForm(Form):
    TYPES = (
        (MenuItem.TYPE_LINK, MenuItem.TYPE_LINK.title()),
        (MenuItem.TYPE_HEADER, MenuItem.TYPE_HEADER.title()),
    )
    type = RadioField('Link type', choices=TYPES, default=MenuItem.TYPE_LINK)
    title = StringField(
        label='Title',
        filters=[trim],
        validators=[vd.InputRequired(), vd.Length(max=500)]
    )
    icon = StringField(
        label='Icon',
        filters=[trim],
        validators=[vd.Optional(), vd.Length(max=50)],
        description='CSS style of the icon from any connected library.'
    )
    help = StringField(
        label='Hint',
        filters=[trim],
        validators=[vd.Optional(), vd.Length(max=255)],
        description='The text to be displayed on hover.'
    )
    endpoint = StringField(
        label='Endpoint name',
        filters=[trim],
        validators=[vd.Optional(), vd.Length(max=255)],
        description='The absolute name of the endpoint.'
    )
    endpoint_args = TextAreaField(
        label='List of positional parameters for the endpoint',
        filters=[trim],
        description='Each value on a new line.'
    )
    endpoint_kwargs = TextAreaField(
        label='List of named parameters for the endpoint',
        filters=[trim],
        description='Each value on a new line, the name from the value is separated by an equal sign.'
    )
    url = StringField(
        label='URL',
        filters=[trim, lambda v: v and v.strip('#')],
        validators=[vd.Optional(), vd.URL(message='Only absolute URLs are allowed.')],
        description='Only absolute URLs are allowed.'
    )

    def _validate(self):
        if self.type == MenuItem.TYPE_LINK and self.endpoint.data and self.url.data:
            raise ValueError('It is required to set the value of one of the fields: %(fieldnames)s.' % dict(
                fieldnames=''.join(['endpoint', 'url'])
            ))

    def validate_endpoint(self, field):
        self._validate()

    def validate_url(self, field):
        self._validate()


class MenuForm(Form):
    title = StringField('Title', filters=[trim], validators=[
        vd.InputRequired(), vd.Length(max=500),
    ])


class LoginForm(Form):
    """Login form."""
    email = StringField('E-Mail', filters=[trim], validators=[
        vd.InputRequired(),
        vd.Email()
    ], render_kw={'data-icon': 'fas fa-envelope'})
    password = PasswordField('Password', validators=[
        vd.InputRequired()
    ], render_kw={'data-icon': 'fas fa-lock'})
    remember_me = BooleanField('Remember Me', validators=[
        vd.Optional()
    ])


class ResetPasswordForm(Form):
    """Password reset form."""
    email = StringField('E-Mail', filters=[trim], validators=[
        vd.InputRequired(),
        vd.Email()
    ], render_kw={'data-icon': 'fas fa-envelope'})
