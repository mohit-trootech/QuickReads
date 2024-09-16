from quickreads.utils.firebase_config import auth, database, storage
from accounts.utils.constants import Key


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


def get_current_logged_in_user(request):
    """
    get current logged in User
    """
    uid = request.session.get("uid")
    details = auth.get_account_info(uid)
    user_raw = (
        database.child("users")
        .child(details.get("users")[0].get("localId"))
        .child("details")
        .get()
        .val()
    )

    return serialize_user_object(user_raw)


def serialize_user_object(user_raw):
    """
    serialize user object

    :param user_raw:
    """
    user = {}
    for key, value in user_raw.items():
        user[key] = value
    return user


def upload_user_profile_image_to_firebase_storage_and_format_url(user, file):
    """
    upload user profile image to firebase storage and format url
    """
    url = storage.child("{user}".format(user=user)).put(file)
    return url.get("downloadTokens")  # type: ignore


def get_user_localId(request):
    """
    get current logged in User localId
    """
    uid = request.session.get("uid")
    details = auth.get_account_info(uid)
    return details.get("users")[0].get("localId")


def update_user_data_to_firebase_database(localId, data):
    """
    update user data to firebase database
    """
    return (
        database.child("users")
        .child(localId)
        .child("details")
        .update(data, json_kwargs={"indent": 4, "sort_keys": True, "default": str})
    )


def serialize_user_form_data(data):
    """
    serialize user form data
    """
    user = {}
    for i, j in data.items():
        if i != Key.PROFILE.value:
            user[i] = j
    return user
