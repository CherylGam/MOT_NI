import csv

data = []

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    for row in spreadsheet:
        monthly_sales = int(row['sales'])
        data.append(monthly_sales)


total_sales = sum(data)

print(f'The total sales for the year 2018 is £ {total_sales}')






