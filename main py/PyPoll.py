import os
import csv

csvpath = r"C:\Users\cppar\OneDrive\Documents\Wk_3_Challenges_6\Starter_Code\PyPoll\Resources\election_data.csv"
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

#Define variables for counter 
    counter = 0
    StockhamCounter = 0
    DeGetteCounter = 0
    DoaneCounter = 0
    Candidates = []

    for row in csvreader:
        if row[2] not in Candidates:
            Candidates.append(row[2])

    #Add 1 to the counter
        counter += 1
        #Add 1 to the voted candidate
        if row[2] == "Charles Casper Stockham":
            StockhamCounter += 1
        if row[2] == "Diana DeGette":
            DeGetteCounter += 1
        if row[2] == "Raymon Anthony Doane":
            DoaneCounter += 1
    #Calculate percent of votes and store in a variable for each candidate
    Spercent = StockhamCounter/counter
    Dpercent = DeGetteCounter/counter
    Rpercent = DoaneCounter/counter
    Winner = max(StockhamCounter,DoaneCounter,DeGetteCounter)

print(Candidates)
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(counter))
print("-------------------------")
print("Charles Casper Stockham: " + format(round(Spercent,5) * 100) + "%  (" + str(StockhamCounter) + ")")
print("Diana DeGette: " + format(round(Dpercent,5) * 100) + "%  (" + str(DeGetteCounter) + ")")
print("Raymon Anthony Doane: " + format(round(Rpercent,5) * 100) + "%  (" + str(DoaneCounter) + ")")
print("-------------------------")
print("Winner: " + str(Winner))
print("-------------------------")

#Store outputs as variables for textfile writing
TotalVotes = "Total Votes: " + str(counter)
Candidate1 = "Charles Casper Stockham: " + format(round(Spercent,5) * 100) + "%  (" + str(StockhamCounter) + ")"
Candidate2 = "Diana DeGette: " + format(round(Dpercent,5) * 100) + "%  (" + str(DeGetteCounter) + ")"
Candidate3 = "Raymon Anthony Doane: " + format(round(Rpercent,5) * 100) + "%  (" + str(DoaneCounter) + ")"
FinalWinner = "Winner: " + str(Winner)

#Export a textfile with the result
f = open('PyPoll_final.txt', 'w')
f.write('Election Results \n')
f.write('------------------------- \n')
f.write(str(TotalVotes))
f.write('\n')
f.write(str(Candidate1))
f.write('\n')
f.write(str(Candidate2))
f.write('\n')
f.write(str(Candidate3))
f.write('\n')
f.write('-------------------------')
f.write('\n')
f.write(str(FinalWinner))