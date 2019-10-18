import requests
from bs4 import BeautifulSoup

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
    get_courses(result['courses'])
    print(result)
    return result


def get_info(data):
    about_info = {}
    soup = BeautifulSoup(get_html(data), 'lxml')
    info = soup.find('table', class_='bgc15').find_all('td')
    about_info['st_number'] = info[2].next
    about_info['first_name'] = info[4].next.replace('Þ', 'Ş').replace('Ý', 'I')
    about_info['last_name'] = info[6].next.replace('Þ', 'Ş').replace('Ý', 'I')
    about_info['region'] = info[8].next.replace('Þ', 'Ş')
    about_info['date_of_birth'] = info[10].next
    about_info['name_of_father'] = info[12].next.replace('Ý', 'I')
    about_info['name_of_mother'] = info[14].next.replace('Ý', 'I')
    return about_info


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
        about_courses[code]['theory'] = str(i.find_all('td')[5].next).replace('<br>','').replace('</br>','')
        about_courses[code]['practice'] = str(i.find_all('td')[6].next).replace('<br>','').replace('</br>','')
        about_courses[code]['T(30%)'] = i.find_all('td')[7].next
        about_courses[code]['U(20%)'] = i.find_all('td')[8].next
    return about_courses


def get_html(url):
    r = requests.get(url)
    return r.text


data = {
    'frm_kullanici': '1604.01028',
    'frm_sifre': 'Koldoshbek'
}
r = requests.post(url=url, data=data)

if __name__ == '__main__':
    to_dict(get_all_links(r.text))
