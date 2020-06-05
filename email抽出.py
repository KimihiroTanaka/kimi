
from bs4 import BeautifulSoup as soup
import requests
d = soup(requests.get('http://acoustofluidics.pratt.duke.edu/acoustic-tweezers-0').text, 'html.parser')
email = d.find('div', {'class':'contactInformation'}).find_all('ul')[-2].find_all('li')[-1].text
