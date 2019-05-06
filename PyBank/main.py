import os, csv

# Path to collect data from the same folder
budget_data_csv = os.path.join('budget_data.csv')

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Remove header
    csv_header = next(csvreader)

    number_of_months = 0    
    total_LP = 0
    #rows = []
    max_increase = 0
    max_decrease = 0
    # Loop through the data
    for row in csvreader:
        #The total number of months included in the dataset
        number_of_months += 1
        #The net total amount of "Profit/Losses" over the entire period
        total_LP += int(row[1])
        #The greatest increase in profits (date and amount) over the entire period
        if int(row[1]) > int(max_increase): 
            max_increase = row[1]
            greatest_increase = str(row[0]) + ' ' + '($' + str(row[1]) + ')'
        #The greatest decrease in losses (date and amount) over the entire period
        if int(row[1]) < int(max_decrease):
            max_decrease = row[1]
            greatest_decrease = str(row[0]) + ' ' + '($' + str(row[1]) + ')'
    print()
    print()
    print("Financial Analysis")
    print("---------------------------------------------")
    print("Total Months: ",number_of_months, sep="")
    print("Total: $",total_LP, sep="")
    #The average of the changes in "Profit/Losses" over the entire period
    averave_LP = (total_LP / number_of_months)
    print("Average Change: $","{:.2f}".format(averave_LP), sep="")
    print(f'Greatest Increase in Profits: {greatest_increase}')
    print(f'Greatest Decrease in Profits: {greatest_decrease}')