from receiving import receivingStats
from passing import passingStats

def main():
    
    receiver = receivingStats()
    stats = receiver.getStats()
    receiver.write_csv('recStats',['Name', 'Team', 'Age', 'Position',
                                   'Yards', 'Receptions', 'Targets', 
                                   'YardsPerReceptions', 'CatchPercentage', 'Touchdowns'], stats)
    

    passer = passingStats()
    stats = passer.getStats()
    passer.write_csv('pasStats', ['Name', 'Team', 'Age', 'Yards', 
                                  'Completions', 'Attempts', 'YardsPerPass',
                                  'Interceptions', 'Touchdowns'], stats)

if __name__ == "__main__":
    main()