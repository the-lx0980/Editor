import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    API_ID = int(os.environ.get("API_ID", 12345))

    API_HASH = os.environ.get("API_HASH", "")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
  
    
