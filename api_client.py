from splitwise import Splitwise
from config import CONSUMER_KEY, CONSUMER_SECRET, API_KEY


def get_splitwise_object():
    return Splitwise(CONSUMER_KEY, CONSUMER_SECRET, api_key=API_KEY)
