from django.forms import (
    Form,
    CharField,
    EmailField,
    EmailInput,
    PasswordInput,
    TextInput,
)
from accounts.utils.constants import Forms


class UserLoginForm(Form):
    email = EmailField(
        required=True,
        widget=EmailInput(
            attrs={
                "class": Forms.FORM_CLASS.value,
                "placeholder": Forms.ACCOUNTS_FORM_EMAIL_PLACEHOLDER.value,
                "autocomplete": "username",
                "required": "True",
            }
        ),
        help_text=Forms.ACCOUNTS_FORM_EMAIL_HELP_TEXT.value,
    )
    password = CharField(
        required=True,
        widget=PasswordInput(
            attrs={
                "class": Forms.FORM_CLASS.value,
                "placeholder": Forms.ACCOUNTS_FORM_PASSWORD_PLACEHOLDER.value,
                "autocomplete": "current-password",
                "required": "True",
            }
        ),
        help_text=Forms.ACCOUNTS_FORM_PASSWORD_HELP_TEXT.value,
    )


class UserRegisterForm(Form):
    name = CharField(
        required=True,
        widget=TextInput(
            attrs={
                "class": Forms.FORM_CLASS.value,
                "placeholder": Forms.ACCOUNTS_FORM_NAME_PLACEHOLDER.value,
                "autocomplete": "username",
                "required": "True",
            }
        ),
        help_text=Forms.ACCOUNTS_FORM_NAME_HELP_TEXT.value,
    )
    email = EmailField(
        required=True,
        widget=EmailInput(
            attrs={
                "class": Forms.FORM_CLASS.value,
                "placeholder": Forms.ACCOUNTS_FORM_EMAIL_PLACEHOLDER.value,
                "autocomplete": "email",
                "required": "True",
            }
        ),
        help_text=Forms.ACCOUNTS_FORM_EMAIL_HELP_TEXT.value,
    )
    password = CharField(
        required=True,
        widget=PasswordInput(
            attrs={
                "class": Forms.FORM_CLASS.value,
                "placeholder": Forms.ACCOUNTS_FORM_PASSWORD_PLACEHOLDER.value,
                "autocomplete": "current-password",
                "required": "True",
            }
        ),
        help_text=Forms.ACCOUNTS_FORM_PASSWORD_HELP_TEXT.value,
    )
