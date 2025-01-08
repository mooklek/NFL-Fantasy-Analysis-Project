from bs4 import BeautifulSoup
from base_scraper import statsScraper

class rushingStats(statsScraper):
    def getStats(self):

        self.fetch_page('rushing')
        table_tag = 'td'

        playerNames = self.find_stat(table_tag, 'name_display')
        playerAge = self.find_stat(table_tag, 'age')
        playerTeams = self.find_stat(table_tag, 'team_name_abbr')
        playerPos = self.find_stat(table_tag, 'pos')
        playerYards = self.find_stat(table_tag, 'rush_yds')
        playerRushAtt = self.find_stat(table_tag, 'rush_att')
        playerTD = self.find_stat(table_tag, 'rush_td')
        playerRushYpG = self.find_stat(table_tag, 'rush_yds_per_g')
        playerFumble = self.find_stat(table_tag, 'fumbles')

        playerYards = playerYards[0:len(playerYards) - 1]

        sortedList = sorted(zip(playerNames, playerTeams, playerAge, 
                                [int(x) for x in playerYards], playerPos, 
                                playerRushAtt, playerRushYpG, playerFumble, playerTD), key=lambda x: (x[1], -x[3]), reverse=False)

        for names, teams, age, yards, pos, rushAtt, rushYpG, fumbles, td in sortedList:
            print(f'{names}, {teams}, {age}, {yards}, {pos}, {rushAtt}, {rushYpG}, {fumbles}, {td}')

        return sortedList