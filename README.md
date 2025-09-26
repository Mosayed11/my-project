
from bs4 import BeautifulSoup
import csv
import requests

date = input("inter the date here format: mm/dd/yyyy: ")
page = requests.get(f"https://www.yallakora.com/match-center/date={date}")

def main(page):
    src = page.content
    soup = BeautifulSoup(src, 'lxml')
    Matches_details = []
    frindlymatche = soup.find_all('div', {'class': 'matchCard'})
    # You can now process frindlymatche as needed
    get_match_details(frindlymatche)

def get_match_details(frindlymatches):
     
    frindlymatche_title = frindlymatches.content[1].find("h2").text.strip()

print(frindlymatche_title) # pyright: ignore[reportUndefinedVariable]
main(page)

