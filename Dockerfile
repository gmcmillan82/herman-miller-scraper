FROM python:3.9.5-alpine

COPY . /scraper

RUN cd /scraper && \
	apk update && \
	apk add --update --no-cache g++ \
		gcc \
		py3-pip \
		libxml2 \
		libxslt \
		libxml2-dev \
		libxslt-dev \
	py3-lxml && \
	pip3 install -r requirements.txt

CMD ["python", "-u", "/scraper/price-scraper.py"]