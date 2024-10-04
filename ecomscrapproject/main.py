import requests
from bs4 import BeautifulSoup
url = 'https://www.linkedin.com/in/varun-jillela-764478216/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'html.parser')

with open('data/blog.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())
print(soup.prettify())