import requests
from enum import Enum


class Currencies(Enum):
    USD = 'usd'


class CurrencyApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_last(self, currency: Currencies):
        url = f"{self.base_url}/last/{currency.value}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        return response.json()
