from wtforms import Form
from wtforms.fields import (
    StringField, PasswordField, BooleanField, HiddenField, FloatField,
    FieldList, FormField, TextAreaField, RadioField
)
from wtforms import validators


class LoginForm(Form):
    """Login form."""
    email = StringField('E-Mail', validators=[
        validators.InputRequired(),
        validators.Email()
    ], render_kw={'data-icon': 'fas fa-envelope'})
    password = PasswordField('Password', validators=[
        validators.InputRequired()
    ], render_kw={'data-icon': 'fas fa-lock'})


class ResetPasswordForm(Form):
    """Password reset form."""
    email = StringField('E-Mail', validators=[
        validators.InputRequired(),
        validators.Email()
    ], render_kw={'data-icon': 'fas fa-envelope'})
