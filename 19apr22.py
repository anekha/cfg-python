import csv

def read_data():
    data = []

    with open('sales.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet:
            data.append(row)
    
    return data 

def run():
    data = read_data()

    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

        total = sum(sales)
        print('Total sales:{}'.format(total))
    lowest_sale = min(sales)
    print(lowest_sale)
    highest_sale = max(sales)
    print(highest_sale)
    average_sale = total/len(sales)
    print(average_sale)
run()








