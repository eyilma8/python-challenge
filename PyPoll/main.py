
import os
import csv
file_path = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(file_path, newline='') as f:
    csvfile = csv.reader(f)

    next(csvfile)
#Total number of votes - convert to list and count with function len()
    TotalVotes = list(csvfile)
    TotalVotesCount = len(csvfile)
#A List candidates and add them in fourth column
r = 0
for i in range(TotalVotesCount):
    if csvfile[i][2] != csvfile[i+1][2]:
        r += 1
        csvfile.append(csvfile[r][3])
#Count per candidate - assumes number of candidates are know
count1=0
count2=0
count3=0
for j in range(TotalVotesCount):
    if csvfile[1][3]==csvfile[j][2]:
        count1=count1+1
    elif csvfile[2][3]==csvfile[j][2]:
          count2=count2+1
    elif csvfile[3][3]==csvfile[j][2]:
        count3 = count3+1
 #percentage Candidate score
Percentage1=count1/TotalVotesCount
Percentage2=count2/TotalVotesCount
Percentage3=count3/TotalVotesCount
# Winner
WinnerCount=max(count1,count2,count3)
if WinnerCount==count1:
    Winner = csvfile[1][3]
elif WinnerCount==count2:
    Winner=csvfile[2][3]
else:
    Winner=csvfile[3][3]
# Report

print("              Election Results                ")

print("----------------------------------------------")
print("Total Votes :  ", TotalVotesCount)
print("----------------------------------------------")
print(csvfile[1][3],Percentage1,count1 )
print(csvfile[2][3],Percentage2,count2 )
print(csvfile[3][3],Percentage3,count3)
print("----------------------------------------------")
print("Winner: ",Winner)