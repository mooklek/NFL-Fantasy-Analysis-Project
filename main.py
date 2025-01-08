from receiving import receivingStats
from passing import passingStats
from rushing import rushingStats

def main():
    
    receiver = receivingStats()
    stats = receiver.getStats()
    receiver.write_csv('recStats', ['Name', 'Team', 'Age', 'Yards',
                                   'Position', 'Receptions', 'Targets', 
                                   'YardsPerReceptions', 'CatchPercentage', 'Touchdowns'], stats)
    

    passer = passingStats()
    stats = passer.getStats()
    passer.write_csv('pasStats', ['Name', 'Team', 'Age', 'Yards', 
                                  'Completions', 'Attempts', 'YardsPerPass',
                                  'Interceptions', 'Touchdowns'], stats)
    

    rusher = rushingStats()
    stats = rusher.getStats()
    rusher.write_csv('rusStats', ['Name', 'Team', 'Age', 'Yards', 
                                 'Position', 'Attempts', 'YardsPerGame', 
                                 'Fumbles', 'Touchdowns'], stats)

if __name__ == "__main__":
    main()