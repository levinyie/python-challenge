import os
import csv

output_path = os.path.join("Resources", "output.csv")
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
        
        #If that row does not equal the name, move on, etc.
        if (row[2] == 'Charles Casper Stockham'):
            charles = charles + 1
        elif (row[2] == 'Diana DeGette'):
            diana = diana + 1
        else:
            raymon = raymon + 1

        #The percentages of each candidates' votes out of total votes
        #Round(____, 3) Round the percentage to 3 decimals
        cperc = (charles / total_votes) * 100
        cperc = round(cperc, 3)
        dperc = (diana / total_votes) * 100
        dperc = round(dperc, 3)
        rperc = (raymon / total_votes) * 100
        rperc = round(rperc, 3)

    #Put the candidates into a dictionary so we can find the winner by using the get.max function
        #This way if the winner changes based on the data, the output would still be accurate
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

#Inserted the values in a tuple to be used when using csvwriter to write it in text file
    election_tuple = (total_votes, charles, diana, raymon, total_winner)

with open(output_path, 'w') as csvfile:
    
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Total Votes', 'Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane', 'Winner'])
    
    csvwriter.writerow(election_tuple)
