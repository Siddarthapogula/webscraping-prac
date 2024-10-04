from bs4 import BeautifulSoup

with open('sample.html', 'r') as f:
    doc = f.read()

soup = BeautifulSoup(doc, 'html.parser')

print(soup.prettify())

# creaing new tags and appending it to the html source

ultag = soup.new_tag('ul')

litag1 = soup.new_tag('li')
litag1.string = 'Home'

litag2 = soup.new_tag('li')
litag2.string = 'About'

ultag.append(litag1)
ultag.append(litag2)

divoflinks = soup.find('div', class_='links')
# divoflinks.append(ultag)
divoflinks.extend(ultag)
print(soup)


with open ('modifiedsample.html', 'w') as f:
    f.write(soup.prettify())