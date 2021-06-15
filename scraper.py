import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime
import logging

"""Things left to do: Setup format logging to remove {now} prints
    Improve/refactor error handling in request"""

logging.basicConfig(level=logging.INFO)
interval = 60 * 60

urls = {
    'https://esgaming.hermanmiller.com/collections/menu/products/embody-gaming-chair': 1.425,
    'https://esgaming.hermanmiller.com/collections/menu/products/aeron-chair-medium-b': 1.427,
    'https://esgaming.hermanmiller.com/collections/menu/products/sayl-chair-red': 678
}

discounted = []


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
    for url, normal_price in urls.items():
        if url not in discounted:
            now = datetime.now()
            now_price = check_price(url)
            price = float(now_price.contents[0].replace(',', ''))
            if price < normal_price:
                logging.info(f"Discount baby!: €{price} @ {url}")
                discounted.append(url)
                continue
            else:
                logging.info(f"{now} - No change in price: €{price}")
                if ((len(discounted)) < len(urls)):
                    print(f'List contains: {discounted}')
                    continue
                else:
                    exit('All items are now discounted. Exiting.') 
    logging.info(f'Sleeping for {interval}')
    sleep(interval)

