import os
import csv

csvpath = r"C:\Users\jimmy\OneDrive\Documents\BootCamp_Challenges\Pypoll\Resource\election_data.csv"

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader) 
    ballots = []
    candidates = []
    max_votes = 0
    winner = ""

    for row in csvreader:
        ballot = row[0]
        ballots.append(ballot)
        candidate = row[2]
        candidates.append(candidate)

    unique_candidates = set(candidates)
    total_votes = len(ballots)
    
    print("Election results")
    print("-------------------------")
    print("                            ")
    print("Total Votes: " + str(total_votes))
    print("                            ")
    print("-------------------------")

    for candidate in unique_candidates:
        votes_for_candidate = candidates.count(candidate)
        percentage = (votes_for_candidate / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes_for_candidate})")
        
        if votes_for_candidate > max_votes:
            max_votes = votes_for_candidate
            winner = candidate
    
    
    print("-------------------------")
    print("                            ")
    print(f"Winner: {winner}")
    print("                            ")
    print("-------------------------")



    
    




