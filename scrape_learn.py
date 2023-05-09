from bs4 import BeautifulSoup
import requests
import csv

html_file = requests.get('https://coreyms.com/').text

Soup = BeautifulSoup(html_file, 'lxml')

csv_file = open('wbscrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Video_link', 'Date_posted'])

Headers = Soup.find_all('header', class_ = "entry-header")
for header in Headers:
    Content = Soup.find('div', class_ = "entry-content")
    Title = header.find('h2', class_ = "entry-title").text
    Date_posted = header.p.time.text
    summary = Content.p.text
    try:   
        Video_link = Content.span.iframe['src']
    except Exception as e:
        Video_link = None


    print(f"{Title}")
    print(f"Summary: {summary}")
    print(f"Video link: {Video_link}")
    print(f"{Date_posted}")
    print("")
    csv_writer.writerow([Title, summary, Video_link, Date_posted])

csv_file.close()