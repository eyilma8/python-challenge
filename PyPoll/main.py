import os
import csv
file_path = os.path.join("Resources","election_data.csv")

with open(file_path, newline='') as f:
    csvfile = csv.reader(f, delimiter=",")

    next(csvfile)
#Total number of votes - convert to list and count with function len()
    csvfilelist=list(csvfile)
    TotalVotesCount = len(csvfilelist)
    
#Create a candidate list
candidatelist=list()
for i in range(TotalVotesCount-1):
        candidate=csvfilelist[i][2]
        if csvfilelist[i][2]!=csvfilelist[i+1][2] and candidate not in candidatelist:
            candidatelist.append(csvfilelist[i][2])

#Vote count per each candidate calculated with double loop for candidates and the entire list for count
votecount = list()
percentagevote = list()
candidatecount = len(candidatelist)
for i in range(candidatecount):
        candidate =candidatelist[i]
        count =0
        for j in range(TotalVotesCount-1):
            if csvfilelist[j][2]==candidate:
              count=count+1
        votecount.append(count)  
        percentagevote.append(count/TotalVotesCount)

#Winner identification
Winnercount = max(votecount)
for i in range(candidatecount):
    if Winnercount == votecount[i]:
         Winner = candidatelist[i]
         
# Report

print("Election Results                ")
print("----------------------------------------------")
print("Total Votes :  ", TotalVotesCount)
print("----------------------------------------------")
for i in range(candidatecount):
    print(candidatelist[i],":", f'{(percentagevote[i]*100):.2f}%', f'({votecount[i]})')
print("-------------------------------------------")
print("Winner:", Winner)

print("-------------------------------------------")