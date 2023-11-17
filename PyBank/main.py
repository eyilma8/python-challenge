import os
import csv
file_path=os.path.join("Resources","budget_data.csv")
with open(file_path) as f:
   csvfile=csv.reader(f,delimiter=",")
   next(csvfile)
   csvfilelist=list(csvfile)
   NumberofMonths=len(csvfilelist)
TotalProfitLoss =list()
Difference = list()
for i in range(NumberofMonths-1):
    ProfLoss = int(csvfilelist[i][1])
    TotalProfitLoss.append(ProfLoss)
    i=i+1
    Diff = int(csvfilelist[i][1])-int(ProfLoss)
    Difference.append(Diff)
    Net=sum(TotalProfitLoss)
#Calculate the value difference in consequitive results 
GreatestIncrease=max(Difference)
GreatestDecrease=min(Difference)
DateofIncrease = list()
DateofDecrease = list()
# Get a date the greatest increase and decrease occured
for j in range(NumberofMonths-1):
    if csvfilelist[j][1]==GreatestIncrease:
         DateofIncrease.append(csvfilelist[j][0])
    elif csvfilelist[j][1]==GreatestDecrease:
         DateofDecrease.append(csvfilelist[j][0])

#Report
print("            Financial Analysis          ")
print("----------------------------------------")
print("Total Months :",NumberofMonths)
print("Total  :",Net)
print("Greatest Increase in profit: ", DateofIncrease,GreatestIncrease)
print("Greatest Decrease in Profit:",  DateofDecrease,GreatestDecrease)

print("----------------------------------------")