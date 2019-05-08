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
    max_inc = 0
    max_dec = 0

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

    # Creating new CSV file to get requested values
    new_list = zip(dates, diffs)
    output_file = os.path.join("output.csv")
    with open(output_file, "w", newline="") as datafile:
        writer = csv.writer(datafile)
        writer.writerows(new_list)

    #Finding largest increase and decrease
    new_list_csv = os.path.join('output.csv')
    # Read in the CSV file
    with open(new_list_csv, 'r') as csvlist:

        # Split the data on commas
        csvreader2 = csv.reader(csvlist, delimiter=',')

        for list_row in csvreader2:
            if int(list_row[1]) > int(max_inc):
                max_inc = list_row[1]
                max_inc_date = list_row[0]
            elif int(list_row[1]) < int(max_dec):
                max_dec = list_row[1]
                max_dec_date = list_row[0]

    #The average of the changes in "Profit/Losses" over the entire period   
    average_LP = sum(diffs) / (len(diffs) -1)
    
    #Formating output
    print()
    print()
    print("Financial Analysis")
    print("---------------------------------------------")
    print("Total Months: ",number_of_months, sep="")
    print("Total: $",total_LP, sep="")
    print("Average Change: $","{:.2f}".format(average_LP), sep="")
    print("Greatest Increase in Profits: ",max_inc_date, " ($",max_inc,")", sep="")
    print("Greatest Decrease in Profits: ",max_dec_date, " ($",max_dec,")", sep="")
    print()
    print()
   