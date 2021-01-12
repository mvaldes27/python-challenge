# Modules
import os
import csv

# Lists to store data 
months = []
profit_loss = []
monthly_changes = []

# Create function that calculates changes in P/L and returns AVG of those changes

# Set path for file
budget_csv = os.path.join("Resources", "budget_data.csv")


# Open CSV Path and specify delimiter
with open(budget_csv, newline='', encoding='utf-8') as csv_file:    
    csv_reader = csv.reader(csv_file, delimiter=",")
    

    # Read header row first 
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Calculate the difference between first two months
    #first_month_change = profit_loss[1] - profit_loss[0]
    # Add this value to monthly_changes list
    #monthly_changes.append(first_month_change)
    
    #pop off first value of profit loss list
    #profit_loss.pop(0)

    for row in csv_reader:

        # add all months to list 
        months.append(row[0]) 
        # add all PL values to list and save as type float   
        profit_loss.append(float(row[1]))

        # create variables to store calculations
        total_num_months = len(months)
        profit_loss_net_total = sum((profit_loss))   

    for value in profit_loss:

        #find value of different between months at index 1 and 0
        month_change = profit_loss[1] - profit_loss[0] 
        
        # add month change value to changes list
        monthly_changes.append(month_change)

        #pop off next value at position 0
        profit_loss.pop(0)

        #create variable to store AVG Month change
        avg_monthly_change = sum(monthly_changes)/len(monthly_changes)

        
    
    # Testing the outputs

    print(total_num_months)
    
    print(profit_loss_net_total)

    print(monthly_changes)

    print(avg_monthly_change)


#Python - Lists,Dictionaries,Functions,Looping through lists(by item wise & by index wise)






