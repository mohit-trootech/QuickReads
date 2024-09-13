from quickreads.utils.firebase_config import storage, database
from dotenv import dotenv_values
from django.http import HttpResponseNotFound

config = dotenv_values(".env")
FILEBASE_IMAGE_URL = config.get("FILEBASE_IMAGE_URL")


def serialize_form_data(form_data, file_url):
    """
    serialize formdata in required format

    :param form_data: dict
    """
    return {
        "name": form_data.get("name"),
        "age": form_data.get("age"),
        "position": form_data.get("position"),
        "city": form_data.get("city"),
        "salary": form_data.get("salary"),
        "joined": form_data.get("joined"),
        "url": file_url,
        "status": form_data.get("status"),
    }


def upload_image_to_firebase_storage_and_format_url(key, file):
    """
    upload image to firebase storage and format url

    :param key:
    :param file:
    """
    url = storage.child("image_{key}".format(key=key)).put(file)
    return FILEBASE_IMAGE_URL.format(token=url.get("downloadTokens"))


def create_database_snapshot_for_employees(key, data):
    """
    create database snapshot in firebase and return response

    :param key:
    :param data:
    """
    return (
        database.child("Employees")
        .child(key)
        .set(data, json_kwargs={"indent": 4, "sort_keys": True, "default": str})
    )


# def create_database_snapshot_for_users(key, data):
#     """
#     _summary_

#     :param key: _description_
#     :param data: _description_
#     """


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
