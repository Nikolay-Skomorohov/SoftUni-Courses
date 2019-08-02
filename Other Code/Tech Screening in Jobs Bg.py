"""
Program: Tech Screening in Jobs Bg.py
Author: Nikolay Skomorohov

The script searches jobs.bg for the amount of job listings per software technology.

1. Script setup
2. Create the database
3. Go to jobs.bg
4. Create a file with the results

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

    def search_term(self):
        return 'python'

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

    def search_term(self):
        return 'javascript'


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

    def search_term(self):
        return 'php'


class Java(SoftTech):
    def __init__(self):
        super().__init__()
        self.spring = 0

    def add_to_framework(self, frame: str, value: int):
        if frame in "spring":
            self.spring += value

    def search_term(self):
        return 'java'


class CPlus(SoftTech):
    def search_term(self):
        return 'c++'


class CSharp(SoftTech):
    def search_term(self):
        return 'c#'


class Swift(SoftTech):
    def search_term(self):
        return 'swift'


class ObjectC(SoftTech):
    def search_term(self):
        return 'objectc'


class DotNet(SoftTech):
    def __init__(self):
        super().__init__()
        self.aspnet = 0

    def add_to_framework(self, frame: str, value: int):
        if frame in "aspnet":
            self.aspnet += value

    def search_term(self):
        return '.net'

class Rust(SoftTech):
    def search_term(self):
        return 'rust'


class Ruby(SoftTech):
    def __init__(self):
        super().__init__()
        self.ruby_on_rails = 0

    def add_to_framework(self, frame: str, value: int):
        if frame in "ruby on rails":
            self.ruby_on_rails += value

    def search_term(self):
        return 'ruby'
class Kotlin(SoftTech):
    def search_term(self):
        return 'kotlin'


class TypeScript(SoftTech):
    def search_term(self):
        return 'typescript'


class CoffeeScript(SoftTech):
    def search_term(self):
        return 'coffeescript'


class Perl(SoftTech):
    def search_term(self):
        return 'perl'


class WebAssembly(SoftTech):
    def search_term(self):
        return 'webassembly'


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


    def search_term(self):
        return 'sql'


class HTML(SoftTech):
    def search_term(self):
        return 'html'


class CSS(SoftTech):
    def search_term(self):
        return 'css'


class Go(SoftTech):
    def search_term(self):
        return 'go'


class Scala(SoftTech):
    def search_term(self):
        return 'scala'


class Haskell(SoftTech):
    def search_term(self):
        return 'haskell'


class Erlang(SoftTech):
    def search_term(self):
        return 'erlang'


class Elexir(SoftTech):
    def search_term(self):
        return 'elexir'


class Matlab(SoftTech):
    def search_term(self):
        return 'matlab'


class Groovy(SoftTech):
    def search_term(self):
        return 'groovy'


class VisualBasic(SoftTech):
    def search_term(self):
        return 'visual basic'


class Delphi(SoftTech):
    def search_term(self):
        return 'delphi'


class Dart(SoftTech):
    def search_term(self):
        return 'dart'


class Julia(SoftTech):
    def search_term(self):
        return 'julia'


class Clojure(SoftTech):
    def search_term(self):
        return 'clojure'


class VBA(SoftTech):
    def search_term(self):
        return 'vba'


class Bash(SoftTech):
    def search_term(self):
        return 'bash'


# 2. CREATE DATABASE
tech_obj_list= []
cities = ("all", "sofia", 'plovdiv', 'varna', 'burgas', 'stara zagora', 'ruse')
technologies = ('python', 'javascript', 'php', 'java',
                'c++', 'c#', 'swift', 'objectc', '.net',
                'rust', 'ruby', 'kotlin', 'typescript',
                'coffeescript', 'perl', 'webassembly', 'sql',
                'html', 'css', 'go', 'scala',
                'haskell', 'erlang', 'elexir', 'matlab',
                'groovy', 'visual basic', 'delphi', 'dart',
                'julia', "clojure", 'vba', 'bash',)

for tech in technologies:
    new_obj = None
    if tech == "python":
        new_obj = Python()
    elif tech == 'javascript':
        new_obj = JavaScript()
    elif tech == 'php':
        new_obj = PHP()
    elif tech == 'java':
        new_obj = Java()
    elif tech == 'c++':
        new_obj = CPlus()
    elif tech == 'c#':
        new_obj = CSharp()
    elif tech == 'swift':
        new_obj = Swift()
    elif tech == 'objectc':
        new_obj = ObjectC()
    elif tech == '.net':
        new_obj = DotNet()
    elif tech == 'rust':
        new_obj = Rust()
    elif tech == 'rugy':
        new_obj = Ruby()
    elif tech == 'kotlin':
        new_obj = Kotlin()
    elif tech == 'typescript':
        new_obj = TypeScript()
    elif tech == 'coffeescript':
        new_obj = CoffeeScript()
    elif tech == 'perl':
        new_obj = Perl()
    elif tech == 'webassembly':
        new_obj = WebAssembly()
    elif tech == 'sql':
        new_obj = SQL()
    elif tech == 'html':
        new_obj = HTML()
    elif tech == 'css':
        new_obj = CSS()
    elif tech == 'go':
        new_obj = Go()
    elif tech == 'scala':
        new_obj = Scala()
    elif tech == 'haskell':
        new_obj = Haskell()
    elif tech == 'erlang':
        new_obj = Erlang()
    elif tech == 'elexir':
        new_obj = Elexir()
    elif tech == 'matlab':
        new_obj = Matlab()
    elif tech == 'groovy':
        new_obj = Groovy()
    elif tech == 'visual basic':
        new_obj = VisualBasic()
    elif tech == 'delphi':
        new_obj = Delphi()
    elif tech == 'dart':
        new_obj = Dart()
    elif tech == 'julia':
        new_obj = Julia()
    elif tech == 'clojure':
        new_obj = Clojure()
    elif tech == 'vba':
        new_obj = VBA()
    elif tech == 'bash':
        new_obj = Bash()
    if new_obj is not None:
        tech_obj_list.append(new_obj)

# 3. GO TO JOBS.BG

for town in range(1):
    for obj in tech_obj_list:
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
        print(text[-1])
