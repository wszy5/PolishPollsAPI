import requests
from bs4 import BeautifulSoup as soup
import pandas as pd


def parse_float(number):
    try:
        return float(number)
    except:
        return(0.0)


def fetch_polls() -> pd.DataFrame:
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

            parties = poll.find_all("div",{"class":"section_polls_data"})
            result['lewica'] = parse_float(parties[0].text)
            result['ko'] = parse_float(parties[1].text)
            result['p2050'] = parse_float(parties[2].text)
            result['psl'] = parse_float(parties[3].text)
            result['ap'] = parse_float(parties[4].text)
            result['w'] = parse_float(parties[5].text)
            result['pis'] = parse_float(parties[6].text)
            result['konfa'] = parse_float(parties[7].text)
                        
            responses.append(result)
        except:
            continue
    return(pd.DataFrame(responses))
