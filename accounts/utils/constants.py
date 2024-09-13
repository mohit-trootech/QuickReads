from enum import Enum
from django.utils.translation import gettext_noop as _


class Templates(Enum):
    SIGN_IN = "accounts/login.html"
    REGISTER = "accounts/register.html"


class Urls(Enum):
    LOGIN_REVERSE = "login"
    LOGOUT_REVERSE = "logout"
    REGISTER_REVERSE = "register"
    HOME_REVERSE = "index"


class Forms(Enum):
    FORM_CLASS = "input input-bordered w-full max-w-xs"
    ACCOUNTS_FORM_NAME_PLACEHOLDER = _("Please Enter Login Name")
    ACCOUNTS_FORM_NAME_HELP_TEXT = _("Please Enter Login Name")
    ACCOUNTS_FORM_EMAIL_PLACEHOLDER = _("Please Enter Login Email")
    ACCOUNTS_FORM_EMAIL_HELP_TEXT = _("Please Enter Login Email")
    ACCOUNTS_FORM_PASSWORD_PLACEHOLDER = _("Please Enter Login Password")
    ACCOUNTS_FORM_PASSWORD_HELP_TEXT = _("Password is Required")


class SuccessMessages(Enum):
    LOGIN = "Logged in Successfully"
    SIGNUP = "User Created Successfully"
    LOGOUT = "Logged out Successfully"


class ErrorMessages(Enum):
    LOGIN = "Failed to Login Try Again with Correct Credentials"
    PASSWORD_NOT_MATCH = "Please Check Passwords are Not Matching"
    UNIQUE_USER_ERROR = "User with Same Username or Password Already Exists"


# USER_UPDATE_PLACEHOLDER = {
#     "first_name": _("Please Enter First Name"),
#     "last_name": _("Please Enter Last Name"),
#     "email": _("Please Enter Email"),
# }

# USER_CREATE_PLACEHOLDER = {
#     "first_name": _("Please Choose First Name"),
#     "last_name": _("Please Choose Last Name"),
#     "email": _("Please Choose Email"),
#     "username": _("Please Choose Username"),
# }

# CRUD_USER_CREATE_PLACEHOLDER = {
#     "title": _("Please Choose Full Name"),
#     "age": _("Please Enter Age"),
# }


# USER_UPDATE_HELP_TEXT = {
#     "first_name": _("First Name is Required Field"),
#     "last_name": _("Last Name is Required Field"),
#     "email": _("Email is Required Field"),
# }
# USER_CREATE_HELP_TEXT = {
#     "email": _("Please Enter Correct Email Format"),
#     "username": _("Username is Required Field"),
# }

# # URLS
# PROFILE_UPDATE_SUCCESS_URL = "/profile/{pk}"

# # Error
# LOGIN_ERROR = _("Failed to Login Try Again with Correct Credentials")
# PASSWORD_NOT_MATCH = _("Please Check Passwords are Not Matching")
# UNIQUE_USER_ERROR = _("User with Same Username or Password Already Exists")

# # Success
# LOGIN_SUCCESS = _("Logged in Successfully")
# SIGNUP_SUCCESS = _("User Registered Successfully")
# LOGOUT_SUCCESS = _("User Logged Out Successfully")

# # Cache Variables
# CACHE_TABLE_NAME = "cache_table"

# # Context Object Names
# USERS = "users"
