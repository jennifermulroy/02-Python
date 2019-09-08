# Import the pathlib and csv library
from pathlib import Path
import csv

Path.cwd()

csvpath = Path('/Users/jenni/Homework/python-homework/budget_data.csv')

# Initialize list of records and variables
monthly_difference = []
month_count = 0 
profit_loss = 0
total = 0 
monthly_pnl_data = []


# Initialize greatest profit key-value pair
greatest_profit_date = ""
greatest_profit_value = 0

# Initialize greatest loss key-value pair
greatest_loss_date = "" 
greatest_loss_value = 0

# Open the csv file as an object
with open(csvpath, 'r') as csvfile:
    # Pass in the csv file to the csv.reader() function and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
     # Read the header to skip in loop
    csv_header = next(csvreader)

    
       
    # Read each row of data 
    for row in (csvreader):
        date = str(row[0])
        #count the number of months and total pnl 
        profit_loss = profit_loss + int(row[1])
        month_count = month_count + 1    
        monthly_pnl_data.append(int(row[1]))
        
                                                     
        if greatest_profit_value == 0:
            greatest_profit_value = int(row[1])
            greatest_profit_date = date
            greatest_loss_value = int(row[1])
            greatest_loss_date = date
        elif int(row[1]) > greatest_profit_value:
            greatest_profit_value = int(row[1])
            greatest_profit_date = date 
        if int(row[1]) < greatest_loss_value:
            greatest_loss_value = int(row[1])
            greatest_loss_date = date
    
    
        # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(monthly_pnl_data)-1):
        
        monthly_difference.append(monthly_pnl_data[i+1]-monthly_pnl_data[i])
        max_increase_value = max(monthly_difference)
        max_decrease_value = min(monthly_difference)
    
    for pnl in monthly_difference:
        total = total + pnl 
    #print(total)    
    average_difference = round(total/len(monthly_difference),2)
    
    
    print("Total Months:", month_count)
    print(f"Total ${profit_loss}")
    print(f"Average Change: ${average_difference}")
    print (f"The Greatest Increase in Profits: {greatest_profit_date} (${max_increase_value})")
    print (f"The Greatest Decrease in Profits: {greatest_loss_date} (${max_decrease_value})")    

    # Output files
output_file = Path("Financial_Analysis_Summary.txt")
                   
with open(output_file,"w") as file:
                   
# Write methods to print to Financial_Analysis
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {month_count}")
    file.write("\n")
    file.write(f"Total: ${profit_loss}")
    file.write("\n")
    file.write(f"Average Change: ${average_difference}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {greatest_profit_date} (${max_increase_value})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {greatest_loss_date} (${max_decrease_value})")