# Herman Miller price scraper
This script will monitor the prices for all Herman Miller (Logitech) chairs. These are the only versions that are easy to find here in Spain.

It contains a dict of the urls for each chair and its 'normal' price. The script will scrape the price every hour and send a notification to Telegram when the price has fallen below normal. The script will exit when all items are on discount. You will need to set your own Telegram `CHAT_ID` and `TELEGRAM_TOKEN` (See [here](https://core.telegram.org/bots) for more info)

## Installation
I have included a Dockerfile and docker-compose file. Simply build the Docker image and bring up the project.

```
EXPORT CHAT_ID="your_chat_id"
EXPORT TELEGRAM_TOKEN="your_telegram_token"

git clone https://github.com/gmcmillan82/herman-miller-scraper
cd herman-miller-scraper
docker build -t herman-miller-scraper:v1 .
docker-compose up -d
```
