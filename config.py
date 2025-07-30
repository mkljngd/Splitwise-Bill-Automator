import os
from dotenv import load_dotenv

load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
API_KEY = os.getenv("API_KEY")

USERS_DICT = {"M": "Mukul", "D": "Dipayan", "H": "Sri"}
