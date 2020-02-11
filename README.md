# Automate Your Day Job with Python

Python scripts were written to analyze two hypothetical companys' financial records, PyBank and PyRamen, to automate daily workflow processes. 

### PyBank
In PyBank, budget data was provided and Python was used to calculate PNL (profit and loss). Metrics included net total amount of PNL of the entire period, the average of the changes in PNL, the greatest increase in profits with data and amount over the entire period and greatest decrease. 

A `main.py` file was created and the `pathlib` and `csv` libraries were imported to read in the budget data. 

````

# Open the csv file as an object
with open(csvpath, 'r') as csvfile:
    # Pass in the csv file to the csv.reader() function and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
     # Read the header to skip in loop
    csv_header = next(csvreader)
    
````

The final output was pushed to a .txt file:

Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-12 ($1926159)
Greatest Decrease in Profits: Sep-13 ($-2196167)

