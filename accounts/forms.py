from django.forms import (
    Form,
    EmailField,
    EmailInput,
    CharField,
    PasswordInput,
    TextInput,
    NumberInput,
    IntegerField,
    ImageField,
    ClearableFileInput,
)
from accounts.utils.constants import Forms
from phonenumber_field.formfields import PhoneNumberField


class UserLoginForm(Form):
    email = EmailField(
        required=True,
        widget=EmailInput(
            attrs={
                "class": Forms.FORM_CLASS.value,
                "placeholder": Forms.ACCOUNTS_FORM_EMAIL_PLACEHOLDER.value,
                "autocomplete": "username",
                "required": True,
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
                "required": True,
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
                "required": True,
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
                "required": True,
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
                "required": True,
            }
        ),
        help_text=Forms.ACCOUNTS_FORM_PASSWORD_HELP_TEXT.value,
    )


class UserUpdateForm(Form):
    profile = ImageField(
        required=False,
        widget=ClearableFileInput(
            attrs={
                "class": "file-input file-input-bordered w-full",
                "placeholder": Forms.ACCOUNTS_FORM_PROFILE_PLACEHOLDER.value,
                "accept": "image/*",
            },
        ),
    )
    name = CharField(
        required=False,
        widget=TextInput(
            attrs={
                "class": Forms.FORM_CLASS.value,
                "placeholder": Forms.ACCOUNTS_FORM_NAME_PLACEHOLDER.value,
                "autocomplete": "username",
            },
        ),
        help_text=Forms.ACCOUNTS_FORM_NAME_HELP_TEXT.value,
    )
    age = IntegerField(
        required=False,
        widget=NumberInput(
            attrs={
                "class": Forms.FORM_CLASS.value,
                "placeholder": Forms.ACCOUNTS_FORM_AGE_PLACEHOLDER.value,
                "autocomplete": "age",
                "max": 100,
                "min": 18,
            }
        ),
    )
    phone = PhoneNumberField(
        region="IN",
        required=False,
        widget=NumberInput(
            attrs={
                "class": Forms.FORM_CLASS.value,
                "placeholder": Forms.ACCOUNTS_FORM_PHONE_PLACEHOLDER.value,
            }
        ),
    )
    address = CharField(
        required=False,
        widget=TextInput(
            attrs={
                "class": Forms.FORM_CLASS.value,
                "placeholder": Forms.ACCOUNTS_FORM_ADDRESS_PLACEHOLDER.value,
            }
        ),
    )
