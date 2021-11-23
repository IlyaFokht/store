import requests
import json
from conf import keys


class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert( quote: str, base:str, amount:str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/pricemulti?fsyms={quote_ticker}&tsyms={base_ticker}&api_key=221b49777c8d87e48471043dc1edbd4bf18a63ae4d827b83846db2ed35562562')
        total_base = json.loads(r.content)[keys[quote]][keys[base]]
        total_base *= amount
        return total_base