import requests
from lxml import html
from bs4 import BeautifulSoup


def get_courses_list(course_list_page_url):
    course_list_page = requests.get(course_list_page_url)
    html_content = html.fromstring(course_list_page.content)
    course_list = html_content.xpath('//url/loc/text()')
    return course_list[:20]


def get_html_parse_course_info(course_page, tag_name, class_name):
    soup = BeautifulSoup(course_page.content, 'html.parser')
    element = soup.find(tag_name, class_name)
    if not element:
        return None
    return element.get_text()


def get_course_info(course_list):
    for course in course_list:
        course_page = requests.get(course)
        title_of_course = get_html_parse_course_info(
            course_page, 'h1', 'title display-3-text')
        language_of_course = get_html_parse_course_info(
            course_page, 'div', 'language-info')
        start_date = get_html_parse_course_info(
            course_page, 'div', 'startdate')
        average_course_rating = get_html_parse_course_info(
            course_page, 'div', 'ratings-text bt3-visible-xs')
        course_continuance = get_html_parse_course_info(
            course_page, 'td', 'td-data')
    return title_of_course, language_of_course, start_date, average_course_rating, course_continuance


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    course_list_page_url = 'https://www.coursera.org/sitemap~www~courses.xml'
    course_list = get_courses_list(course_list_page_url)
    course = course_list[0]
    course_page = requests.get('https://www.coursera.org/learn/missing-data')
    soup = BeautifulSoup(course_page.content, 'html.parser')
    
    course_continuance = soup.find_all('div', class_='week-heading body-2-text')
    print(len(course_continuance))
    #print(get_course_info(course_list))
