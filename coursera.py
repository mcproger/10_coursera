import requests
from lxml import html
from bs4 import BeautifulSoup


def get_courses_list(course_list_page_url):
    course_list_page = requests.get(course_list_page_url)
    html_content = html.fromstring(course_list_page.content)
    course_list = html_content.xpath('//url/loc/text()')
    return course_list[:20]


def get_course_info(course_slug):
    pass


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    course_list_page_url = 'https://www.coursera.org/sitemap~www~courses.xml'
    course_list = get_courses_list(course_list_page_url)
    for course in course_list:
        course_page = requests.get(course)
        soup = BeautifulSoup(course_page.content, 'html.parser')
        title_of_course = soup.find('h1', class_='title display-3-text').get_text()
        print(title_of_course)
