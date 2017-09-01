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


def get_course_countinuance(soup):
    course_continuance = soup.find_all('div', class_='week-heading body-2-text')
    return len(course_continuance)


def get_course_info(course_page):
    soup = BeautifulSoup(course_page.content, 'html.parser')
    course_info_tags = make_course_info_tags(soup)
    course_info = {}
    for tag, tag_info in course_info_tags.items():
        course_info[tag] = tag_info.get_text() if tag_info else None
    course_info['continuance_of_course'] = get_course_countinuance(soup)
    return course_info


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    course_list_page_url = 'https://www.coursera.org/sitemap~www~courses.xml'
    course_list = get_courses_list(course_list_page_url)
    courses = []
    for course in course_list:
        course_page = requests.get(course)
        courses.append(get_course_info(course_page))
    print(courses)
    
    book = Workbook()
    sheet = book.active
    book.save('')
