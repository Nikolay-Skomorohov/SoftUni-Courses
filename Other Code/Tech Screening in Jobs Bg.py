"""
Program: Tech Screening in Jobs Bg.py
Author: Nikolay Skomorohov

The script searches jobs.bg for the numbers of mentions per software technology.
The goal is to have a rough approximation of techs demand.

1. Imports and class creation
2. Power up selenium driver
3. Create IT class instances
4. Go to jobs.bg and loop over cities and techs
5. Create file with the data

"""
import csv
from time import time
from selenium import webdriver


class SoftTech:
    def __init__(self):
        self.all = 0
        self.sofia = 0
        self.plovdiv = 0

    def add_to_city(self, city: str, value: int):
        if city == "all":
            self.all += value
        if city == "sofia":
            self.sofia += value
        elif city == "plovdiv":
            self.plovdiv += value


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
        return 'Python'


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
        return 'JavaScript'


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
        return 'PHP'


class Java(SoftTech):
    def __init__(self):
        super().__init__()
        self.spring = 0

    def add_to_framework(self, frame: str, value: int):
        if frame in "spring":
            self.spring += value

    @staticmethod
    def search_term():
        return 'Java'


class CPlus(SoftTech):
    @staticmethod
    def search_term():
        return 'C++'


class CSharp(SoftTech):
    @staticmethod
    def search_term():
        return 'C#'


class Swift(SoftTech):
    @staticmethod
    def search_term():
        return 'Swift'


class Rust(SoftTech):
    @staticmethod
    def search_term():
        return 'Rust'


class Ruby(SoftTech):
    def __init__(self):
        super().__init__()
        self.ruby_on_rails = 0

    def add_to_framework(self, frame: str, value: int):
        if frame in "ruby on rails":
            self.ruby_on_rails += value

    @staticmethod
    def search_term():
        return 'Ruby'


class Kotlin(SoftTech):
    @staticmethod
    def search_term():
        return 'Kotlin'


class TypeScript(SoftTech):
    @staticmethod
    def search_term():
        return 'TypeScript'


class CoffeeScript(SoftTech):
    @staticmethod
    def search_term():
        return 'CoffeeScript'


class Perl(SoftTech):
    @staticmethod
    def search_term():
        return 'Perl'


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
        return 'SQL'


class HTML(SoftTech):
    @staticmethod
    def search_term():
        return 'HTML'


class CSS(SoftTech):
    @staticmethod
    def search_term():
        return 'CSS'


class Go(SoftTech):
    @staticmethod
    def search_term():
        return 'Goland'


class Haskell(SoftTech):
    @staticmethod
    def search_term():
        return 'Haskel'


class Erlang(SoftTech):
    @staticmethod
    def search_term():
        return 'Erlang'


class Elixir(SoftTech):
    @staticmethod
    def search_term():
        return 'Elixir'


class Matlab(SoftTech):
    @staticmethod
    def search_term():
        return 'Matlab'


class Groovy(SoftTech):
    @staticmethod
    def search_term():
        return 'Groovy'


class VisualBasic(SoftTech):
    @staticmethod
    def search_term():
        return 'Visual Basic'


class Delphi(SoftTech):
    @staticmethod
    def search_term():
        return 'Delphi'


class Dart(SoftTech):
    @staticmethod
    def search_term():
        return 'Dart'


class Julia(SoftTech):
    @staticmethod
    def search_term():
        return 'Julia'


class Clojure(SoftTech):
    @staticmethod
    def search_term():
        return 'Clojure'


class VBA(SoftTech):
    @staticmethod
    def search_term():
        return 'VBA'


class Bash(SoftTech):
    @staticmethod
    def search_term():
        return 'Bash'


def language_object_creation():
    """Creates a list with object representations for each IT tech"""
    technologies = ('Python', 'JavaScript', 'PHP',
                    'C++', 'C#', 'Swift', 'Rust', 'Dart',
                    'Ruby', 'Kotlin', 'Typescript',
                    'CoffeeScript', 'Perl', 'SQL', 'Java',
                    'HTML', 'CSS', 'Golang', 'Matlab',
                    'Haskel', 'Erlang', 'Elixir',
                    'Groovy', 'Visual Basic', 'Delphi',
                    'Julia', "Clojure", 'VBA', 'Bash')

    tech_obj_list = []
    for tech in technologies:
        new_obj = None
        if tech == "Python":
            new_obj = Python()
        elif tech == 'JavaScript':
            new_obj = JavaScript()
        elif tech == 'PHP':
            new_obj = PHP()
        elif tech == 'Java':
            new_obj = Java()
        elif tech == 'C++':
            new_obj = CPlus()
        elif tech == 'C#':
            new_obj = CSharp()
        elif tech == 'Swift':
            new_obj = Swift()
        elif tech == 'Rust':
            new_obj = Rust()
        elif tech == 'Ruby':
            new_obj = Ruby()
        elif tech == 'Kotlin':
            new_obj = Kotlin()
        elif tech == 'TypeScript':
            new_obj = TypeScript()
        elif tech == 'CoffeeScript':
            new_obj = CoffeeScript()
        elif tech == 'Perl':
            new_obj = Perl()
        elif tech == 'SQL':
            new_obj = SQL()
        elif tech == 'HTML':
            new_obj = HTML()
        elif tech == 'CSS':
            new_obj = CSS()
        elif tech == 'Golang':
            new_obj = Go()
        elif tech == 'Haskel':
            new_obj = Haskell()
        elif tech == 'Erlang':
            new_obj = Erlang()
        elif tech == 'Elixir':
            new_obj = Elixir()
        elif tech == 'Matlab':
            new_obj = Matlab()
        elif tech == 'Groovy':
            new_obj = Groovy()
        elif tech == 'Visual Basic':
            new_obj = VisualBasic()
        elif tech == 'Delphi':
            new_obj = Delphi()
        elif tech == 'Dart':
            new_obj = Dart()
        elif tech == 'Julia':
            new_obj = Julia()
        elif tech == 'Clojure':
            new_obj = Clojure()
        elif tech == 'VBA':
            new_obj = VBA()
        elif tech == 'Bash':
            new_obj = Bash()
        if new_obj is not None:
            tech_obj_list.append(new_obj)
    return tech_obj_list


def initiate_web_driver():
    """Powers up the Firefox browser in hidden mode and passes it with return"""
    gecko_driver = 'C:\\geckodriver.exe'
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    browser = webdriver.Firefox(executable_path=gecko_driver, options=options)
    return browser


def get_data_for_techs():
    """Calls 'initiate_web_driver' and 'language_object_creation'
     functions, then instructs the driver to go to jobs.bg and
     loop over each city and IT tech. Creates csv with a function call
     to 'create_csv_file_with_results' and prints data with 'print_data' call"""
    locations = ({'all': 'Всички'}, {'sofia': "София"}, {'plovdiv': 'Пловдив'})
    browser = initiate_web_driver()
    tech_obj_list = language_object_creation()

    for location in locations:
        location_bg = list(location.items())
        for obj_from_tech_list in tech_obj_list:
            browser.get('http://jobs.bg')

            city_tab = browser.find_element_by_xpath('//*[@id="location"]')
            city_tab.click()
            city_tab.send_keys(location_bg[0][1])

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
            obj_from_tech_list.add_to_city(location_bg[0][0], int(result_text[-1]))
            browser.get('http://jobs.bg')

    browser.quit()
    create_csv_file_with_results(tech_obj_list)
    print_results(tech_obj_list)


def print_results(tech_obj_list: list):
    """Print the lists with results produced by the get_data_for_techs function"""
    for obj_to_print in tech_obj_list:
        print(f"{obj_to_print.search_term()} has the following number of mentions in job listings:")
        print(f" - BG total: {obj_to_print.all} mentions.")
        print(f" - Sofia: {obj_to_print.sofia} mentions.")
        print(f" - Plovdiv: {obj_to_print.plovdiv} mentions.")
        print("-" * 65)


def create_csv_file_with_results(tech_obj_list: list):
    with open('C:\\Users\\Huskarl\\Desktop\\Tech_Mentions_Jobs_August_2019.csv', "w", newline='') as filename:
        file_write = csv.writer(filename, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_write.writerow(['Tech', 'BG Total', 'Sofia', 'Plovdiv'])
        for obj in tech_obj_list:
            file_write.writerow([str(obj.search_term()), obj.all, obj.sofia, obj.plovdiv])


def main():
    start_time = time()
    get_data_for_techs()
    end_time = time()
    print(f"The program finished in {(end_time - start_time) // 60:.0f}"
          f" minutes and {((end_time - start_time) % 60):.0f} seconds.")


if __name__ == "__main__":
    main()
