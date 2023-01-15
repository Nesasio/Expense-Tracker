# A Simple Balance Sheet Application built in Python

# Author: Light, Github: https://github.com/Nesasio
# Status: Development

# ================================================

import os
import sys
import csv

# ================================================

initialAmount = 20882.44

# A list for storing the all the inidividual costs
cost = []

# ================================================

# Function for reading and displaying the data 

def Display():    
    with open('data.csv') as dataFile:

        csv_reader = csv.reader(dataFile, delimiter = ',')
        line_count = 0

        for row in csv_reader:
            print(f"{row[0]} : {row[1]}")

            if line_count == 0:
                line_count += 1

            else:
                value = float(row[1])
                cost.append(value)
                line_count += 1


    # -------------------------------------

    # Calculating the total expenditure
    totalCost = 0            
    for item in cost:
        totalCost += item

    # -------------------------------------

    # Printing the total cost
    print("----------------------")
    print(f"Total Cost : {totalCost}")

    # -------------------------------------

    # Calculating and printing the balance
    balance = initialAmount - totalCost
    print("----------------------")
    print(f"Balance : {balance}")
    print("======================")


# ================================================

print("\n====== Expense Report ======\n")

# Displaying the data
Display()

# Taking user input
add = int(input("\nEnter 1 to add item to the list or 2 to quit: "))

if add == 1:
    source = str(input("--> Enter the name of the item to be added: "))
    cost = str(input(f"--> Enter the amount spent on {source}: "))

    with open('data.csv', 'a', newline='') as dataFile:
        writer = csv.writer(dataFile, delimiter=',')
        #writer.writerow([])
        writer.writerow([f'{source}', f'{cost}'])
        dataFile.close()

    print(f"\n{source} has been added to the report")

elif add == 2:
    sys.exit("Quitting!")

else:
    print("Error: I said to enter either 1 or 2, can't you see the numbers you moron!")

# ==================== END OF PROGRAM ===========================