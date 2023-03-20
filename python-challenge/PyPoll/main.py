import csv
import os

csvpath = os.path.join('Resources','election_data.csv')

# Dependencies

votes = {}
total_votes = 0

# Read as reader and skip the header row

with open(csvpath, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    
# The total number of votes cast

    for row in reader:
        total_votes += 1
        
        candidate = row[2]
        
# A complete list of candidates who received votes

        if candidate not in votes:
            votes[candidate] = 0

        votes[candidate] += 1
        
    print(f"Total Votes: {total_votes}")
    
# The percentage of votes each candidate won
# The total number of votes each candidate won

# Export analysis to txt prior to looping for percentages and total votes per candidate

    analysis = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )

    for candidate, vote_count in votes.items():
        percent = (vote_count / total_votes) * 100
        analysis += f"{candidate}: {percent:.3f}% ({vote_count})\n"
    
# The winner of the election based on popular vote

    winner = max(votes, key=votes.get)
    analysis += f"-------------------------\n"
    analysis += f"Winner: {winner}\n"
    analysis += f"-------------------------"

print(analysis)

# Export a text file with the results

analysis_export = "analysis/Election_Results.txt"

with open(analysis_export,"w") as txt_file:
    txt_file.write(analysis)