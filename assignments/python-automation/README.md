# 📘 Assignment: Python Automation with CSV File I/O

## 🎯 Objective

Practice Python automation by working with CSV files, file input/output, and basic data processing. Students will build tools that read inventory data, update records, and generate reports automatically.

## 📝 Tasks

### 🛠️ Task 1: Read and Analyze CSV Data

#### Description

Read the provided inventory CSV file and calculate useful summary information. Students will load the data into Python, compute totals, and identify records that need attention.

#### Requirements
Completed program should:

- Read `inventory.csv` using Python's built-in `csv` module.
- Calculate and print the total number of items in inventory.
- Calculate and print the total inventory value using `quantity * price`.
- Print a list of products with low stock (quantity less than 5).
- Use clear and user-friendly output formatting.

### 🛠️ Task 2: Update Inventory Records

#### Description

Add functions that modify inventory data and save the changes back to a CSV file. Students will practice editing rows and writing updated CSV data.

#### Requirements
Completed program should:

- Add a new product record to the inventory.
- Update the quantity for at least one existing product.
- Save the updated inventory to a new file, such as `inventory_updated.csv`.
- Preserve the original CSV header and data structure.
- Include error handling for file read/write operations.

### 🛠️ Task 3: Automate Backup and Reporting

#### Description

Create automation tools that keep inventory data safe and generate a quick summary report. Students will package functionality into reusable functions.

#### Requirements
Completed program should:

- Create a backup copy of the original `inventory.csv` file.
- Generate a text report named `inventory_report.txt` summarizing total items, total inventory value, and low-stock products.
- Use functions for each major step: loading data, updating inventory, backing up files, and generating reports.
- Include comments explaining the purpose of each function.

## 🚀 Getting Started

1. Open `starter-code.py` to explore the helper functions.
2. Run the script with `python starter-code.py`.
3. Confirm the output files `inventory_updated.csv`, `inventory_report.txt`, and backup copies are created.

## 📚 Resources

- [Python csv module](https://docs.python.org/3/library/csv.html)
- [Working with files in Python](https://realpython.com/working-with-files-in-python/)
- [Python functions and error handling](https://docs.python.org/3/tutorial/errors.html)
