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
        playerGames = []
        playerGameStart = []
        playerCatchPerc = []
        playerTD = []

        table_tag = 'td'

        '''
        for row in rows:
            players = row.findAll('a', href=True)
            for index, player in enumerate(players):
                if index % 2 == 0:
                    name = player.text.strip()
                    playerNames.append(name)
        
            yards = row.findAll('td', {'data-stat': 'rec_yds'}) 
            for index, totalYard in enumerate(yards):
                yard = totalYard.text.strip()
                playerYards.append(yard)

            teams = row.findAll('td', {'data-stat': 'team_name_abbr'}) 
            for index, teamName in enumerate(teams):
                team = teamName.text.strip()
                playerTeams.append(team)
        '''

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
    
