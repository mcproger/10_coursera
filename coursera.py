import requests
from lxml import html
from bs4 import BeautifulSoup


def get_courses_list(course_list_page_url):
    course_list_page = requests.get(course_list_page_url)
    html_content = html.fromstring(course_list_page.content)
    course_list = html_content.xpath('//url/loc/text()')
    return course_list[:20]


def get_course_info(course_list):
    for course in course_list:
        course_page = requests.get(course)
        soup = BeautifulSoup(course_page.content, 'html.parser')
        title_of_course = soup.find('h1', class_='title display-3-text').get_text()
        language_of_course = soup.find('div', class_='language-info').get_text()
    

def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    course_list_page_url = 'https://www.coursera.org/sitemap~www~courses.xml'
    course_list = get_courses_list(course_list_page_url)
    course = course_list[0]
    course_page = requests.get(course)
    soup = BeautifulSoup(course_page.content, 'html.parser')
    #title_of_course = soup.find('h1', class_='title display-3-text').get_text()
    #table = soup.find('table', class_='basic-info-table bt3-table bt3-table-striped bt3-table-bordered bt3-table-responsive')
    print(table)


#<table class="basic-info-table bt3-table bt3-table-striped bt3-table-bordered bt3-table-responsive" data-reactid="148"><tbody data-reactid="149"><tr data-reactid="150"><td data-reactid="151"><i class="cif-clock" data-reactid="152"></i><span class="td-title" data-reactid="153">Выполнение</span></td><td class="td-data" data-reactid="154">от 4 до 8 часов в неделю</td></tr><tr data-reactid="155"><td data-reactid="156"><i class="cif-language" data-reactid="157"></i><span class="td-title" data-reactid="158">Язык</span></td><td class="td-data" data-reactid="159"><div class="language-info" data-reactid="160"><div class="rc-Language" data-reactid="161"><!-- react-text: 162 -->English<!-- /react-text --><span data-reactid="163"><span data-reactid="164">, </span><strong data-reactid="165">Субтитры: </strong><!-- react-text: 166 -->Ukrainian, Chinese (Simplified), Portuguese (Brazilian), Vietnamese, Russian, Turkish, Spanish, Kazakh<!-- /react-text --></span></div></div></td></tr><tr data-reactid="167"><td data-reactid="168"><i class="cif-graduation-hat i-how-to-pass" data-reactid="169"></i><span class="td-title" data-reactid="170">Как пройти курс</span></td><td class="td-data" data-reactid="171">Чтобы пройти курс, выполните все оцениваемые задания.</td></tr></tbody></table>