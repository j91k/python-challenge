import os
import csv

csvpath = r"C:\Users\jimmy\OneDrive\Documents\BootCamp_Challenges\Pypoll\Resource\election_data.csv"

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    #Store Header
    header = next(csvreader) 
    ballots = []
    candidates = []
    max_votes = 0
    winner = ""

    # Created a loop for the rows
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

    # Created a loop for 'candidate' to only cycle through the unique candidates then to figure out the % of votes and total votes
    for candidate in unique_candidates:
        votes_for_candidate = candidates.count(candidate)
        percentage = (votes_for_candidate / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes_for_candidate})")
        
        # Finding which candidate has the most votes
        if votes_for_candidate > max_votes:
            max_votes = votes_for_candidate
            winner = candidate
    
    
    print("-------------------------")
    print("                            ")
    print(f"Winner: {winner}")
    print("                            ")
    print("-------------------------")

# Results that will be in text
output_text = (
    "Election results\n"
    "-------------------------\n"
    "                            \n"
    f"Total Votes: {total_votes}\n"
    "                            \n"
    "-------------------------\n"
)

# Added the if statement again to have the correct value on the text file
for candidate in unique_candidates:
    votes_for_candidate = candidates.count(candidate)
    percentage = (votes_for_candidate / total_votes) * 100
    output_text += f"{candidate}: {percentage:.3f}% ({votes_for_candidate})\n"

output_text += (
    
    "-------------------------\n"
    "                            \n"
    f"Winner: {winner}\n"
    "                            \n"
    "-------------------------\n"
)

# Write the output to a text file
output_path = r"C:\Users\jimmy\OneDrive\Documents\BootCamp_Challenges\Pypoll\analysis\result_Pypoll.txt"
with open(output_path, 'w') as output_file:
    output_file.write(output_text)
    
    




