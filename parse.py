import requests
from bs4 import BeautifulSoup
import courses

url = 'http://obis.manas.edu.kg/'


def get_all_links(html):
    list_of_menus = []
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find('table', class_='bgc9').find('tr').find('td').find_all('input')
    for i in links:
        list_of_menus.append(
            'http://obis.manas.edu.kg/index.php?' + str(i.get('onclick')).split('?')[1].replace("'", ''))
    return list_of_menus


def to_dict(all_links):
    result = {}

    result['menu'] = all_links[0]
    result['info'] = all_links[1]
    result['courses'] = all_links[2]
    result['notes'] = all_links[3]
    result['transcripts'] = all_links[4]
    result['reference'] = all_links[5]
    result['change_password'] = all_links[6]
    result['exit'] = all_links[7]
    get_info(result['info'])
    print(courses.get_courses((result['courses'])))
    print(result)
    return result


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


data = {
    'frm_kullanici': '1604.01028',
    'frm_sifre': 'Koldoshbek'
}
r = requests.post(url=url, data=data)

if __name__ == '__main__':
    to_dict(get_all_links(r.text))
