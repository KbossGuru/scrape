import requests
from bs4 import BeautifulSoup



html_file = requests.get(f"https://www.indiacode.nic.in/simple-search?query=&sort_by=score&order=desc&rpp=100&etal=0&start={pages}").text
            
Soup = BeautifulSoup(html_file, "lxml")

table= Soup.find('table', class_= "table table-hover")

for rows in table.find_all('tr'):
    for title in rows.find_all('td', class_ = "evenRowEvenCol"):
        if title['headers']==['t3']:
        print(title.text)
            

