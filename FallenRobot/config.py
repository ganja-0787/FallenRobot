class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 27744639
    API_HASH = "a5e9da62bcd7cc761de2490c52c89ccf"

    CASH_API_KEY = "BUATLRCHB18ICFC0"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://inrxxedz:HzJvAfoh73yRlx64xGp8Bg2WA0XVR5oa@tiny.db.elephantsql.com/inrxxedz"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002279809564)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://waifuuu0786:sungjinwoo@cluster0.uctgneu.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://i.ibb.co/Y8tMqkB/photo-2024-10-29-17-43-43.jpg"

    SUPPORT_CHAT = "ur_hell_paradise"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "8066514303:AAHaQOjQYGa-lPCDJ0hLl-assumizp80U9E"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "3LPPBQ5DET7O"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7775259302  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = [7775259302]  # List of groups that you want blacklisted.
    DRAGONS = [7775259302]  # User id of sudo users
    DEV_USERS = [7775259302]  # User id of dev users
    DEMONS = [7775259302]  # User id of support users
    TIGERS = [7775259302]  # User id of tiger users
    WOLVES = [7775259302]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
