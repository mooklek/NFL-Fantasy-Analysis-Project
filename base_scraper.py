from bs4 import BeautifulSoup
import requests
import csv

class statsScraper:

    base_url = f'https://www.pro-football-reference.com/years/2024/'

    def __init__(self) -> None:
        self.doc = None 

    def fetch_page(self, stat_type): 
        url = f'{self.base_url}{stat_type}.htm'
        result = requests.get(url)
        self.doc = BeautifulSoup(result.text, 'html.parser')

    def parse_rows(self):
        rows = self.doc.findAll('tr')
        return rows 
    
    def write_csv(self, fileName: str, data: list, ):
        with open(fileName + '.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Name', 'Team', 'Yards'])
            writer.writerows(data)

    


        

    

    