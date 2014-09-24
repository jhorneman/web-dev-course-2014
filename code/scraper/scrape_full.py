import requests
from bs4 import BeautifulSoup

category_prefix = "category-"
author_prefix = "author-"

url = "http://www.intelligent-artifice.com/"

r = requests.get(url)

soup = BeautifulSoup(r.text)

for entry_post in soup.find_all('div', class_='hentry'):
	title = entry_post.find(class_='entry-title').get_text()

	classes = entry_post.attrs['class']

	category = "None"
	for v in classes:
		if v.startswith(category_prefix):
			category = v[len(category_prefix):]
			break

	author = "Unknown"
	for v in classes:
		if v.startswith(author_prefix):
			author = v[len(author_prefix):]
			break

	# category = next((v[len(category_prefix):] for v in classes if v.startswith(category_prefix)), "None")
	# author = next((v[len(author_prefix):] for v in classes if v.startswith(author_prefix)), "Unknown")

	print title.encode('ascii', 'replace')
	print "Category:", category, "- author:", author
