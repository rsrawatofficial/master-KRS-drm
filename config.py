import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8003649544:AAGoiThVN8KLJyKGsGf1BcfTsjDTrSmjFR8")
    API_ID = int(os.environ.get("API_ID", "27900743"))
    API_HASH = os.environ.get("API_HASH", "7857589413:AAE79aTmwa6-LIdbK0L4xS1byZJQIH2IR8U")
    AUTH_USER = os.environ.get("AUTH_USERS", '7804396225').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "[꧁ 𝐉𝐨𝐡𝐧 𝐖𝐢𝐜𝐤 ꧂]"
