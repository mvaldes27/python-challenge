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

    
    for row in csv_reader:

        # add all months to list 
        months.append(row[0]) 
        # add all PL values to list and save as type float   
        profit_loss.append(float(row[1]))
       

        #create variables to store calculations
        total_num_months = (len(months))
        profit_loss_net_total = sum(profit_loss)
        month_change = profit_loss(float([row + 1]) - profit_loss(float([row])

        # add month_change values into monthly_changes list
        monthly_changes.append(float(month_change))


    

        

            


    
    # Testing the outputs
        
    
    print(total_num_months)
    
    print(profit_loss_net_total)

    print(month_change)









