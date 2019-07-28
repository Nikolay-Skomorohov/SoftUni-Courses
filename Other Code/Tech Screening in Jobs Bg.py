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


geckodriver = 'C:\\geckodriver.exe'
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
browser = webdriver.Firefox(executable_path=geckodriver, options=options)
browser.get('http://jobs.bg')









