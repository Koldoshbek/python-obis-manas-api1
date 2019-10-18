import requests
from bs4 import BeautifulSoup
import courses

def get_info(data):
    about_info = {}
    soup = BeautifulSoup(courses.get_html(data), 'lxml')
    info = soup.find('table', class_='bgc15').find_all('td')
    about_info['st_number'] = info[2].next
    about_info['first_name'] = info[4].next.replace('Þ', 'Ş').replace('Ý', 'I')
    about_info['last_name'] = info[6].next.replace('Þ', 'Ş').replace('Ý', 'I')
    about_info['region'] = info[8].next.replace('Þ', 'Ş')
    about_info['date_of_birth'] = info[10].next
    about_info['name_of_father'] = info[12].next.replace('Ý', 'I')
    about_info['name_of_mother'] = info[14].next.replace('Ý', 'I')
    return about_info
