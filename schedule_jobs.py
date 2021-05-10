import time
from app_package.scraper import Scraper


def run_scraper():
    news_scraper = Scraper()
    news_scraper.run()


if __name__ == '__main__':
    while True:
        run_scraper()
        time.sleep(3600) # sleep for one hour