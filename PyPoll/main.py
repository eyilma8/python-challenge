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

# Reporting to text file ("PyPoll, Text_Report")
Text_Report = os.path.join("Analysis","Text_Report.txt")
with open(Text_Report, "w") as f:

    print("Election Results                ",file=f)
    print("--------------------------------------------",file=f)

    print("Total Votes :  ", TotalVotesCount,file=f)

    print("--------------------------------------------",file=f)

    for i in range(candidatecount):
        print(candidatelist[i],":", f'{(percentagevote[i]*100):.2f}%', f'({votecount[i]})',file=f)
    print("-------------------------------------------",file=f)
    print("Winner:", Winner,file=f)

    print("-------------------------------------------", file=f)