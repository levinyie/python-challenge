import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

with open(election_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)

    total_votes = 0
    charles = 0
    diana = 0
    raymon = 0
    cperc = 0
    dperc = 0
    rperc = 0

    for row in csv_reader:
        #Total number of votes cast
        total_votes += 1
        
        if (row[2] == 'Charles Casper Stockham'):
            charles = charles + 1
        elif (row[2] == 'Diana DeGette'):
            diana = diana + 1
        else:
            raymon = raymon + 1

        cperc = (charles / total_votes) * 100
        cperc = round(cperc, 3)
        dperc = (diana / total_votes) * 100
        dperc = round(dperc, 3)
        rperc = (raymon / total_votes) * 100
        rperc = round(rperc, 3)
    winner = {charles: 'Charles Casper Stockham', diana: 'Diana DeGette', raymon: 'Raymon Anthony Doane'}
    total_winner = winner.get(max(winner))

    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------------')
    print(f'Charles Casper Stockham: {cperc}% ({charles})')
    print(f'Diana DeGette: {dperc}% ({diana})')
    print(f'Raymon Anthony Doane: {rperc}% ({raymon})')
    print('-------------------------')
    print(f'Winner: {total_winner}')
    print('-------------------------')


