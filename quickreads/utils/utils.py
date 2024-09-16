from quickreads.utils.constants import Templates, TYPE_HTML, NEWSLETTER
from quickreads.utils.firebase_config import storage, database
from dotenv import dotenv_values
from django.http import HttpResponseNotFound
from django.core.mail import send_mass_mail, EmailMultiAlternatives
from django.template.loader import render_to_string


config = dotenv_values(".env")
FILEBASE_IMAGE_URL = config.get("FILEBASE_IMAGE_URL")


def serialize_form_data(form_data, cover, book):
    """
    serialize formdata in required format

    :param form_data: dict
    """
    return {
        "title": form_data.get("title"),
        "description": form_data.get("description"),
        "authors": form_data.get("authors"),
        "published": form_data.get("published"),
        "cover": form_data.get("cover"),
        "book": form_data.get("book"),
    }


def upload_image_to_firebase_storage_and_format_url(key, file):
    """
    upload image to firebase storage and format url

    :param key:
    :param file:
    """
    url = storage.child("image_{key}".format(key=key)).put(file)
    return FILEBASE_IMAGE_URL.format(token=url.get("downloadTokens"))  # type: ignore


def create_database_snapshot_for_employees(key, data):
    """
    create database snapshot in firebase and return response

    :param key:
    :param data:
    """
    return (
        database.child("Books")
        .child(key)
        .set(data, json_kwargs={"indent": 4, "sort_keys": True, "default": str})
    )


def get_books_data_snapshot():
    """
    get all employees data snapshot
    """
    data = database.child("Books").get().val()
    if data is not None:
        return format_employees_snapshot_in_required_format(data)
    return HttpResponseNotFound("Books not found")


def format_employees_snapshot_in_required_format(data):
    """
    _summary_

    :param data:
    """
    books_list = []
    for key, value in data.items():
        books_list.append(value)
    return books_list


def send_mails(subject, sender, receiver, body, attachment):
    """
    send emails

    :param subject: str
    :param sender: str
    :param receiver: list
    :param body: str
    :param attachment:
    """
    mail = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email=sender,
        to=receiver,
    )
    html_message = render_to_string(Templates.NEWSLETTER.value)
    mail.attach_alternative(html_message, TYPE_HTML)
    if attachment:
        mail.attach("image.jpeg", attachment.read())
    mail.send()


def push_email_newsletter_database(email: str):
    """
    add email in newsletter database

    :param email: str
    """
    database.child(NEWSLETTER).push(email)
