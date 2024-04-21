#import modules
import csv
import os

#point to data file
INPUT_CSV_PATH = os.path.join("Resources", "budget_data.csv")

#file to hold pybank analysis
outputfile = os.path.join("pybankAnalysis.txt")

#variables to hold information
totalMonths = 0 
total = 0 #profits/losses
netChanges = []
months = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 999999999999]


os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(INPUT_CSV_PATH) as input_csv_file:
    csvreader = csv.reader(input_csv_file)

    #read header row
    header = next(csvreader)
    #move to first row
    firstRow = next(csvreader)
    
    #count of the total months
    totalMonths += 1
    #add to the total profits
    total += int(firstRow[1])
    
    #initialize previous data in index 1
    previousData = int(firstRow[1])

    for row in csvreader:
        #increment total count of months
        totalMonths += 1
        #add on to the total profit
        total += int(row[1])

        #get net change
        netChange = int(row[1]) - previousData
        #add on to the list of average change
        netChanges.append(netChange)

        #add first month that a change occurs
        months.append(row[0])

        #update the previous revenue
        previousData = float(row[1])

        #if statements to calculate the greatest increase and decrease
        if netChange > greatestIncrease[1]:
                greatestIncrease[0] = row[0]
                greatestIncrease[1] = netChange
                
        if netChange< greatestDecrease[1]:
                greatestDecrease[0] = row[0]
                greatestDecrease[1] = netChange

netMonthlyAverage = (sum(netChanges) / len(netChanges))


output = (
    f"Financial Analysis \n"
    f"--------------------------\n"
    f"Total Months: {totalMonths} \n"
    f"Total: ${total}\n"
    f"Average Change: ${netMonthlyAverage:,.2f}\n"
    f"Greatest Increase in Profits: ${greatestIncrease}\n"
    f"Grestest Decrease in Profits: ${greatestDecrease}\n"
    )

print(output)

with open(outputfile, "w") as textfile:
    textfile.write(output)
  