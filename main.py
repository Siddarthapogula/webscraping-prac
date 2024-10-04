import requests

url = 'https://github.com/Siddarthapogula/webscraping-prac'

def fetchDataAndWriteToFile(url, path):
    resp = requests.get(url)
    with open(path, 'w') as f:
        f.write(resp.text)
    return

fetchDataAndWriteToFile(url, 'data/gitsid.html')
