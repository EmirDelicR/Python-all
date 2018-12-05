from urllib import request
from bs4 import BeautifulSoup
import os
import re
from filereader.index import File


class Crawler:
    """
        Crawl specific web sate to fetch content:
        Use:
        cr = Crawler()
        cr.crawl_website('https://www.wikipedia.org')
        obj = cr.parse_html_content()
        # Can use just obj that is all website
        # Or use specific tag like (h1, h2)
        cr.write_data(obj.title, 'wiki_titles.txt')
        cr.append_data(obj.title, 'wiki_titles.txt')
    """
    __html_content = ''
    __ABSOLUTE_PATH = os.path.dirname(__file__) + '/sites/'
    __NAME = ''

    def __init__(self):
        print('Crawler init')

    def __getitem__(self, name):
        return getattr(self, name)

    def crawl_website(self, url):
        """Specify web sites to fetch content url: string ('https://www.wikipedia.org') """
        try:
            self.__NAME = self.__extract_site_name(url)
            site = request.urlopen(url)
            self.__html_content = site.read()
        except ConnectionRefusedError as err:
            print(err)

    def parse_html_content(self):
        """Parse html content using BeautifulSoup"""
        bs_object = BeautifulSoup(self.__html_content, 'html.parser')
        return bs_object

    def __create_project_dir(self, dir_name):
        """Create directory """
        dir_name = dir_name.lower()
        path = self.__ABSOLUTE_PATH + dir_name
        if not os.path.exists(path):
            print('Creating directory ' + dir_name)
            os.makedirs(path)

    @staticmethod
    def __extract_site_name(url):
        """ extract sites name (https://www.wikipedia.org == wikipedia) """
        pattern = r'\..*\.'
        search_string = re.search(pattern, url)
        name = search_string.group().replace('.', '')
        return name

    def write_data(self, data, file_name):
        """Write data to file"""
        path = self.__set_path()
        file = File()
        file.write_to_file(path, data, file_name)

    def append_data(self, data, file_name):
        """Append data to file"""
        path = self.__set_path()
        file = File()
        file.append_to_file(path, data, file_name)

    def __set_path(self):
        """Set file path"""
        self.__create_project_dir(self.__NAME)
        path = self.__ABSOLUTE_PATH + self.__NAME + '/'
        return path




