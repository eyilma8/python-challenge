import os
import csv
file_path=os.path.join("Resources","budget_data.csv")
with open(file_path) as f:
       csvfile=csv.reader(f,delimiter=",")
next(csvfile)
#TotalNumberofMonth len is a function to count, and
NumberofMonth=list(csvfile)
TotalNumberofMonths=len(NumberofMonth)
#sum will add all value in column 2 
NetProfLoss=sum(csvfile[1])
#Creating third column and populate with difference values inconsecutive rows in column 2     
for i in range(0,TotalNumberofMonths-1):
        csvfile[i].append(csvfile[i]-csvfile[i+1])
#Add the third column with Prof/loss change
GreatestIncrease=max(csvfile[2])
GreatestDecrease=min(csvfile[2])
#Date of Greatest Inrease and Decrease
for i in range(TotalNumberofMonths):
     if csvfile[i][2] == GreatestIncrease:
             DateofIncrease = csvfile[0]
     elif csvfile[i][2] == GreatestDecrease:
        DateofDecrease= csvfile[0]
#Report
print("              Financial Analysis             ")

print("---------------------------------------------")
print("Total Months :  ", TotalNumberofMonths)
print("Total :  ",NetProfLoss )
print("Greatest Increase in Profit : ",DateofIncrease,GreatestIncrease)
print("Greatest Decrease in Profit : ",DateofDecrease,GreatestDecrease)