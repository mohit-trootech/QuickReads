import pyrebase
from dotenv import dotenv_values

env_config = dotenv_values(".env")
config = {
    "apiKey": env_config.get("API_KEY"),
    "authDomain": env_config.get("AUTH_DOMAIN"),
    "databaseURL": env_config.get("DATABASE_URL"),
    "projectId": env_config.get("PROJECT_ID"),
    "storageBucket": env_config.get("STORAGE_BUCKET"),
    "messagingSenderId": env_config.get("MESSAGING_SENDER_ID"),
    "appId": env_config.get("APP_ID"),
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
storage = firebase.storage()
