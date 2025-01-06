from receiving import receivingStats

def main():
    receiver = receivingStats()
    stats = receiver.getStats()
    receiver.write_csv('recStats',['Name', 'Team', 'Age', 'Position',
                                   'Yards', 'Receptions', 'Targets', 
                                   'YardsPerReceptions', 'CatchPercentage', 'Touchdowns'], stats)

if __name__ == "__main__":
    main()