
import os
import csv
file_path = os.path.join("PyPoll","Resources","election_data.csv")

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
count=list()
p=0
r=0
for i in range (TotalVotesCount-1):
      if  (csvfilelist[i][2])!=(csvfilelist[i+1][2]):
          candidate1=str(csvfilelist[i][2])
          candidates.append(candidate1)

candidate1=candidates[0]
candidate2=candidates[1]
candidate3=candidates[2]
count1=0
count2=0
count3=0

#Count per candidate - assumes number of candidates are know as 3
for i in range(TotalVotesCount):
    if candidate1==csvfilelist[i][2]:
        count1=count1+1

for i in range(TotalVotesCount):
    if candidate2==csvfilelist[i][2]:
        count2=count2+1

for i in range(TotalVotesCount):
    if candidate3==csvfilelist[i][2]:
        count3=count3+1
#Percentage of counts for each candidate converted to a percentage and rounded to two decimal place
Percentage1 = round((count1/TotalVotesCount)*100,2)
Percentage2 = round((count2/TotalVotesCount)*100,2)
Percentage3 = round((count3/TotalVotesCount)*100,2)

WinnerCount = max(count1,count2,count3)

if WinnerCount==count1:
    Winner = candidate1
elif WinnerCount==count2:
    Winner = candidate2
elif WinnerCount==count3:
    Winner=candidate3
# Report

print("Election Results                ")
print("----------------------------------------------")
print("Total Votes :  ", TotalVotesCount)
print("----------------------------------------------")
print(candidate1,":" ,Percentage1,"%","(",count1,")" )
print(candidate2,":" ,Percentage2,"%","(",count2,")" )
print(candidate3,":" ,Percentage3,"%","(",count3,")" )
print("-------------------------------------------")
print("Winner :", Winner)

print("-------------------------------------------")