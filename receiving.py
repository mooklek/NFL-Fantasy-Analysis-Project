from bs4 import BeautifulSoup
import requests
from base_scraper import statsScraper
import csv

class receivingStats(statsScraper):
    def getStats(self):

        '''inputs receiving parameter into fetch_page() function in order to get values from the website'''
        self.fetch_page('receiving') 

        '''initalizes lists for each value for each player'''
        playerNames = []
        playerYards = []
        playerTeams = []
        playerRecs = []
        playerYpR = []
        playerTar = [] 
        playerTD = []
        playerAge = []
        playerPos = []
        table_tag = 'td'

        '''scrapes website using the html tags given on the website'''
        playerNames = self.find_stat(table_tag, 'name_display')
        playerTeams = self.find_stat(table_tag, 'team_name_abbr')
        playerYards = self.find_stat(table_tag, 'rec_yds')
        playerRecs = self.find_stat(table_tag, 'rec')
        playerYpR = self.find_stat(table_tag, 'rec_yds_per_rec')
        playerTar = self.find_stat(table_tag, 'targets')
        playerCatchPert = self.find_stat(table_tag, 'catch_pct')
        playerTD = self.find_stat(table_tag, 'rec_td')
        playerAge = self.find_stat(table_tag, 'age')
        playerPos = self.find_stat(table_tag, 'pos')

        '''removes last row from playerYards because there's an empty row on the bottom of the website table'''
        playerYards = playerYards[0:len(playerYards) - 1]
        
        '''creating sortedList which includes all the data collected and is sorted by playerTeams first, playerYards second, then playerPos'''
        sortedList = sorted(zip(playerNames, playerTeams, 
                                [int(x) for x in playerYards], playerAge, playerPos, playerRecs, 
                                playerTar, playerYpR, playerCatchPert, playerTD), key=lambda x: (x[1], -x[2], x[4]), reverse = False) 

        '''prints just to make sure that data is being receieved'''
        for names, teams, ages, pos, yards, recs, targs, ypr, catchpert, touchdowns in sortedList: 
            print(f'{names}, {teams}, {ages}, {pos}, {yards}, {recs}, {targs}, {ypr}, {catchpert}, {touchdowns}')

        return sortedList  
    
