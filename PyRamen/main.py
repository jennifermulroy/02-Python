# Import libraries
import csv
from pathlib import Path

# Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('/Users/jenni/Homework/python-homework/PyRamen/menu_data.csv')
sales_filepath = Path('/Users/jenni/Homework/python-homework/PyRamen/sales_data.csv')

#Initialize list objects to hold our menu and sales data
menu = []
sales = []

#Initialize dictionary to hold the future aggregated per-product results.
#The report dictionary will eventually contain the following metrics:
#01-count: the total quantity for each ramen type
#02-revenue: the total revenue for each ramen type
#03-cogs: the total cost of goods sold for each ramen type
#04-profit: the total profit for each ramen type
#report = {" ": {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0,} }
report = { }

#initialize variables from the files to pull in the dictionary 
sales_item = 0 
menu_item = 0
price = 0 
cost = 0 
profit = 0 
quantity = 0 

# Read in the menu data into the menu list

with open(menu_filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # Print the header
    #print(csv_header)
    #Loop over the rest of the rows and append every row to the menu list object
    #the outcome is a list of lists if using csvreader 
    for row in csvreader:
        menu.append(row)
    
   #Read in the sales data into the sales list

with open(sales_filepath, 'r') as csvfilesales:
    csvreader = csv.reader(csvfilesales, delimiter=',')
    csv_header = next(csvreader)
    # Print the header
    #print(csv_header)
    #append every row of the sales data to a new sales list object
    for row in csvreader:
        sales.append(row)


for item in menu:
    if item[1] == 'entree':
        #print(item)
        report[str(item[0])] =  {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0,}


for row in sales:
    #For each row of the sales data, set quantity data and sales_items of the sales data to their own variables
    quantity = int(row[3]) #col 3
    sales_item = str(row[4]) #col 4 
    #set sales_item as key in report dictionary 
    report[sales_item]
    #set metrics as values per sales_items key 
    #for values in report.values():
    #report[sales_item] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0,}
    for i in menu: 
        menu_item = str(i[0])
        price = float(i[3])
        cost =  float(i[4])
        #for keys, values in report.items():
        if sales_item == menu_item:
            profit = (price)-(cost)
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity
# print(report)
        #else:
            #print("{sales_item} does not equal {menu_item}! NO MATCH!")

# Output files
output_file = Path("PyRamen.txt")
           
with open(output_file,"w") as file:
                   
# Write methods to print 
    file.write("PyRamen")
    file.write("\n")
    file.write("----------------------------\n")
    for key in report:
        file.write(key+" "+str(report[key])+"\n")