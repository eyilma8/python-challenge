import os
import csv
file_path=os.path.join("PyBank","Resources","budget_data.csv")
with open(file_path) as f:
   csvfile=csv.reader(f,delimiter=",")
   next(csvfile)
   csvfilelist=list(csvfile)
   NumberofMonths=len(csvfilelist)
TotalProfitLoss =list()
#Identify monthly Prof/Loss and sum to get net prof/Loss, append values of diffenece in consecuitive values in a list for later analysis
Difference = list()
Increases=list()
Decreases=list()
for i in range(NumberofMonths-1):
    TotalProfitLoss.append(int(csvfilelist[i][1]))
    NetProfLoss=sum(TotalProfitLoss)
    Difference.append(int(csvfilelist[i][1])-int(csvfilelist[i+1][1]))
#Maximum and Minimum value of changes as calculated above as difference of consequitive entries         
GreatestIncrease =max(Difference)
GreatesDecrease = min(Difference)
AverageChange=round(sum(Difference)/(NumberofMonths),2)
DateofIncrease = list()

#Identify Greatest Increase and Decrease date by attributing the date with a differnce equal Greatest increase identified above
c=0
for i in range(NumberofMonths-1):
    if int(csvfilelist[i][1])-int(csvfilelist[i+1][1])==GreatestIncrease:
        c=i+1
d=0
for i in range(NumberofMonths-1):
   if int(csvfilelist[i][1])-int(csvfilelist[i+1][1])==GreatesDecrease:
        d=i+1
 
#Report
print("Financial Analysis          ")
print("----------------------------------------")
print("Total Months :",NumberofMonths)
print("Total  :","$",NetProfLoss)
print("Average Change :","$",AverageChange)
print("Greatest Increase in profit: ", (csvfilelist[c][0]),"($",GreatestIncrease,")")
print("Greatest Decrease in Profit:",  (csvfilelist[d][0]),"($",GreatesDecrease,")")

print("----------------------------------------")