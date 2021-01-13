# import modules
import os
import csv 

# Set path for file
budget_csv = os.path.join("Resources", "budget_data.csv")


# Open CSV Path and specify delimiter
with open(budget_csv) as csv_file:    
    budget_csv = csv.reader(csv_file, delimiter=",")

    # Read header row first 
    csv_header = next(csv_file)

    # Create variables
    months = 0
    profit_loss_net = 0
    month_to_month_change = 0
    total_change = 0
    greatest_increase = 0
    greatest_decrease = 0

    for row in budget_csv:

        # add months to the month counter
        months += 1

        # add PL to PL net total
        profit_loss_net += int(row[1])

        # record first month PL value and store in past_month
        if months == 1:
            past_month = int(row[1])

        # for remaining months, find change by subtracting past month from current month
        else:
            month_to_month_change = int(row[1]) - past_month
            total_change += month_to_month_change
            past_month = int(row[1])

       # Record the new change if it is greater than greatest_increase or less than greatest_decrease
        if month_to_month_change > greatest_increase:
            greatest_increase = month_to_month_change
            month_of_max_increase = row[0]

        elif month_to_month_change < greatest_decrease:
            greatest_decrease = month_to_month_change
            month_of_max_decrease = row[0]


    # formula for average change
    avg_change = round(total_change / (months - 1), 2)      

    # export analysis to file
    #set filepath 
    output_path = os.path.join('Analysis', 'Analysis.txt') 
    with open(output_path, 'w') as txtfile: 
        txtfile.write("Financial Analysis \n")
        txtfile.write("------------------ \n")
        txtfile.write(f"Total Months: {months}\n")
        txtfile.write(f"Average Change: ${avg_change}\n")
        txtfile.write(f"Greatest Increase in Profits: {month_of_max_increase} (${greatest_increase})\n")
        txtfile.write(f"Greatest Decrease in Profits: {month_of_max_decrease} (${greatest_decrease})\n")

    # open financial analysis and print results to terminal
    with open(output_path) as show_file:
        print(show_file.read())
        











