import os
import csv

total_votes = 0
candidates = []
candidate_votes = {}

election_data_csv = os.path.join("..", "Resources", "election_data.csv")
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = votes / total_votes * 100
    candidate_votes[candidate] = [votes, vote_percentage]

winner = max(candidate_votes, key=lambda x: candidate_votes[x][0])

print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for candidate in candidate_votes:
    votes, percentage = candidate_votes[candidate]
    print(f'{candidate}: {percentage:.3f}% ({votes})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

with open("../analysis/results.txt", "w") as file:
    file.write('Election Results\n')
    file.write('-------------------------\n')
    file.write(f'Total Votes: {total_votes}\n')
    file.write('-------------------------\n')
    for candidate in candidate_votes:
        votes, percentage = candidate_votes[candidate]
        file.write(f'{candidate}: {percentage:.3f}% ({votes})\n')
    file.write('-------------------------\n')
    file.write(f'Winner: {winner}\n')
    file.write('-------------------------\n')
