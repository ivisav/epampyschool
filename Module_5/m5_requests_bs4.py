import requests
from bs4 import BeautifulSoup

# Requests will get data for us, BeautifulSoup will get data from page, based on tags

r = requests.Session()
data = r.get(f"http://www.lexicons.ru/old/l/latin/lat-rus-m.html")
print(data.status_code)     # page response code
# data.encoding = "windows-1251" # you can change encoding if needed
soup = BeautifulSoup(data.text, 'html.parser')
for tables in soup.find_all('li'):
    print(tables.get_text())
