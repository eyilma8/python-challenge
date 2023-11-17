
import os
import csv
file_path = os.path.join("Resources","election_data.csv")

with open(file_path, newline='') as f:
    csvfile = csv.reader(f, delimiter=",")

    next(csvfile)
#Total number of votes - convert to list and count with function len()
    csvfilelist=list(csvfile)
    TotalVotesCount = len(csvfilelist)
    
#name of candidates add them in fourth column

candidatelist=list()
candidates = list()
candidatesUnique= list()
for i in range(TotalVotesCount-1):
    candidate=csvfilelist[i][2]
    candidatelist.append(candidate)
p=0
for j in range (TotalVotesCount-1):
   if  csvfilelist[j][2]!=csvfilelist[j+1][2]:
      candidatesUnique.append(csvfilelist[j][2])
else:
     
    candidate1=candidatesUnique[1]
    candidate2=candidatesUnique[2]
    candidate3=candidatesUnique[3]
#Count per candidate - assumes number of candidates are know as 3
count1=0
count2=0
count3=0
for i in range(TotalVotesCount):
    if candidate1==candidatelist:
        count1=count1+1
    elif candidate2==candidatelist:
      count2=count2+1
    elif candidate3==candidatelist:
        count3=count3+1
#percentage Candidate score
Percentage1=count1/TotalVotesCount
Percentage2=count2/TotalVotesCount
Percentage3=count3/TotalVotesCount
# Winner
WinnerCount=max(count1,count2,count3)
if WinnerCount==count1:
    Winner = candidatelist[1]
elif WinnerCount==count2:
  Winner=candidatelist[2]
else:
    Winner=candidatelist[3]
# Report

print("              Election Results                ")
print("----------------------------------------------")
print("Total Votes :  ", TotalVotesCount)
print("----------------------------------------------")
print(candidatelist[1],Percentage1,count1 )
print(candidatelist[2],Percentage2,count2 )
print(candidatelist[3],Percentage3,count3)
print("----------------------------------------------")
print("Winner: ",Winner)
print("----------------------------------------------")