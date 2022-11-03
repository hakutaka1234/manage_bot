from HakutakaRobot.sample_config import Config

class Development(Config):
LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 17278438  # integer value, dont use ""
    API_HASH = "7886b64c08117902bf1aaff07280b512"
    TOKEN = "5622516770:AAFZ3jZV0WU1fFY5GpNF1ba2GPg_4VTpDN8"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1954780613  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "gemini_hakutaka"
    SUPPORT_CHAT = "evzesda"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001686544997
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001686544997
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://xefvomva:ITUQ4uaQlxZwQajl0hV5VPjgYL6falXF@jelani.db.elephantsql.com/xefvomva"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    MONGO_DB_URI = ""
    ARQ_API_KEY = "WZUJJH-MSBTKJ-NUFTNA-XVVSOJ-ARQ"
    URL = None
    SPAMWATCH_API = "7uGFiAfdrcjaDaLEv2j~qp~25NxnldP54OTqh8ZdAlhSe6E7GXEL~HlmR~f0saOb"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = 1954780613
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = 1954780613
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = 1954780613
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = 1954780613
    WOLVES = 1954780613
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5432
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = False  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "9HLRVYSUNY1EQEKB"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "MHCCEF9DHQDV"  # Get your API key from https://timezonedb.com/api
    WALL_API = None
    AI_API_KEY = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None