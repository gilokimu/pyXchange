import os
from os.path import dirname, join

from dotenv import load_dotenv


load_dotenv(join(dirname(__file__), '.env'))

API_KEY = os.getenv("HITBTC_API_KEY")
SECRET_KEY = os.getenv("HITBTC_SECRET_KEY")
