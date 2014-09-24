import requests
from bs4 import BeautifulSoup

url = "http://www.intelligent-artifice.com/"

r = requests.get(url)

soup = BeautifulSoup(r.text)

print soup.get_text().encode('ascii', 'replace')
