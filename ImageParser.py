# # from icrawler.builtin import GoogleImageCrawler

# # # google_crawler = GoogleImageCrawler(storage={'root_dir': 'Sonic'})
# # # google_crawler.crawl(keyword='Sonic The Hedgehog', max_num=200)

# from icrawler.builtin import GreedyImageCrawler

# greedy_crawler = GreedyImageCrawler(storage={'root_dir': 'Sonic'})
# greedy_crawler.crawl(domains='https://yandex.ru/images/search?text=Sonic', max_num=50,
#                      min_size=None, max_size=None)


import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

driver.get("https://yandex.ru/images/search?from=tabbar&text=Sonic")
results = []
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")


def parse_image_urls(classes, location, source):
    for a in soup.findAll(attrs={"class": classes}):
        name = a.find(location)
        if name not in results:
            results.append(name.get(source))


parse_image_urls("s-item__image-wrapper image-treatment", "img", "src")