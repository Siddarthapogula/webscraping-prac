
from bs4 import BeautifulSoup

# changing the things in the html

with open('sample.html', 'r') as f:
    doc = f.read()

soup = BeautifulSoup(doc, 'html.parser')

# print(soup.prettify())

cont = soup.find('div', class_='links')
cont.name = 'span'


with open('modifiedsample.html', 'w') as f:
    f.write(soup.prettify())

print(soup)