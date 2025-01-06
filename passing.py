from bs4 import BeautifulSoup
from base_scraper import statsScraper

class passingStats(statsScraper):
    def getStats(self):
        self.fetch_page('passing')
        
        playerNames = []
        playerAge = []
        playerTeams = []
        playerComp = []
        playerAtt = []
        playerPassYards = []
        playerCompRate = []
        playerTD = []
        playerInt = []
        table_tag = 'td'

        playerNames = self.find_stat(table_tag, 'name_display')
        playerAge = self.find_stat(table_tag, 'age')
        playerTeams = self.find_stat(table_tag, 'team_name_abbr')
        playerComp = self.find_stat(table_tag, 'pass_cmp')
        playerAtt = self.find_stat(table_tag, 'pass_att')
        playerPassYards = self.find_stat(table_tag, 'pass_yds')
        playerCompRate = self.find_stat(table_tag, 'pass_cmp_pct')
        playerTD = self.find_stat(table_tag, 'td')
        playerInt = self.find_stat(table_tag, 'pass_int')



