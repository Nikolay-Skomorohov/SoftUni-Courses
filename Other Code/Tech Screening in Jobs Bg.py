"""
Program: Tech Screening in Jobs Bg.py
Author: Nikolay Skomorohov

The script searches jobs.bg for the numbers of mentions per software technology.
The goal is to have a rough(!) approximation of techs relevance in the jobs market.
Results should be takes with a grain of salt, the jobs.bg search engine is underwhelming.
Quantifying actual demand is much harder!

1. Imports and class creation
2. Power up selenium driver with 'initiate_web_driver()'
3. Create IT class instances with 'language_object_creation()'
4. Go to jobs.bg and loop over cities and techs with 'get_data_for_techs()'
5. Create file with the data with 'create_csv_file_with_results()'
6. Prints the results with 'print_results()'

"""
import csv
import time
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
    @staticmethod
    def search_term():
        return 'Python'


class Django(SoftTech):
    @staticmethod
    def search_term():
        return 'Django'


class Flask(SoftTech):
    @staticmethod
    def search_term():
        return 'Flask'


class Scrapy(SoftTech):
    @staticmethod
    def search_term():
        return 'Scrapy'


class JavaScript(SoftTech):
    @staticmethod
    def search_term():
        return 'JavaScript'


class React(SoftTech):
    @staticmethod
    def search_term():
        return 'React'


class Angular(SoftTech):
    @staticmethod
    def search_term():
        return 'Angular'


class Vue(SoftTech):
    @staticmethod
    def search_term():
        return 'Vue'


class Node(SoftTech):
    @staticmethod
    def search_term():
        return 'Node'


class JQuery(SoftTech):
    @staticmethod
    def search_term():
        return 'jQuery'


class PHP(SoftTech):
    @staticmethod
    def search_term():
        return 'PHP'


class Java(SoftTech):
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


class Perl(SoftTech):
    @staticmethod
    def search_term():
        return 'Perl'


class SQL(SoftTech):
    @staticmethod
    def search_term():
        return 'SQL'


class MySQL(SoftTech):
    @staticmethod
    def search_term():
        return 'MySQL'


class NoSQL(SoftTech):
    @staticmethod
    def search_term():
        return 'NoSQL'


class PostgreSQL(SoftTech):
    @staticmethod
    def search_term():
        return 'PostgreSQL'


class MongoDB(SoftTech):
    @staticmethod
    def search_term():
        return 'MongoDB'


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


class GraphQL(SoftTech):
    @staticmethod
    def search_term():
        return 'GraphQL'


def language_object_creation():
    """Creates a list with object representations for each IT tech"""
    technologies = ('Python', 'Django', 'Flask', 'Scrapy', 'JavaScript',
                    'React', 'Angular', 'Vue', 'Node', 'jQuery', 'GraphQL',
                    'SQL', 'NoSQL', 'MySQL', 'PostreSQL', 'MongoDB', 'HTML',
                    'CSS', 'PHP', 'Java', 'C++', 'C#', 'Swift', 'TypeScript',
                    'Rust', 'Ruby', 'Kotlin', 'Golang', 'Dart', 'Julia',
                    'Haskel', 'Erlang', 'Elixir', 'Clojure', 'Groovy', 'VBA',
                    'Visual Basic', 'Delphi', 'Perl', 'Matlab', 'Bash')

    tech_obj_list = []
    for tech in technologies:
        new_obj = None
        if tech == "Python":
            new_obj = Python()
        elif tech == 'Django':
            new_obj = Django()
        elif tech == 'Flask':
            new_obj = Flask()
        elif tech == 'Scrapy':
            new_obj = Scrapy()
        elif tech == 'JavaScript':
            new_obj = JavaScript()
        elif tech == 'React':
            new_obj = React()
        elif tech == 'Angular':
            new_obj = Angular()
        elif tech == 'Vue':
            new_obj = Vue()
        elif tech == 'Node':
            new_obj = Node()
        elif tech == 'jQuery':
            new_obj = JQuery()
        elif tech == 'GraphQL':
            new_obj = GraphQL()
        elif tech == 'SQL':
            new_obj = SQL()
        elif tech == 'NoSQL':
            new_obj = NoSQL()
        elif tech == 'MySQL':
            new_obj = MySQL()
        elif tech == 'PostreSQL':
            new_obj = PostgreSQL()
        elif tech == 'MongoDB':
            new_obj = MongoDB()
        elif tech == 'HTML':
            new_obj = HTML()
        elif tech == 'CSS':
            new_obj = CSS()
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
        elif tech == 'TypeScript':
            new_obj = TypeScript()
        elif tech == 'Rust':
            new_obj = Rust()
        elif tech == 'Ruby':
            new_obj = Ruby()
        elif tech == 'Kotlin':
            new_obj = Kotlin()
        elif tech == 'Perl':
            new_obj = Perl()
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
        elif tech == 'VBA':
            new_obj = VBA()
        elif tech == 'Delphi':
            new_obj = Delphi()
        elif tech == 'Dart':
            new_obj = Dart()
        elif tech == 'Julia':
            new_obj = Julia()
        elif tech == 'Clojure':
            new_obj = Clojure()
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
    current_date = time.strftime("%d_%b_%Y")
    with open(f'Tech_Mentions_JobsBG_{current_date}.csv', "w", newline='') as filename:
        file_write = csv.writer(filename, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_write.writerow(['Tech', 'BG Total', 'Sofia', 'Plovdiv'])
        for obj in tech_obj_list:
            file_write.writerow([str(obj.search_term()), obj.all, obj.sofia, obj.plovdiv])


def main():
    start_time = time.time()
    get_data_for_techs()
    end_time = time.time()
    print(f"The program finished in {(end_time - start_time) // 60:.0f}"
          f" minutes and {((end_time - start_time) % 60):.0f} seconds.")


if __name__ == "__main__":
    main()
