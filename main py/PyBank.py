#PyBank
import os
import csv
#Import the file and ensure it reads properly
csvpath = r"C:\Users\cppar\OneDrive\Documents\Wk_3_Challenges_6\Starter_Code\PyBank\Resources\budget_data.csv"
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

#Create variables to hold the count, Profit/Loss, greatest increase, greatest decrease, and total change
    counter = 0
    netPnL = 0
    Greatest = 0 
    Least = 0
    TotalChange = 0

#Define last month to help with calculations
    vLastPnL = 0

#Loop through each row
    for row in csvreader:

        #Add 1 to the count of months
        counter += 1

        #Calculate the month-to-month change
        vThisPnL = (float(row[1]))
        MonthlyChange = vThisPnL-vLastPnL
        if counter > 1:
            TotalChange += MonthlyChange

        #If new greatest increase value, store new value
        if (MonthlyChange < Least):
            Least = MonthlyChange
            vLowDate = row[0]

        #If new greatest decrease value, store new value
        if MonthlyChange > Greatest:            
            Greatest = MonthlyChange
            vHighDate = str(row[0])

        #Add the profit/loss 
        netPnL += float(row[1])

        #Set current month to last month before next loop
        vLastPnL = vThisPnL

#Calculate the average change for profit/loss column
AvgChange = (TotalChange/(counter - 1))

    
#Print variables to terminal showing results
print("Financial Analysis")
print("---------------------------------------------------")
print("Total Months: " +str(counter))
print("Total: $" + format(int(netPnL)))
print("Average Change: $" + format(round(AvgChange,2)))
print("Greatest Increase in Profits: " + vHighDate +  " $" + format(int(Greatest)))
print("Greatest Decrease in Profits: " + vLowDate +  " $" + format(int(Least)))

    
#Store outputs as variables for textfile writing
FinalTotalMonths = "Total Months: " +str(counter)
FinalTotalCash = "Total: $" + format(int(netPnL))
FinalTotalAvgChng = "Average Change: $" + format(round(AvgChange,2))
FinalGreatestInc = "Greatest Increase in Profits: " + vHighDate +  " $" + format(int(Greatest))
FinalGreatestDec = "Greatest Decrease in Profits: " + vLowDate +  " $" + format(int(Least))

#Export a text file with results
f = open('PyBank_final.txt', 'w')
f.write('Financial Analysis \n')
f.write('---------------------------------------------------\n')
f.write(str(FinalTotalMonths))
f.write('\n')
f.write(str(FinalTotalCash))
f.write('\n')
f.write(str(FinalTotalAvgChng))
f.write('\n')
f.write(str(FinalGreatestInc))
f.write('\n')
f.write(str(FinalGreatestDec))


