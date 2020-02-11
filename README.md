# Automate Your Day Job with Python

Python scripts were written to analyze two hypothetical companys' financial records, PyRamen and PyBank, to automate daily workflow processes. 

### PyRamen

PyRamen is a ramen shop that has been in business for two years and the owner would like to evaluate the financial performance of the business. The business is growing and maintaining the analysis and data in Excel is not sufficient. Python provides a wide range of capabilities for handling data, harnessing the power of low-level Python data structures and high-level development libraries, while supporting the automation and scalability needs for a growing enterprise.

The owner provides sales data that needs to be cross-referenced with internal menu data to perform calculations. The calculations of interest include total revenue and costs, and on a per-product basis to understand which products are doing well, which are doing poorly, and which products need to be removed.  

A `main.py` script was created, and the `pathlib` and `csv` libraries were imported to read in the sales and menu data files. Within the script, lists were created to hold the menu and sales data as objects in Python and a dictionary was initialized to hold the future aggregated per-product resulsts:  

Python Lists: 

````
menu = []
sales = []

````
Python Dictionary: 

````
#The report dictionary will eventually contain the following metrics:
#01-count: the total quantity for each ramen type
#02-revenue: the total revenue for each ramen type
#03-cogs: the total cost of goods sold for each ramen type
#04-profit: the total profit for each ramen type
#report = {" ": {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0,} }
report = { }

````

The final results and summary from the script were pushed to a .txt file 

````
PyRamen
----------------------------
nagomi shoyu {'01-count': 9132, '02-revenue': 100452.0, '03-cogs': 45660.0, '04-profit': 54792.0}
shio ramen {'01-count': 9180, '02-revenue': 100980.0, '03-cogs': 45900.0, '04-profit': 55080.0}
spicy miso ramen {'01-count': 9238, '02-revenue': 110856.0, '03-cogs': 46190.0, '04-profit': 64666.0}
vegetarian spicy miso {'01-count': 9216, '02-revenue': 110592.0, '03-cogs': 46080.0, '04-profit': 64512.0}
miso crab ramen {'01-count': 8890, '02-revenue': 106680.0, '03-cogs': 53340.0, '04-profit': 53340.0}
soft-shell miso crab ramen {'01-count': 9130, '02-revenue': 127820.0, '03-cogs': 63910.0, '04-profit': 63910.0}
tori paitan ramen {'01-count': 9156, '02-revenue': 119028.0, '03-cogs': 54936.0, '04-profit': 64092.0}
tonkotsu ramen {'01-count': 9288, '02-revenue': 120744.0, '03-cogs': 55728.0, '04-profit': 65016.0}
burnt garlic tonkotsu ramen {'01-count': 9070, '02-revenue': 126980.0, '03-cogs': 54420.0, '04-profit': 72560.0}
vegetarian curry + king trumpet mushroom ramen {'01-count': 8824, '02-revenue': 114712.0, '03-cogs': 61768.0, '04-profit': 52944.0}
truffle butter ramen {'01-count': 8982, '02-revenue': 125748.0, '03-cogs': 62874.0, '04-profit': 62874.0}

````


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

````

Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-12 ($1926159)
Greatest Decrease in Profits: Sep-13 ($-2196167)

````



