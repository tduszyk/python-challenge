import os, csv

# Path to collect data from the current folder
election_data_csv = os.path.join('election_data.csv')

# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Remove header
    csv_header = next(csvreader)

    vote_number = 0
    candidates = []
    cand1 = 0
    cand2 = 0
    cand3 = 0
    cand4 = 0
    winner = "None"

    #Looping through the data
    for row in csvreader:

        #The total number of votes cast
        vote_number += 1

        #A complete list of candidates who received votes
        if str(row[2]) not in candidates:
            candidates.append(str(row[2]))
        
        #The total number of votes each candidate won 
        #
        # This is faster but I don't like hardcoded names in the candidates
        #if row[2] == "Khan":
        #    cand1 += 1
        #if row[2] == "Correy":
        #    cand2 += 1
        #if row[2] == "Li":
        #    cand3 += 1
        #if row[2] == "O'Tooley":
        #    cand4 +=1
        #
        # This makes program execute slower but it gives extra flexibility
        #
        for name in candidates:
            if str(row[2]) == str(candidates[0]):
                cand1 += 1
            elif str(row[2]) == str(candidates[1]):
                cand2 += 1
            elif row[2] == candidates[2]:
                cand3 += 1
            elif row[2] == candidates[3]:
                cand4 +=1
        
        #The percentage of votes each candidate won
        cand1_perc = (cand1 / vote_number) * 100
        cand2_perc = (cand2 / vote_number) * 100
        cand3_perc = (cand3 / vote_number) * 100
        cand4_perc = (cand4 / vote_number) * 100

    #The winner of the election based on popular vote.
    if cand4 > cand3:
        #winner = "O'Tooley"
        winned = candidates[0]
    elif cand3 > cand2:
        winner = "Li"
    elif cand2 > cand1:
        winner = "Correy"
    else:
        winner = "Khan"

    print()
    print("Election Results")
    print("-------------------------------")
    print(f'Total Votes: {vote_number}')
    print("-------------------------------")
    print(f'{candidates[0]}: {cand1_perc:.3f}% ({cand1})')
    print(f'{candidates[1]}: {cand2_perc:.3f}% ({cand2})')
    print(f'{candidates[2]}: {cand3_perc:.3f}% ({cand3})')
    print(f'{candidates[3]}: {cand4_perc:.3f}% ({cand4})')
    print("-------------------------------")
    print(f'Winner: {winner}')
    print("-------------------------------")
    print()