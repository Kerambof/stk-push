import requests
import base64
from datetime import datetime
from requests.auth import HTTPBasicAuth

from config import Config


# =====================================
# GET ACCESS TOKEN
# =====================================
def get_access_token():

    url = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    response = requests.get(
        url,
        auth=HTTPBasicAuth(
            Config.MPESA_CONSUMER_KEY,
            Config.MPESA_CONSUMER_SECRET
        )
    )

    if response.status_code == 200:
        return response.json()["access_token"]

    return None


# =====================================
# GENERATE PASSWORD
# =====================================
def generate_password():

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    password = base64.b64encode(
        (
            Config.MPESA_SHORTCODE +
            Config.MPESA_PASSKEY +
            timestamp
        ).encode()
    ).decode()

    return timestamp, password


# =====================================
# STK PUSH
# =====================================
def stk_push(phone, amount):

    token = get_access_token()

    if token is None:
        return {
            "success": False,
            "message": "Failed to generate access token."
        }

    timestamp, password = generate_password()

    url = "https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {

        "BusinessShortCode": Config.MPESA_SHORTCODE,

        "Password": password,

        "Timestamp": timestamp,

        "TransactionType": "CustomerBuyGoodsOnline",

        "Amount": int(amount),

        "PartyA": phone,

        "PartyB": Config.MPESA_SHORTCODE,

        "PhoneNumber": phone,

        "CallBackURL": Config.CALLBACK_URL,

        "AccountReference": "STK TEST",

        "TransactionDesc": "Testing STK Push"

    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    return response.json()