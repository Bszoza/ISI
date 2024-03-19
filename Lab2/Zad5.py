from bs4 import BeautifulSoup
import requests


def daj_html_z_linku(LINK):
    response = requests.get(LINK)
    if response.status_code == 200:
        return response.text
    return None


soup = BeautifulSoup(daj_html_z_linku("https://beautiful-soup-4.readthedocs.io/en/latest/#)"), 'html.parser')

tablica_z_linkami = []

for link in soup.find_all('a', href=True):
    tablica_z_linkami.append(link['href'])

print(tablica_z_linkami)

#Zwraca blad 403 nie wiem jak to naprawic na ten moment