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

    def add_to_city(self, city: str, value: int):
        if city in "sofia":
            self.sofia += value
        elif city in "plovdiv":
            self.plovdiv += value
        elif city in "varna":
            self.varna += value
        elif city in "burgas":
            self.burgas += value
        elif city in "stara zagora":
            self.stara_zagora += value
        elif city in "ruse":
            self.ruse += value
        self.bulgaria += value


class Python(SoftTech):
    def __init__(self):
        super().__init__()
        self.django = 0
        self.flask = 0
        self.pandas = 0
        self.tensor_flow = 0
        self.bottle = 0
        self.numpy = 0
        self.pyramid = 0
        self.web2py = 0
        self.cherrypy = 0
        self.tornado = 0
        self.pylons = 0
        self.turbogears = 0
        self.keras = 0
        self.pytorch = 0
        self.theano = 0
        self.matplotlib = 0
        self.scikit = 0
        self.scrapy = 0
        self.pygame = 0

    def add_to_framework(self, frame: str, value: int):
        if frame in "django":
            self.django += value
        elif frame in "flask":
            self.flask += value
        elif frame in "pandas":
            self.pandas += value
        elif frame in "tensor-flow, tensorflow":
            self.tensor_flow += value
        elif frame in "bottle":
            self.bottle += value
        elif frame in "numpy":
            self.numpy += value
        elif frame in "pyramid":
            self.pyramid += value
        elif frame in "web2py":
            self.web2py += value
        elif frame in "cherrypy":
            self.cherrypy += value
        elif frame in "tornado":
            self.tornado += value
        elif frame in "pylons":
            self.pylons += value
        elif frame in "turbogears, turbo-gears":
            self.turbogears += value
        elif frame in "keras":
            self.keras += value
        elif frame in "pytorch":
            self.pytorch += value
        elif frame in "theano":
            self.theano += value
        elif frame in "matplotlib":
            self.matplotlib += value
        elif frame in "scikit":
            self.scikit += value
        elif frame in "scrapy":
            self.scrapy += value
        elif frame in "pygame":
            self.pygame += value


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

    def add_to_framework(self, frame: str, value: int):
        if frame in "jquery":
            self.jquery += value
        elif frame in "angular.js":
            self.angular += value
        elif frame in "react.js":
            self.react += value
        elif frame in "vue.js":
            self.vue += value
        elif frame in "express":
            self.express += value
        elif frame in "node.js":
            self.nodejs += value
        elif frame in "ember":
            self.ember += value


class PHP(SoftTech):
    def __init__(self):
        super().__init__()
        self.symfony = 0
        self.laravel = 0
        self.drupal = 0
        self.wordpress = 0

    def add_to_framework(self, frame: str, value: int):
        if frame in "symfony":
            self.symfony += value
        elif frame in "laravel":
            self.laravel += value
        elif frame in "drupal":
            self.drupal += value
        elif frame in "wordpress":
            self.wordpress += value


class Java(SoftTech):
    def __init__(self):
        super().__init__()
        self.spring = 0

    def add_to_framework(self, frame: str, value: int):
        if frame in "spring":
            self.spring += value


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

    def add_to_framework(self, frame: str, value: int):
        if frame in "aspnet":
            self.aspnet += value


class Rust(SoftTech):
    pass


class Ruby(SoftTech):
    def __init__(self):
        super().__init__()
        self.ruby_on_rails = 0

    def add_to_framework(self, frame: str, value: int):
        if frame in "ruby on rails":
            self.ruby_on_rails += value


class Kotlin(SoftTech):
    pass


class TypeScript(SoftTech):
    pass


class CoffeeScript(SoftTech):
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
        self.mariadb = 0

    def add_to_framework(self, frame: str, value: int):
        if frame in "mysql":
            self.mysql += value
        elif frame in "postgresql":
            self.postgresql += value
        elif frame in "elasticsearch":
            self.elasticsearch += value
        elif frame in "mongodb":
            self.mongodb += value
        elif frame in "sqlite":
            self.sqlite += value
        elif frame in "sqlalchemy":
            self.sqlalchemy += value
        elif frame in "mariadb":
            self.mariadb += value


class HTML(SoftTech):
    pass


class CSS(SoftTech):
    pass


class Go(SoftTech):
    pass


class Scala(SoftTech):
    pass


class Haskell(SoftTech):
    pass


class Erlang(SoftTech):
    pass


class Elexir(SoftTech):
    pass


class Matlab(SoftTech):
    pass


class Groovy(SoftTech):
    pass


class VisualBasic(SoftTech):
    pass


class Delphi(SoftTech):
    pass


class Dart(SoftTech):
    pass


class Julia(SoftTech):
    pass


class Clojure(SoftTech):
    pass


class VBA(SoftTech):
    pass


class Bash(SoftTech):
    pass


# 2. GO TO JOBS.BG

cities = ("all", "sofia", 'plovdiv', 'varna', 'burgas', 'stara zagora', 'ruse')
technologies = ('python', 'javascript', 'php', 'java',
                'c++', 'c#', 'swift', 'objectc', '.net',
                'rust', 'ruby', 'kotlin', 'typescript',
                'coffeescript', 'perl', 'webassembly', 'sql',
                'html', 'css', 'go', 'scala',
                'haskell', 'erlang', 'elexir', 'matlab',
                'groovy', 'visual basic', 'delphi', 'dart',
                'julia', "clojure", 'vba', 'bash',)

'''
for city in cities:
    for tech in techs:
        for lib in libreries:
            gecko_driver = 'C:\\geckodriver.exe'
            options = webdriver.FirefoxOptions()
            options.add_argument('-headless')
            browser = webdriver.Firefox(executable_path=gecko_driver, options=options)
            browser.get('http://jobs.bg')
            button_to_click = browser.find_element_by_xpath(
                "/html/body/table[2]/tbody/tr/td/table[2]/tbody/tr/td[1]/form/table/tbody/tr[7]/td/a/span[1]")
            button_to_click.click()
            button_to_click = browser.find_element_by_xpath(
                '//*[@id="keyword"]')
            text_input = "pycharm"
            button_to_click.send_keys(text_input)
            button_to_click = browser.find_element_by_xpath('//*[@id="addKeywordLink"]')
            button_to_click.click()
            button_to_click = browser.find_element_by_xpath(
                '/html/body/table[2]/tbody/tr/td/table[2]/tbody/tr/td[1]/form/table/tbody/tr[12]/td/a')
            browser.implicitly_wait(5)
            button_to_click.click()
            button_to_click = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/table[2]/tbody/tr/td/form/div[2]/table/tbody/tr/td/table/tbody/tr[3]/td[1]")
            text = button_to_click.text.split()
            print(text[-1])'''
