from config import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
from urllib.parse import quote
import pymongo

browser = webdriver.Chrome()

wait = WebDriverWait(browser, 10)
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def main():
    """
    遍历每一页
    """
    for i in range(1, MAX_PAGE+1):
        index_page(i)
    browser.close()


def index_page(page):
    """
    :param page: 页码
    :return:
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://www.jobui.com/jobs?cityKw='+ quote(CITY)+'&jobKw=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.j-pageNum > .pager > a.pg-updown')))
            submit.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.j-recommendJob .c-job-list')))
        get_content()
    except TimeoutException:
        index_page(page)

def get_content():
    """
       提取求职信息
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('.j-recommendJob .c-job-list').items()
    for item in items:
        content={
            'company_name': item.find('.job-content a.job-company-name').text()
        }
        print(content)

if __name__ == '__main__':
    main()
