import schedule
import time
import subprocess

def run_spider():
    subprocess.run(['scrapy', 'crawl', 'yahoo'], cwd='yahoo_finances/yahoo_finances')

schedule.every(1).minutes.do(run_spider)

while True:
    schedule.run_pending()
    time.sleep(1)