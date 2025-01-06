from bs4 import BeautifulSoup
import requests
import csv

class statsScraper:

    '''url of the website we're scraping the data from with parameter cut off'''
    base_url = f'https://www.pro-football-reference.com/years/2024/'

    '''initializing the doc we're going to pull from'''
    def __init__(self) -> None:
        self.doc = None 

    '''fetching specific page in order to pull stats... passing, rushing, receiving'''
    def fetch_page(self, stat_type): 
        url = f'{self.base_url}{stat_type}.htm'
        result = requests.get(url)
        self.doc = BeautifulSoup(result.text, 'html.parser')

    '''parsing through the rows so we can find the tags with the data we want to take'''
    def parse_rows(self):
        rows = self.doc.findAll('tr')
        return rows 
    
    '''writing csv files with the data taken from the reference website'''
    def write_csv(self, fileName: str, csvRowNames: list, data: list):
        with open(fileName + '.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(csvRowNames)
            writer.writerows(data)
    
    '''finds any specific data stat that we want to take'''
    def find_stat(self, tag: str,stat_name: str):
        rows = self.parse_rows()
        compiledStat = []
        for row in rows:
            stats = row.findAll(tag, {'data-stat': stat_name})
            for index, stat in enumerate(stats):
                cleanStat = stat.text.strip()
                compiledStat.append(cleanStat)
        return compiledStat


    


        

    

    