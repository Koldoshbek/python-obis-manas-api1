import requests
from bs4 import BeautifulSoup


def get_courses(data):
    about_courses = {}
    soup = BeautifulSoup(get_html(data), 'lxml')
    info = soup.find('table', class_='bgc15').find_all('tr', class_='bgc15')
    for i in info:
        code = i.find_all('td')[0].next.replace('&nbsp', '')
        about_courses[code] = {}
        about_courses[code]['name'] = i.find_all('td')[1].next.replace('&nbsp', '').replace('Ý', 'I').replace('Þ',
                                                                                                              'Ş').replace(
            'Ð', 'Ğ').replace('\xa0', '')
        about_courses[code]['T'] = i.find_all('td')[2].next.replace('&nbsp', '').replace('\xa0', '')
        about_courses[code]['U'] = i.find_all('td')[3].next.replace('&nbsp', '').replace('\xa0', '')
        about_courses[code]['credi'] = i.find_all('td')[4].next
        about_courses[code]['theory'] = str(i.find_all('td')[5].next).replace('<b>', '').replace('</b>', '')
        about_courses[code]['practice'] = str(i.find_all('td')[6].next).replace('<b>', '').replace('</b>', '')
        about_courses[code]['T(30%)'] = i.find_all('td')[7].next
        about_courses[code]['U(20%)'] = i.find_all('td')[8].next
    return about_courses


def get_html(url):
    r = requests.get(url)
    return r.text
