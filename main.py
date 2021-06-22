import codecs
from urllib.parse import urljoin
import json

import requests
import bs4
import arrow
import os

BASE_URL = "https://tuoitre.vn"
SOURCE_URL = "https://tuoitre.vn/tin-moi-nhat.htm"


def get_article_content(url):
    """Lấy nội dung bài viết từ url"""
    data = {}
    r = requests.get(url)
    if r.ok:
        s = bs4.BeautifulSoup(r.content, 'lxml')
        title = s.select_one('h1.article-title')
        sub_title = s.select_one('h2.sapo')
        content = s.select_one('div#main-detail-body')
        data['title'] = title.text if title else ''
        data['sub_title'] = sub_title.text if sub_title else ''
        data['content'] = content.prettify() if content else ''
        pub_date = s.select_one('div#main-detail .date-time')
        pub_date = pub_date.text.replace(' GMT+7', '')
        pub_date = arrow.get(pub_date, 'DD/MM/YYYY HH:mm').replace(tzinfo='Asia/Ho_Chi_Minh')
        data['pub_date'] = pub_date.format(locale='vi')
    return data


def main():
    r = requests.get(SOURCE_URL)
    if r.ok:
        s = bs4.BeautifulSoup(r.content, 'lxml')
        links = s.select('.list-news-content .news-item')
        for a in links:
            post_id = a.attrs['data-newsid']
            link = a.select_one('h3 > a')
            article = get_article_content(urljoin(BASE_URL, link.attrs['href']))

            # Tạo thư mục
            dir_name = arrow.get(article['pub_date']).format('YYYY-MM')
            if not os.path.isdir(dir_name):
                os.mkdir(dir_name)
            # Tạo file name
            file_name = arrow.get(article['pub_date']).format('YYYY-MM-DD-HH')
            article['post_id'] = file_name + "-" + post_id
            file_name = file_name + "-" + post_id + ".json"
            file_name = os.path.join(dir_name, file_name)

            f = codecs.open(file_name, encoding='utf-8', mode='w')
            json.dump(article, f, ensure_ascii=False, indent=2)
    else:
        print("Không truy cập được")


def replaceText():
    pass


if __name__ == '__main__':
    replaceText()
