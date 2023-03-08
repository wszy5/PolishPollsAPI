import requests
from bs4 import BeautifulSoup as soup

URL = "https://ewybory.eu/sondaze/polska/"

website = requests.get(URL)

if website.status_code != 200:
    print(f"Błąd strony źródłowej! Serwer zwrócił błąd {website.status_code}")

content = soup(website.content,'html.parser')

polls = content.find_all("div",{"class":"section_polls_row"})[1:]

responses = []

for poll in polls:
    result = {}
    try:
        date = poll.find("div",{"class":"section_polls_term"}).text
        result['date'] = date

        company = poll.find("a").text
        result['company'] = company

        sample = poll.find("div",{"class":"section_polls_sample desktop"}).text
        result['sample'] = sample

        details = {}

        parties = poll.find_all("div",{"class":"section_polls_data"})
        details['lewica'] = parties[0].text
        details['ko'] = parties[1].text
        details['p2050'] = parties[2].text
        details['psl'] = parties[3].text
        details['ap'] = parties[4].text
        details['w'] = parties[5].text
        details['pis'] = parties[6].text
        details['konfa'] = parties[7].text
        
        result['details'] = details
        
        responses.append(result)
    except:
        continue
print(responses)
