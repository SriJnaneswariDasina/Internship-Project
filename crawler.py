import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited = set()

def crawl(base_url, max_depth=2):
    urls = set()

    def _crawl(url, depth):
        if depth > max_depth or url in visited:
            return
        visited.add(url)
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'lxml')
            urls.add(url)
            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link['href'])
                if urlparse(full_url).netloc == urlparse(base_url).netloc:
                    _crawl(full_url, depth + 1)
        except:
            pass

    _crawl(base_url, 0)
    return list(urls)
