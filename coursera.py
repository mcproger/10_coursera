import requests
from lxml import html
from bs4 import BeautifulSoup
from openpyxl import Workbook


def get_courses_list(course_list_page_url):
    course_list_page = requests.get(course_list_page_url)
    html_content = html.fromstring(course_list_page.content)
    course_list = html_content.xpath('//url/loc/text()')
    return course_list[:20]


def make_course_info_tags(soup):
    course_info_tags = {
        'title_of_course': soup.find('h1', class_='title display-3-text'),
        'language_of_course': soup.find('div', class_='language-info'),
        'start_of_course': soup.find('div', class_='startdate'),
        'rating_of_course': soup.find('div', class_='ratings-text bt3-visible-xs')
    }
    return course_info_tags


def get_course_info(soup):
    course_info_tags = make_course_info_tags(soup)
    course_info = {}
    for course_tag, course_info_tag in course_info_tags.items():
        course_info[course_tag] = course_info_tag.get_text() if course_info_tag else None
    return course_info


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    course_list_page_url = 'https://www.coursera.org/sitemap~www~courses.xml'
    course_list = get_courses_list(course_list_page_url)
    courses = []
    for course in course_list:
        course_page = requests.get(course)
        soup = BeautifulSoup(course_page.content, 'html.parser')
        courses.append(get_course_info(soup))
    book = Workbook()
    sheet = book.active
    book.save("sample.xlsx")
