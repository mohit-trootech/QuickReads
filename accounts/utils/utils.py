from quickreads.utils.firebase_config import *


def create_user_session_in_request(request, user):
    """
    create user session in request

    :param request:
    :param user:
    """
    session_id = user.get("idToken")
    request.session["uid"] = session_id


def serialize_user_object_data(data: dict):
    """
    serialize user object data in required format

    :param data: dict
    """
    return {
        "name": data.get("name"),
        "email": data.get("email"),
        "age": data.get("age", None),
        "phone": data.get("phone", None),
        "address": data.get("address", None),
        "gender": data.get("gender", None),
        "profile": data.get("profile", None),
        "status": data.get("status", 0),
    }


def create_user_information_in_database(user, data):
    """
    create user information in database

    :param user:
    :param data:
    """
    data = serialize_user_object_data(data=data)
    uid = user.get("localId")
    database.child("users").child(uid).child("details").set(data)
    uid = user.get("localId")
    database.child("users").child(uid).child("details").set(data)
