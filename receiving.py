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

        rows = self.parse_rows() 

        for row in rows:
            players = row.findAll('a', href=True)
            for index, player in enumerate(players):
                if index % 2 == 0:
                    name = player.text.strip()
                    playerNames.append(name)
            '''
            yards = row.findAll('td', {'data-stat': 'rec_yds'}) 
            for index, totalYard in enumerate(yards):
                yard = totalYard.text.strip()
                playerYards.append(yard)
            '''
            
            teams = row.findAll('td', {'data-stat': 'team_name_abbr'}) 
            for index, teamName in enumerate(teams):
                team = teamName.text.strip()
                playerTeams.append(team)

        playerYards = self.find_stat('td', 'rec_yds')

        playerYards = playerYards[0:len(playerYards) - 1] 

        sortedList = sorted(zip(playerNames, playerTeams, [int(x) for x in playerYards]), key=lambda x: x[1], reverse = False) 

        for playerName, playerYard, playerTeam in sortedList: 
            print(f'{playerName} | {playerYard} | {playerTeam}')

        return sortedList  