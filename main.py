import requests
from bs4 import BeautifulSoup as soup

URL = "https://ewybory.eu/sondaze/polska/"

website = requests.get(URL)

if website.status_code != 200:
    print(f"Błąd strony źródłowej! Serwer zwrócił błąd {website.status_code}")

content = soup(website.content,'html.parser')

polls = content.find_all("div",{"class":"section_polls_row"})[1:]

for poll in polls:
    results = {}
    try:
        date = poll.find("div",{"class":"section_polls_term"}).text
        results['date'] = date
        company = poll.find("a").text
        results['company'] = company
        sample = poll.find("div",{"class":"section_polls_sample desktop"}).text
        results['sample'] = sample
        details = {}
        parties = poll.find_all("div")[4:]
        for party in parties:
            details['pis'] = ""
            pass
    except:
        continue
