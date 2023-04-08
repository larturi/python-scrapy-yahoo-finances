# Scraping Yahoo Finances

## Install Depencences

```
pipenv shell

pipenv install

```

## Scrapy Crawl Execution

#### Generates a json file with bones information

```
cd yahoo_finances

scrapy crawl yahoo   

```

## Flask Server

#### Exposes an endpoint with the generated data in <http://127.0.0.1:5000/yahoo>

```
python main.py

```
