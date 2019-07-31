class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        new_value = value.split()
        if len(new_value) < 2:
            self.__author = value
        elif value.split()[1][0].isdigit():
            raise Exception("Author not valid!")
        else:
            self.__author = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if len(value) < 3:
            raise Exception("Title not valid!")
        else:
            self.__title = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception("Price not valid!")
        self.__price = value

    def __str__(self):
        return f"Type: {self.__class__.__name__}\n" \
               f"Title: {self.title}\n" \
               f"Author: {self.author}\n" \
               f"Price: {self.price:.2f}\n"


class GoldenEditionBook(Book):
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception("Price not valid!")
        else:
            self.__price = value * 1.3


new_author = input()
new_title = input()
new_price = float(input())

try:
    new_book = Book(author=new_author, title=new_title, price=new_price)
    new_GEB = GoldenEditionBook(author=new_author, title=new_title, price=new_price)
    print(new_book)
    print(new_GEB)

except Exception as text:
    print(text)
