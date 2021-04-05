#Data we need

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initilaize vote counter
total_votes = 0
# Empty candidate list 
candidate_options = []
# Empty dictionary for vote counting
candidate_votes = {}
# Winning Candidate tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
# Print header row from the CSV
    headers = next(file_reader)
    #print(headers)
    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        #print(total_votes)

        # Print the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list, unique candidates only
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    # Percent vote calculation
    for candidate_name in candidate_votes:
        # Pull vote count
        votes = candidate_votes[candidate_name]
        # Calc percentage
        vote_percentage = (float(votes) / float(total_votes) * 100)
        # Print results of the loop
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote")
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

#Print the winning candidate, vote count, and percentage
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
print(winning_candidate_summary)

# Total number of votes cast
# A complete list of candidates who recieved votes
# Percentage of votes for each candidate
# Total number of votes per candidate
# Winner of election based on popular vote



