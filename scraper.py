import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
interval = 60 * 60
normal_price = 1.425

# url = [
#     'https://esgaming.hermanmiller.com/collections/menu/products/embody-gaming-chair'
#     'https://esgaming.hermanmiller.com/collections/menu/products/aeron-chair-medium-b'
#     ]

url = 'https://esgaming.hermanmiller.com/collections/menu/products/aeron-chair-medium-b'


def get_response(*args):
    """Get HTTP response from server and handle gracefully"""

    for link in args:
        try:
            response = requests.get(link)
            response.raise_for_status()
        except HTTPError as http_err:
            logging.error(f'{now} - HTTP error occurred: {http_err}')
        except Exception as err:
            logging.error(f'{now} - Other error occurred: {err}')
        else:
            return response


def check_price(url):
    """Parse HTML on page and find stock value for item"""

    response = get_response(url)
    soup = BeautifulSoup(response.content, 'lxml')
    price = soup.find('span', 'price')
    return price

while True:
    now = datetime.now()
    now_price = check_price(url)
    price = float(now_price.contents[0].replace(',', ''))

    if price < normal_price:
        logging.info(f"Discount baby!: {price}")
        break
    else:
        logging.info(f"{now} - No change in price: {price}. Checking again in {interval} seconds")
        sleep(interval)
        continue

