from bs4 import BeautifulSoup

with open('data/gitsid.html', 'r') as f:
    doc = f.read()

soup = BeautifulSoup(doc, 'html.parser')

# print(soup.div)

# for a in soup.find_all('a'):
#     print(a.get('href'))


# print(soup.find_all('div')[0].text)

# for div in soup.find_all('div') :
#     print(div.text)


# for link in soup.find('div', class_='links').findChildren('a'):
#     print(link.get('href'))


#gets you all the text from the page
data = soup.get_text()

# as we are getting the data like spaced over spaced right, so we can use regex
data = ' '.join(data.split())
with open('scrapedData/gitdata.txt', 'w') as f:
    f.write(data)