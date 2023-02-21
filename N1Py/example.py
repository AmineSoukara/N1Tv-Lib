import re
import threading
import traceback
from pathlib import PurePosixPath
from urllib.parse import quote, unquote, urlparse

import humanize
import markdown
import requests
import urllib3
from bs4 import BeautifulSoup
from dotmap import DotMap
from strsimpy.ngram import NGram

from requests import Session, get

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Example:
    def __init__(self, base_url="https://example.com"):

        self.USER_AGENT = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
        }
        self.session = Session
        url = get(base_url).url
        self.url = [url, url[:-1]][url[-1] == "/"]
        self.search_url = self.url + "/search?q="
        self.switcher = {
            "المسلسل": "serie",
            "البرنامج": "show",
            "الأنمي": "anime",
            "العرض مصارعة": "wwe",
            "البلد": "country",
            "اللغة": "language",
            "التصنيف": "genres",
            "النوع": "type",
            "التقييم": "rating",
            "تقييم المسلسل": "rating",
            "تقييم الأنمي": "rating",
            "تقييم البرنامج": "rating",
            "تقييم العرض مصارعة": "rating",
            "المدة": "duration",
            "الجودة": "quality",
            "الدقة": "accuracy",
            "الحجم": "size",
            "التحميل": "download",
            "الترجمة": "translation",
            "السنة": "year",
            "جودة الفيلم": "quality",
            "انتاج": "country",
            "مدة الفيلم": "duration",
            "مدة المسلسل": "duration",
            "مدة البرنامج": "duration",
            "مدة الحلقة": "duration",
            "الحلقة التالية": "next_episode",
            "الحلقة السابقة": "previous_episode",
        }

    def name(self, txt):
        txt = txt.strip()
        ok = self.switcher.get(txt, txt)
        return ok

    def search(
        self,
        query,
        includeMovies=False,
        includeSeries=False,
        includeShows=False,
        includeAnimes=False,
        includeAll=False,
        order=False,
        extra=True,
    ):
        return [{}]

    def getPage(
        self,
        type="recent",
        page=0,
        includeAll=False,
        includeMovies=False,
        includeSeries=False,
        includeAnimes=False,
        includeShows=False,
        includeEpisodes=False,
    ):
        return [{}]

    def getPages(
        self,
        type="recent",
        pages=2,
        includeAll=False,
        includeMovies=False,
        includeSeries=False,
        includeAnimes=False,
        includeShows=False,
        includeEpisodes=False,
    ):
        return [{}]

    def __getpage(
        self,
        URL,
        includeAll=False,
        includeMovies=False,
        includeSeries=False,
        includeAnimes=False,
        includeShows=False,
        includeEpisodes=False,
    ):
        a = {
                            "type": "",
                            "id": "",
                            "title": "",
                            "quality": "",
                            "genres": [],
                            "url": "",
                            "rating": "",
                            "img": "",
                            
                        }
        return [a]

    def get_episodes(self, url, order=True):
        data = {
                    "link": link,
                    "img": img,
                    "title": title,
                    "id": id,
                }

        return [data]

    def dl(self, link):
        a = {
                "quality": "",
                "resolution": "",
                "url": "",
                "type": "",
                "origin_name": "",
                "file_name": "",
                "name": "",
                "size": {"humanbytes": "", "bytes": ""},
            }
        return [a]

    def info(self, url):
        done = {}
        return done

    def get_title(self, url, soup=None:
        if not soup:
            soup = self.soup(url)

        title = ""
        return title

    def get_seasons(self, url, soup=None):
        if not soup:
            soup = self.soup(url)

        data = {
                "title": "",
                "link": "",
                "id": "",
            }

        return [data]


    def get_image(self, url, soup=None):
        if not soup:
            soup = self.soup(url)

        img = ""
        return img

    def get_type(self, url, soup=None):
        if not soup:
            soup = self.soup(url)
        type = ""
        return  type

    def get_last_page_number(self, url, soup=None):
        if not soup:
            soup = self.soup(url)

        last_page_num = ""
        return last_page_num

    def soup(self, url):
        """This Function Helps To make the code more cleaner"""
        req = get(url).content.decode()
        soup = BeautifulSoup(req, features="html.parser")
        return soup
