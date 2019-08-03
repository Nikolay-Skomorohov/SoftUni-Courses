"""
Program: Tech Screening in Jobs Bg.py
Author: Nikolay Skomorohov

The script searches jobs.bg for the numbers of mentions per software technology.
The goal is to have a rough approximation of techs demand.

1. Script setup
2. Create the database
3. Go to jobs.bg
4. Create a file with the results

"""

# 1. SCRIPT SETUP

from time import time
from selenium import webdriver


class SoftTech:
    def __init__(self):
        self.all = 0
        self.sofia = 0
        self.plovdiv = 0
        self.varna = 0
        self.burgas = 0
        self.stara_zagora = 0
        self.ruse = 0

    def add_to_city(self, city: str, value: int):
        if city == "all":
            self.all += value
        if city == "sofia":
            self.sofia += value
        elif city == "plovdiv":
            self.plovdiv += value
        elif city == "varna":
            self.varna += value
        elif city == "burgas":
            self.burgas += value
        elif city == "stara zagora":
            self.stara_zagora += value
        elif city == "ruse":
            self.ruse += value


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

    @staticmethod
    def search_term():
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

    @staticmethod
    def search_term():
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

    @staticmethod
    def search_term():
        return 'php'


class Java(SoftTech):
    def __init__(self):
        super().__init__()
        self.spring = 0

    def add_to_framework(self, frame: str, value: int):
        if frame in "spring":
            self.spring += value

    @staticmethod
    def search_term():
        return 'java'


class CPlus(SoftTech):
    @staticmethod
    def search_term():
        return 'c++'


class CSharp(SoftTech):
    @staticmethod
    def search_term():
        return 'c#'


class Swift(SoftTech):
    @staticmethod
    def search_term():
        return 'swift'


class ObjectiveC(SoftTech):
    @staticmethod
    def search_term():
        return 'objective c'


class DotNet(SoftTech):
    def __init__(self):
        super().__init__()
        self.aspnet = 0

    def add_to_framework(self, frame: str, value: int):
        if frame in "aspnet":
            self.aspnet += value

    @staticmethod
    def search_term():
        return '.net'


class Rust(SoftTech):
    @staticmethod
    def search_term():
        return 'rust'


class Ruby(SoftTech):
    def __init__(self):
        super().__init__()
        self.ruby_on_rails = 0

    def add_to_framework(self, frame: str, value: int):
        if frame in "ruby on rails":
            self.ruby_on_rails += value

    @staticmethod
    def search_term():
        return 'ruby'


class Kotlin(SoftTech):
    @staticmethod
    def search_term():
        return 'kotlin'


class TypeScript(SoftTech):
    @staticmethod
    def search_term():
        return 'typescript'


class CoffeeScript(SoftTech):
    @staticmethod
    def search_term():
        return 'coffeescript'


class Perl(SoftTech):
    @staticmethod
    def search_term():
        return 'perl'


class WebAssembly(SoftTech):
    @staticmethod
    def search_term():
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

    @staticmethod
    def search_term():
        return 'sql'


class HTML(SoftTech):
    @staticmethod
    def search_term():
        return 'html'


class CSS(SoftTech):
    @staticmethod
    def search_term():
        return 'css'


class Go(SoftTech):
    @staticmethod
    def search_term():
        return 'golang'


class Scala(SoftTech):
    @staticmethod
    def search_term():
        return 'scala'


class Haskell(SoftTech):
    @staticmethod
    def search_term():
        return 'haskell'


class Erlang(SoftTech):
    @staticmethod
    def search_term():
        return 'erlang'


class Elixir(SoftTech):
    @staticmethod
    def search_term():
        return 'elixir'


class Matlab(SoftTech):
    @staticmethod
    def search_term():
        return 'matlab'


class Groovy(SoftTech):
    @staticmethod
    def search_term():
        return 'groovy'


class VisualBasic(SoftTech):
    @staticmethod
    def search_term():
        return 'visual basic'


class Delphi(SoftTech):
    @staticmethod
    def search_term():
        return 'delphi'


class Dart(SoftTech):
    @staticmethod
    def search_term():
        return 'dart'


class Julia(SoftTech):
    @staticmethod
    def search_term():
        return 'julia'


class Clojure(SoftTech):
    @staticmethod
    def search_term():
        return 'clojure'


class VBA(SoftTech):
    @staticmethod
    def search_term():
        return 'vba'


class Bash(SoftTech):
    @staticmethod
    def search_term():
        return 'bash'


def language_object_creation():
    cities = ("all", "sofia", 'plovdiv', 'varna', 'burgas', 'stara zagora', 'ruse')
    technologies = ('python', 'javascript', 'php', 'java',
                    'c++', 'c#', 'swift', 'objectivec', '.net',
                    'rust', 'ruby', 'kotlin', 'typescript',
                    'coffeescript', 'perl', 'webassembly', 'sql',
                    'html', 'css', 'golang', 'scala',
                    'haskell', 'erlang', 'elixir', 'matlab',
                    'groovy', 'visual basic', 'delphi', 'dart',
                    'julia', "clojure", 'vba', 'bash',)

    tech_obj_list = []
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
        elif tech == 'objectivec':
            new_obj = ObjectiveC()
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
        elif tech == 'golang':
            new_obj = Go()
        elif tech == 'scala':
            new_obj = Scala()
        elif tech == 'haskel':
            new_obj = Haskell()
        elif tech == 'erlang':
            new_obj = Erlang()
        elif tech == 'elixir':
            new_obj = Elixir()
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
    return tech_obj_list


def initiate_web_driver():
    gecko_driver = 'C:\\geckodriver.exe'
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    browser = webdriver.Firefox(executable_path=gecko_driver, options=options)
    return browser


def get_data_for_techs():
    browser = initiate_web_driver()
    tech_obj_list = language_object_creation()

    for town in range(1):
        for obj_from_tech_list in tech_obj_list:
            if town != "all":
                pass
            else:
                pass
            browser.get('http://jobs.bg')
            open_keyword_tab = browser.find_element_by_xpath(
                "/html/body/table[2]/tbody/tr/td/table[2]/tbody/tr/td[1]/form/table/tbody/tr[7]/td/a/span[1]")
            open_keyword_tab.click()
            keyword_tab = browser.find_element_by_xpath('//*[@id="keyword"]')
            keyword_tab.click()
            input_keyword_tab = obj_from_tech_list.search_term()
            keyword_tab.send_keys(input_keyword_tab)
            add_keyword_button = browser.find_element_by_xpath('//*[@id="addKeywordLink"]')
            add_keyword_button.click()
            site_search_button = browser.find_element_by_xpath(
                '/html/body/table[2]/tbody/tr/td/table[2]/tbody/tr/td[1]/form/table/tbody/tr[12]/td/a')
            browser.implicitly_wait(1)
            site_search_button.click()
            try:
                pop_up_no_button = browser.find_element_by_xpath(
                    '/html/body/table[2]/tbody/tr/td/table[2]/tbody/tr/td[1]/form/table/tbody/tr[12]/td/div/div['
                    '2]/center/table/tbody/tr/td[2]/a')
                pop_up_no_button.click()
            except:
                pass
            search_result_count = browser.find_element_by_css_selector(
                "#search_results_div > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > "
                "table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1)")
            result_text = search_result_count.text.split()
            obj_from_tech_list.add_to_city("all", int(result_text[-1]))
            browser.get('http://jobs.bg')

    browser.quit()
    print_results(tech_obj_list)


def print_results(tech_obj_list: list):
    for obj_to_print in tech_obj_list:
        print(f"{obj_to_print.__class__.__name__}: {obj_to_print.all}")


def main():
    start_time = time()
    get_data_for_techs()
    end_time = time()
    print(f"The program finished in {(end_time - start_time) // 60:.0f}"
          f" minutes and {((end_time - start_time) % 60):.0f} seconds.")


if __name__ == "__main__":
    main()
