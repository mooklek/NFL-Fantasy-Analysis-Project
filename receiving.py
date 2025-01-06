from bs4 import BeautifulSoup
import requests
from base_scraper import statsScraper
import csv

class receivingStats(statsScraper):
    def getStats(self):
        self.fetch_page('receiving')
        playerNames = []
        playerYards = []
        playerTeams = []
        playerRecs = []
        playerYpR = []
        playerTar = [] 
        playerTD = []

        table_tag = 'td'

        playerNames = self.find_stat(table_tag, 'name_display')
        playerTeams = self.find_stat(table_tag, 'team_name_abbr')
        playerYards = self.find_stat(table_tag, 'rec_yds')
        playerRecs = self.find_stat(table_tag, 'rec')
        playerYpR = self.find_stat(table_tag, 'rec_yds_per_rec')
        playerTar = self.find_stat(table_tag, 'targets')
        playerCatchPert = self.find_stat(table_tag, 'catch_pct')
        playerTD = self.find_stat(table_tag, 'rec_td')

        playerYards = playerYards[0:len(playerYards) - 1]
        
        sortedList = sorted(zip(playerNames, playerTeams, [int(x) for x in playerYards], playerRecs, playerTar, playerYpR, playerCatchPert, playerTD), key=lambda x: x[1], reverse = False) 

        for names, teams, yards, recs, targs, ypr, catchpert, touchdowns in sortedList: 
            print(f'{names}, {teams}, {yards}, {recs}, {targs}, {ypr}, {catchpert}, {touchdowns}')

        return sortedList  
    
