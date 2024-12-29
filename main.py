from receiving import receivingStats

def main():
    receiver = receivingStats()
    stats = receiver.getStats()
    receiver.write_csv('recStats', stats)

if __name__ == "__main__":
    main()