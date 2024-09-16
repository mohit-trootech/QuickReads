from enum import Enum
from django.utils.translation import gettext_noop as _


class Templates(Enum):
    SIGN_IN = "accounts/login.html"
    REGISTER = "accounts/register.html"
    PROFILE = "accounts/profile.html"


class Urls(Enum):
    LOGIN_REVERSE = "login"
    LOGOUT_REVERSE = "logout"
    REGISTER_REVERSE = "register"
    HOME_REVERSE = "index"
    UPDATE_REVERSE = "profile"


class Forms(Enum):
    FORM_CLASS = "input input-bordered"
    ACCOUNTS_FORM_NAME_PLACEHOLDER = _("Please Enter Login Name")
    ACCOUNTS_FORM_NAME_HELP_TEXT = _("Please Enter Login Name")
    ACCOUNTS_FORM_EMAIL_PLACEHOLDER = _("Please Enter Login Email")
    ACCOUNTS_FORM_EMAIL_HELP_TEXT = _("Please Enter Login Email")
    ACCOUNTS_FORM_PASSWORD_PLACEHOLDER = _("Please Enter Login Password")
    ACCOUNTS_FORM_PASSWORD_HELP_TEXT = _("Password is Required")
    ACCOUNTS_FORM_AGE_PLACEHOLDER = _("Please Enter Age")
    ACCOUNTS_FORM_PROFILE_PLACEHOLDER = _("Choose Profile Picture")
    ACCOUNTS_FORM_PHONE_PLACEHOLDER = _("Enter Phone Number")
    ACCOUNTS_FORM_ADDRESS_PLACEHOLDER = _("Please Enter Address")


class SuccessMessages(Enum):
    LOGIN = "Logged in Successfully"
    SIGNUP = "User Created Successfully"
    LOGOUT = "Logged out Successfully"
    UPDATE = "Profile Updated Successfully"


class ErrorMessages(Enum):
    LOGIN = "Failed to Login Try Again with Correct Credentials"
    PASSWORD_NOT_MATCH = "Please Check Passwords are Not Matching"
    UNIQUE_USER_ERROR = "User with Same Username or Password Already Exists"
    UNKNOWN_ERROR = "Other error occurred: {err}"


class Key(Enum):
    PROFILE = "profile"
