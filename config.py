import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    MPESA_CONSUMER_KEY = os.getenv("MPESA_CONSUMER_KEY")

    MPESA_CONSUMER_SECRET = os.getenv("MPESA_CONSUMER_SECRET")

    MPESA_SHORTCODE = os.getenv("MPESA_SHORTCODE")

    MPESA_PASSKEY = os.getenv("MPESA_PASSKEY")

    CALLBACK_URL = os.getenv("CALLBACK_URL")