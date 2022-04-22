import logging
import time
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen

import schedule
from lxml.cssselect import CSSSelector
from lxml.html import fromstring as html_fromstring
from redis import Redis
from settings import (JOB_LINK_SELECTOR, REDIS_CHANNEL, REDIS_HOST, REDIS_PORT,
                      URLS)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
redis = Redis(host=REDIS_HOST, port=REDIS_PORT)


def parse():
    logging.info("Parsing is started.")
    links_count = 0
    for url in URLS:
        html_tree = html_fromstring(urlopen(url).read())
        job_link_selector = CSSSelector(JOB_LINK_SELECTOR)
        job_links = [e.get("href") for e in job_link_selector(html_tree)]
        links_count += len(job_links)
        for link in job_links:
            link_without_query = urljoin(link, urlparse(link).path)
            redis.publish(REDIS_CHANNEL, link_without_query)
    logging.info("Done! %d links fetched", links_count)


if __name__ == "__main__":
    schedule.every(5).minutes.do(parse)
    schedule.run_all()
    while True:
        schedule.run_pending()
        time.sleep(10)
