from enum import Enum
from dotenv import dotenv_values


class Templates(Enum):
    ADD = "quickreads/create-book.html"
    BOOKS_LIST = "quickreads/books-list.html"
    BOOK_CARD = "quickreads/book-card.html"
    NEWSLETTER = "email_templates/newsletter.html"


class Employees(Enum):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )
    POSITION_CHOICES = (
        ("accountant", "Accountant"),
        ("ceo", "Chief Executive Officer (CEO)"),
        ("technical_author", "Technical Author"),
        ("software_engineer", "Software Engineer"),
        ("integration_specialist", "Integration Specialist"),
        ("pre_sales_support", "Pre-Sales Support"),
        ("sales_assistant", "Sales Assistant"),
        ("developer", "Developer"),
    )


class Urls(Enum):
    HOME_REVERSE = "index"
    BOOKS_REVERSE = "books"
    CREATE_BOOK_REVERSE = "create-book"
    LOGIN_REVERSE = "login"
    REGISTER_REVERSE = "register"
    NEWLETTER_REVERSE = "newsletter"


class Constants(Enum):
    FORM_CLASS = "input input-bordered w-full"
    NOT_AUTHENTICATED = "Please Login to Continue"
    THEME_CHOICES = (
        ("light", "light"),
        ("dark", "dark"),
        ("cupcake", "cupcake"),
        ("bumblebee", "bumblebee"),
        ("emerald", "emerald"),
        ("corporate", "corporate"),
        ("synthwave", "synthwave"),
        ("retro", "retro"),
        ("cyberpunk", "cyberpunk"),
        ("valentine", "valentine"),
        ("halloween", "halloween"),
        ("garden", "garden"),
        ("forest", "forest"),
        ("aqua", "aqua"),
        ("lofi", "lofi"),
        ("pastel", "pastel"),
        ("fantasy", "fantasy"),
        ("wireframe", "wireframe"),
        ("black", "black"),
        ("luxury", "luxury"),
        ("dracula", "dracula"),
        ("cmyk", "cmyk"),
        ("autumn", "autumn"),
        ("business", "business"),
        ("acid", "acid"),
        ("lemonade", "lemonade"),
        ("night", "night"),
        ("coffee", "coffee"),
        ("winter", "winter"),
        ("dim", "dim"),
        ("nord", "nord"),
        ("sunset", "sunset"),
    )


LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
STATIC_URL = "static/"
STATIC_PATH = "templates/static/"
STATIC_ROOT = "assets"
TEMPLATES = "templates/"
TYPE_HTML = "text/html"
NEWSLETTER = "Newsletter"


# Email Constants
class EmailConstants(Enum):
    config = dotenv_values(".env")
    NEWSLETTER = "QuickReads Newsletter Subscribed"
    HOST = config.get("EMAIL_HOST_USER")


class SuccessMessages(Enum):
    NEWSLETTER = "You Subscribed to the Newsletter"
