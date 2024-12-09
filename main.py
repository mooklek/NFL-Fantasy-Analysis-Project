from bs4 import BeautifulSoup
import requests
import csv

measurement = '' # Easier to swap which measurement we're looking at. Passing, Receiving, Rushing, etc

def insertMeasurement(measurement: str) -> str:
    url = "https://www.pro-football-reference.com/years/2024/" + measurement + ".htm" # Changes the URL based on what measurement we put and returns it for bs4 & requests to use
    return url


result = requests.get(insertMeasurement('receiving'))
doc = BeautifulSoup(result.text, "html.parser")

playerNames = []
playerYards = []

rows = doc.findAll('tr') # BS4 Parsing through the html to find specific stats. In this specific case, we're parsing through to find the receiving stats for players 

for row in rows:
    players = row.findAll('a', href=True) # finding names
    for index, player in enumerate(players):
        if index % 2 == 0:
            href = player['href']
            name = player.text.strip()
            playerNames.append(name)

    yards = row.findAll('td', {'data-stat': 'rec_yds'}) # finding received yards
    for index, totalYard in enumerate(yards):
        yard = totalYard.text.strip()
        playerYards.append(yard)

playerYards = playerYards[0:len(playerYards) - 1] # removing the last row of the list since it's empty and will break the sorted function

sortedList = sorted(zip(playerNames, [int(x) for x in playerYards]), key=lambda x: x[1], reverse = True) # sorting the list by most yards to least yards

for playerName, playerYard in sortedList: 
    print(f'{playerName} : {playerYard}')

with open('RECIVINGstats.csv', 'w', newline = '') as csvfile: # writes to csv file
    writer = csv.writer(csvfile)
    writer.writerows(sortedList)
