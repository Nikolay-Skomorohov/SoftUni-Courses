"""
Program: Tech Screening in Jobs bg.py
Author: Nikolay Skomorohov

The script searches jobs.bg for the amount of job listings per software technology.

1. Script setup
2. Go to jobs.bg
3. Loop for counting listings
4. Append result to a file

"""

# 1. SCRIPT SETUP


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SoftTech:
    def __init__(self):
        self.tech_total = 0
        self.bulgaria = 0
        self.sofia = 0
        self.plovdiv = 0
        self.varna = 0
        self.burgas = 0
        self.stara_zagora = 0
        self.ruse = 0

    def add_to_city(self, city):
        pass


class Python(SoftTech):
    def __init__(self):
        super().__init__()
        self.django = 0
        self.flask = 0
        self.pandas = 0
        self.tensor_flow = 0


class JavaScript(SoftTech):
    def __init__(self):
        super().__init__()
        self.jquery = 0
        self.angular = 0
        self.react = 0
        self.vue = 0
        self.express = 0
        self.nodejs = 0
        self.ember = 0


class PHP(SoftTech):
    def __init__(self):
        super().__init__()
        self.symfony = 0
        self.laravel = 0
        self.drupal = 0


class Java(SoftTech):
    def __init__(self):
        super().__init__()
        self.spring = 0


class CPlus(SoftTech):
    pass


class CSharp(SoftTech):
    pass


class Swift(SoftTech):
    pass


class ObjectC(SoftTech):
    pass


class DotNet(SoftTech):
    def __init__(self):
        super().__init__()
        self.aspnet = 0


class Rust(SoftTech):
    pass


class Ruby(SoftTech):
    def __init__(self):
        super().__init__()
        self.ruby_on_rails = 0


class Kotlin(SoftTech):
    pass


class TypeScript(SoftTech):
    pass


class CofeeScript(SoftTech):
    pass


class Perl(SoftTech):
    pass


class WebAssembly(SoftTech):
    pass


class SQL(SoftTech):
    def __init__(self):
        super().__init__()
        self.mysql = 0
        self.postgresql = 0
        self.elasticsearch = 0
        self.mongodb = 0
        self.sqlite = 0
        self.sqlalchemy = 0


class HTML(SoftTech):
    pass


class CSS(SoftTech):
    pass


gecko_driver = 'C:\\geckodriver.exe'
# options = webdriver.FirefoxOptions()
# options.add_argument('-headless')
browser = webdriver.Firefox(executable_path=gecko_driver)
browser.get('http://jobs.bg')
button_to_click = browser.find_element_by_xpath(
    "/html/body/table[2]/tbody/tr/td/table[2]/tbody/tr/td[1]/form/table/tbody/tr[7]/td/a/span[1]")
button_to_click.click()
button_to_click = browser.find_element_by_xpath(
    '//*[@id="keyword"]')
text_input = "Python"
button_to_click.send_keys(text_input)
button_to_click = browser.find_element_by_xpath('//*[@id="addKeywordLink"]')
button_to_click.click()
button_to_click = browser.find_element_by_xpath(
    '/html/body/table[2]/tbody/tr/td/table[2]/tbody/tr/td[1]/form/table/tbody/tr[12]/td/a')
browser.implicitly_wait(10)
button_to_click.click()
button_to_click = browser.find_element_by_xpath(
    "/html/body/div[1]/div/div[2]/table[2]/tbody/tr/td/form/div[2]/table/tbody/tr/td/table/tbody/tr[3]/td[1]")
text = button_to_click.text.split()
print(text[-1])








