# Scraping Yahoo Finances

## Install depencences:

```
pipenv shell

pipenv install

```

## Scrapy execution (manual):

#### Generates a json file with bones information

```
cd yahoo_finances

scrapy crawl yahoo   

```

## Scrapy execution (cron):

#### Run a cron to generete the json with the data

```
python cron.py

```

## Flask Server:

#### Exposes an endpoint with the generated data in <http://127.0.0.1:5000/yahoo>

```
python main.py

```
