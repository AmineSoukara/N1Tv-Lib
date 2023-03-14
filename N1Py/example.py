import urllib3
from bs4 import BeautifulSoup
from requests import Session, get

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Example:
    def __init__(self, base_url="https://example.com"):
        self.Headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }
        self.Session = Session
        url = get(base_url, headers=self.Headers).url
        self.url = [url, url[:-1]][url[-1] == "/"]
        self.search_url = self.url + "/search?q="
        self.switcher = {
            "المسلسل": "serie",
            "البرنامج": "show",
            "الأنمي": "anime",
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

    def info(self, url, soup=None):
        if not soup:
            soup = self.soup(url)
        done = {}
        return done

    def get_seasons(self, url, soup=None):
        if not soup:
            soup = self.soup(url)
        data = {
            "title": "",
            "link": "",
            "id": "",
        }
        return [data]

    def get_episodes(self, url, order=True):
        data = {
            "link": link,
            "img": img,
            "title": title,
            "id": id,
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
        return type

    def get_id(self, url, soup=None):
        if not soup:
            soup = self.soup(url)
        id = ""
        return id

    def get_link(self, id):
        link = ""
        return link

    def soup(self, url):
        """This Function Helps To make the code more cleaner"""
        req = get(url, headers=self.Headers).content.decode()
        soup = BeautifulSoup(req, features="html.parser")
        return soup
