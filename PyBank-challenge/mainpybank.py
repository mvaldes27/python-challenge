# Modules
import os
import csv
#import numpy as np

# Lists to store data 
months = []
profit_loss = []
monthly_changes = []


# Set path for file
budget_csv = os.path.join("Resources", "budget_data.csv")


# Open CSV Path and specify delimiter
with open(budget_csv) as csv_file:    
    budget_csv = csv.reader(csv_file, delimiter=",")
    

    # Read header row first 
    csv_header = next(csv_file)

    #initialize variables
    greatest_increase = 0
    greatest_decrease = 0
    current = 0
    past = 0
    month_increase = ""
    month_decrease = ""
    


    for i, row in budget_csv:

        # add all months to list 
        months.append(row[0]) 
        # add all PL values to list and save as type float   
        profit_loss.append(float(row[1]))

        # create variables to store calculations
        total_num_months = len(months)
        profit_loss_net_total = sum(profit_loss)

        if i > 0:
            current = int(row[1])
            monthly_changes.append(current - past)     

    #for value in profit_loss:

        #find value of different between months at index 1 and 0
        #month_change = profit_loss[1] - profit_loss[0] 
        
        # add month change value to changes list
        #monthly_changes.append(month_change)

        #pop off next value at position 0
        #profit_loss.pop(0)

    #create variable to store AVG Month change
    #avg_monthly_change = round(sum(monthly_changes)/len(monthly_changes), 2)
    #avg_monthly_change = np.mean(monthly_changes)



        
    
    # Testing the outputs

    print(total_num_months)
    
    print(profit_loss_net_total)

    print(monthly_changes)

    print(sum(monthly_changes))

    print(len(monthly_changes))

    print(avg_monthly_change)









