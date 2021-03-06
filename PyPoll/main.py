import os
import csv
from collections import Counter

Voter_ID_list=[]
County_list=[]
Candidate_list=[]

with open('Resources/election_data.csv', 'r') as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
       Voter_ID_list.append(row[0])
    for row in reader:
       Candidate_list.append(row[2])
Total_votes =len(Voter_ID_list)
print("Total Votes:", Total_votes)
print("---------------------------------")

with open('Resources/election_data.csv', 'r') as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
       Candidate_list.append(row[2])


Candidate_count=dict(Counter(Candidate_list))
#print(type(Candidate_count))
Candidate_summary={k:v/len(Voter_ID_list) for k,v in Candidate_count.items()}
for k,v in Candidate_summary.items():
    print(f"{k} : {round(v*100,3)}% ({round(v*len(Voter_ID_list))})")
print("---------------------------------")

winner_count=max(Candidate_count.values())
winner_name=[k for k,v in Candidate_count.items() if v==winner_count]
for winner in winner_name:
    print(f"Winner: {winner}")
print("---------------------------------")


