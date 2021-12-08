import requests
from bs4 import BeautifulSoup

def icd9_to_icd10(icd9_code:str):
    # Could add ways to deal with input being not valid icd9
    base_url = "https://www.icd10data.com/Convert/"
    response = requests.get(base_url + str(icd9_code))
    soup = BeautifulSoup(response.content, 'html.parser')
    identifier_spans = soup.select(".ulConversion .identifier")
    parsed_codes = [i.text for i in identifier_spans]
    return parsed_codes    

def example():
    print(icd9_to_icd10("00.01"))