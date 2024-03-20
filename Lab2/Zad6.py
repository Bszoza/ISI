#!/usr/bin/env python3

import cloudscraper
from bs4 import BeautifulSoup

LINK = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing"

class Home:
	def __init__(self, header_name, price, price_for_m2):
		self.header_name = header_name
		self.price = price
		self.price_for_m2 = price_for_m2

	def __str__(self):
		return f"Nazwa:{self.header_name}, Cena:{self.price}, Cena za metr: {self.price_for_m2}"

def daj_html_z_linku(link):
	sc = cloudscraper.create_scraper()
	return sc.get(link).text

soup = BeautifulSoup(daj_html_z_linku(LINK), 'html.parser')

homes = []

for listing_item in soup.find_all('article', attrs={"data-cy": "listing-item"}):
	header_name = listing_item.find('p', attrs={"data-cy": "listing-item-title"}).text
	header_content = listing_item.find('div', attrs={"data-testid": "listing-item-header"})
	span = header_content.find('span', class_="css-1uwck7i e1a3ad6s0")
	if span is None or span.text.strip() == "Zapytaj o cenę":
		continue

	price = span.contents[0].strip()
	price = price.replace("zł", "")
	price_per_meter = span.find('span', class_="css-v14eu1 e1a3ad6s1").text.strip()
	price_per_meter = price_per_meter.replace("zł/m²", "")

	homes.append(Home(header_name, price, price_per_meter))


for home in homes:
	print(home)

