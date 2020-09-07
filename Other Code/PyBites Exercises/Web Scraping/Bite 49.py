from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    book_title = soup.find_all("div", class_="dotd-title")[0].h2.get_text().strip()
    book_desc = soup.find_all("div", class_="dotd-title")[
        0].next_sibling.next_sibling.next_sibling.next_sibling.get_text().strip()
    book_link = soup.find_all("div", class_="dotd-main-book-image float-left")[0].a.get('href')
    book_img = soup.find_all("img", class_="bookimage imagecache imagecache-dotd_main_image")[0]["src"]
    return Book(title=book_title, description=book_desc, image=book_img, link=book_link)
