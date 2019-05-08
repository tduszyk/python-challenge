import os, csv
from statistics import mean

# Path to collect data from the same folder
budget_data_csv = os.path.join('budget_data.csv')

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Remove header
    csv_header = next(csvreader)

    #Setting addtional variables
    number_of_months = 0    
    total_LP = 0
    dates = []
    values = []
    diffs = []
    average_diff = []
    i = 0

    # Loop through the datai
    for row in csvreader:
        #The total number of months included in the dataset
        number_of_months += 1
        #The net total amount of "Profit/Losses" over the entire period
        total_LP += int(row[1])
        
        # Create 3 separte lists
        dates.append(row[0])
        values.append(int(row[1]))
    for i in range(len(values)):
        if i == 0:
            diffs.append(0)
        else:
            diff = ((values[i]) - values[i - 1])
            diffs.append(diff)
    
    #print(dates)
    #print(values)
    #print(diffs)

    new_list = zip(dates, diffs)
    # save the output file path
    output_file = os.path.join("output.csv")

    # open the output file, create a header row, and then write the zipped object to the csv
    with open(output_file, "w", newline="") as datafile:
        writer = csv.writer(datafile)

        #writer.writerow(["Date", "Difference"])

        writer.writerows(new_list)


    #Finding largest increase and decrease
    
    #The average of the changes in "Profit/Losses" over the entire period   
    
    print()
    print()
    print("Financial Analysis")
    print("---------------------------------------------")
    print("Total Months: ",number_of_months, sep="")
    print("Total: $",total_LP, sep="")
    
    #print("Average Change: $","{:.2f}".format(average_LP), sep="")
    #print(f'Greatest Increase in Profits: {greatest_increase}')
    #print(f'Greatest Decrease in Profits: {greatest_decrease}')