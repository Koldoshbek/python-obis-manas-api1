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


data = {
    'frm_kullanici': '1604.01028',
    'frm_sifre': 'Koldoshbek'
}
r = requests.post(url=url, data=data)


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
    return result


if __name__ == '__main__':
    print(to_dict(get_all_links(r.text)))
