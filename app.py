
from slack_sdk import WebClient
from os import getenv
from api_client import CurrencyApiClient, Currencies

SLACK_TOKEN = getenv("SLACK_API_TOKEN")
SLACK_CHANNEL_NAME = getenv("SLACK_CHANNEL_NAME")
BASE_URL = getenv("BASE_URL")
api_client = CurrencyApiClient(BASE_URL)
slack_client = WebClient(token=SLACK_TOKEN)

data = api_client.get_last(Currencies.USD)
today_price = data['USDBRL']

today_price_formatted = "R$ {:,.2f}".format(float(today_price['ask'])).replace('.', ',')
today_variation_formatted = f"{today_price['varBid'].replace('.', ',')}%"
message = f"USD is trading at {today_price_formatted} with a variation of {today_variation_formatted}"

if float(today_price['varBid']) < 0:
    slack_client.chat_postMessage(
        channel=SLACK_CHANNEL_NAME,
        text=message
    )
