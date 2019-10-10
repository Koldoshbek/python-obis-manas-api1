import requests
from bs4 import BeautifulSoup

url = 'http://obis.manas.edu.kg/'


def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find('table', class_='bgc9').find('tr').find('td').find_all('input')
    for i in links:
        print(str(i.get('onclick')).split('?')[1].replace("'", ''))
    return links


data = {
    'frm_kullanici': '1604.01028',
    'frm_sifre': 'Koldoshbek'
}
r = requests.post(url=url, data=data)

if __name__ == '__main__':
    get_all_links(r.text)
