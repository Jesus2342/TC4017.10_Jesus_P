"""
Instituto Tecnologico y de Estudios Superiores de Monterrey
Student: Jose de Jesus Pena Rodriguez
Student ID: A01794940
Programming Exercise: Compute sales
Description: The program shall compute the total cost for all sales

Usage:
Type the name of the text file in INPUT_FILE then
run ---> python compute_sales.py TC1.ProductList.json TC1.Sales.json
run ---> python compute_sales.py TC1.ProductList.json TC2.Sales.json
run ---> python compute_sales.py TC1.ProductList.json TC3.Sales.json
"""""

import sys
import json
import time

start_time = time.time()

PRODUCT_LIST_JSON = sys.argv[1]
sales_list_json = sys.argv[2]
system_output = []
TEST_CASE = "TC3"
AUX_TITLE = "SalesResults_"
OUTPUT_FILE = AUX_TITLE+TEST_CASE+".txt"

if len(sys.argv) != 3:
    system_output.append(">>>>Files were NOT entered, try again!!>>>>")
    sys.exit(1)


system_output.append(f"Results from {TEST_CASE}")
system_output.append("-------------------------------------------")
system_output.append("Files to be processed")
system_output.append(f"Product list ----> {PRODUCT_LIST_JSON}")
system_output.append(f"Sales list  -----> {sales_list_json}")


try:
    with open(PRODUCT_LIST_JSON, "r", encoding="utf-8") as file:
        PRODUCT_LIST_JSON = json.load(file)
        system_output.append("-------------------------------------------")
        system_output.append("** Product list loaded")
except FileNotFoundError:
    error_msg_1 = f"Error: Product list {PRODUCT_LIST_JSON} not found."
    print(error_msg_1)
    system_output.append(error_msg_1)
    sys.exit(1)
try:
    with open(sales_list_json, "r", encoding="utf-8") as file:
        sales_list_json = json.load(file)
        system_output.append("** Sales list loaded")
        system_output.append("-------------------------------------------")
except FileNotFoundError:
    error_msg_2 = f"Error: Sales list {sales_list_json} not found."
    print(error_msg_2)
    system_output.append(error_msg_2)
    sys.exit(1)
TOTAL_SALES = 0
for sale in sales_list_json:
    product_name = sale["Product"]
    quantity = sale["Quantity"]
    PRODUCE_PRICE = None
    for product in PRODUCT_LIST_JSON:
        if product["title"] == product_name:
            PRODUCE_PRICE = product["price"]
            break
    if PRODUCE_PRICE is not None:
        cost = PRODUCE_PRICE * quantity
        TOTAL_SALES += cost
    else:
        error_msg3 = f"Product {product_name} not found in product list"
        print(error_msg3)
        system_output.append(error_msg3)
system_output.append(f"Total is {round(TOTAL_SALES,2)}")
system_output.append("-------------------------------------------")

end_time = time.time()
execution_time = round(end_time - start_time, 4)
system_output.append(f"Execution Time: {execution_time} seconds")
system_output.append("-------------------------------------------")

for line in system_output:
    print(line)
with open(OUTPUT_FILE, "w", encoding="utf-8") as report_file:
    for line in system_output:
        report_file.write(line + "\n")
    report_file.write("\n")