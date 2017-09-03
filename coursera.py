import requests
import argparse
from lxml import html
from bs4 import BeautifulSoup
from openpyxl import Workbook


def get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('course_quant', type=int)
    parser.add_argument('filepath', type=str,
                        help='Filepath for result course info file')
    args = parser.parse_args()
    return args


def get_courses_list(course_list_page_url, course_quant):
    course_list_page = requests.get(course_list_page_url)
    html_content = html.fromstring(course_list_page.content)
    course_list = html_content.xpath('//url/loc/text()')
    return course_list[:course_quant]


def get_course_info_tags(soup):
    course_info_tags = {
        'title_of_course': soup.find('h1', class_='title display-3-text'),
        'language_of_course': soup.find('div', class_='language-info'),
        'start_of_course': soup.find('div', class_='startdate'),
        'rating_of_course': soup.find('div', class_='ratings-text bt3-visible-xs')
    }
    return course_info_tags


def get_course_countinuance(soup):
    course_continuance = soup.find_all(
        'div', class_='week-heading body-2-text')
    return len(course_continuance)


def get_course_info(course_page):
    soup = BeautifulSoup(course_page.content, 'html.parser')
    course_info_tags = get_course_info_tags(soup)
    course_info = {}
    for tag, tag_info in course_info_tags.items():
        course_info[tag] = tag_info.get_text() if tag_info else None
    course_info['continuance_of_course'] = get_course_countinuance(soup)
    return course_info


def output_courses_info_to_xlsx(work_book, work_sheet, courses, filepath):
    for course in courses:
        work_sheet.append(list(course.values()))
    work_book.save(filepath)
    return None


if __name__ == '__main__':
    args = get_argparser()
    course_list_page_url = 'https://www.coursera.org/sitemap~www~courses.xml'
    course_list = get_courses_list(course_list_page_url, args.course_quant)
    courses = []
    for course in course_list:
        course_page = requests.get(course)
        courses.append(get_course_info(course_page))
    work_book = Workbook()
    work_sheet = work_book.active
    course_info_xlsx = output_courses_info_to_xlsx(
        work_book, work_sheet, courses, args.filepath)
