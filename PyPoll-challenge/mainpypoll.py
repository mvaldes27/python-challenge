# import modules
import os
import csv

# Set path for file
election_csv = os.path.join("Resources", "election_data.csv")

# Open CSV Path and specify delimiter
with open(election_csv) as csv_file:    
    election_csv = csv.reader(csv_file, delimiter=",")

    # Read header row first 
    csv_header = next(csv_file)

    # Create variables
    total_votes = 0
    candidates = []
    Khan_votes = 0
    Correy_votes = 0 
    Li_votes = 0
    oTooley_votes = 0
    vote_dict = {}
    


    for vote in election_csv: 
        # add total votes
        total_votes += 1

    # if candidate name is not in list, add to candidate list
        if vote[2] not in candidates:
            candidates.append(vote[2])
            

    # calculate total number of votes each candidate won
        if vote[2] == "Khan":
            Khan_votes += 1
        elif vote[2] == "Correy":
            Correy_votes += 1
        elif vote[2] == "Li":
            Li_votes += 1
        else: 
            oTooley_votes += 1

    # calculate percentage of votes each candidate won
    Khan_percent = float(round(Khan_votes/total_votes * 100))
    Correy_percent = float(round(Correy_votes/total_votes * 100))
    Li_percent = float(round(Li_votes/total_votes * 100))
    oTooley_percent = float(round(oTooley_votes/total_votes * 100))

    # create dictionary of candidates and vote totals
    vote_dict = {'Khan': Khan_votes, 'Correy': Correy_votes , 'Li' : Li_votes, 'oTooley': oTooley_votes}

    # calculate popular vote value
    max_votes = max(vote_dict.values())

    # get matching key for max_votes to find the winner

    #loop through dictionary to find max
    for key in vote_dict: 
        winner = max(vote_dict, key=vote_dict.get)

    # export analysis to file
    #set filepath 
    output_path = os.path.join('Analysis', 'Election_Results.txt') 
    with open(output_path, 'w') as txtfile: 
        txtfile.write("Election Results \n")
        txtfile.write("----------------------\n")
        txtfile.write(f"Total Votes: {total_votes}\n")
        txtfile.write("----------------------\n")
        txtfile.write(f"Khan: {Khan_percent}% ({Khan_votes}) \n")
        txtfile.write(f"Correy: {Correy_percent}% ({Correy_votes}) \n")
        txtfile.write(f"Li: {Li_percent}% ({Li_votes}) \n")
        txtfile.write(f"O'Tooley: {oTooley_percent}% ({oTooley_votes}) \n")
        txtfile.write("----------------------\n")
        txtfile.write(f"Winner : {winner}\n")
        txtfile.write("----------------------\n")

    #print results to terminal
    # open financial analysis and print results to terminal
    with open(output_path) as show_file:
        print(show_file.read())