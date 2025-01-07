from bs4 import BeautifulSoup
from base_scraper import statsScraper

class passingStats(statsScraper):
    def getStats(self):

        '''inputs passing parameter into fetch_page() funciton in order to get values'''
        self.fetch_page('passing')
        table_tag = 'td'

        '''scrapes website using the html tags given on the website'''
        playerNames = self.find_stat(table_tag, 'name_display')
        playerAge = self.find_stat(table_tag, 'age')
        playerTeams = self.find_stat(table_tag, 'team_name_abbr')
        playerComp = self.find_stat(table_tag, 'pass_cmp')
        playerAtt = self.find_stat(table_tag, 'pass_att')
        playerPassYards = self.find_stat(table_tag, 'pass_yds')
        playerYardsPerPass = self.find_stat(table_tag, 'pass_yds_per_att')
        playerTD = self.find_stat(table_tag, 'pass_td')
        playerInt = self.find_stat(table_tag, 'pass_int')

        '''removes last row because it's empty'''
        playerPassYards = playerPassYards[0:len(playerPassYards) - 1]

        '''sorts list by Team then Passing Yards'''
        sortedList = sorted(zip(playerNames, playerTeams, playerAge, 
                                [int(x) for x in playerPassYards], playerComp, 
                                playerAtt, playerYardsPerPass, playerInt, playerTD ), key=lambda x: (x[1], -x[3]), reverse=False)
        
        '''prints to make sure the data is being correctly gathered'''
        for names, teams, age, yards, comp, att, ypp, inter, td in sortedList:
            print(f'{names}, {teams}, {age}, {yards}, {comp}, {att}, {ypp}, {inter}, {td}')
        
        return sortedList
