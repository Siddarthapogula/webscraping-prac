from bs4 import BeautifulSoup

with open('sample.html', 'r') as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')

print(soup.title.text)