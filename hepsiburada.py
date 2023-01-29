import csv

file = open("orders.csv", "r")
orders = list(csv.DictReader(file, delimiter=";"))

fieldnames = [
    orders[0][None][2],
    orders[0][None][8],
    orders[0][None][9],
    orders[0][None][10],
    orders[0][None][11],
    orders[0][None][15],
    'Birim',
    orders[0][None][18],
    orders[0][None][20],
    'Total',
    orders[0][None][23][:8],
    'Net Kar'
    ]

def create_csv():
    with open('./siparis.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

def update_csv():
    try:
        with open('./siparis.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for data in orders[1:]:
                date = data[None][2].split(" ",1)[0]
                name = data[None][8]
                address = data[None][9].split("detay: ",1)[1]
                city = data[None][10]
                town = data[None][11]
                product = data[None][15]
                unit = data[None][16]
                unit_cost = round(int(data[None][18].split(" TRY",1)[0].replace(',', '')) / 10000, 2)
                quantity = int(data[None][20])
                total = round(int(data[None][21].split(" TRY",1)[0].replace(',', '')) / 10000, 2)
                commission = round(int(data[None][23].split(" TRY",1)[0].replace(',', '')) / 10000, 2)
                net_total = round(total - commission, 2)

                row = {
                    fieldnames[0]: date,
                    fieldnames[1]: name,
                    fieldnames[2]: address,
                    fieldnames[3]: city,
                    fieldnames[4]: town,
                    fieldnames[5]: product,
                    fieldnames[6]: unit,
                    fieldnames[7]: unit_cost,
                    fieldnames[8]: quantity,
                    fieldnames[9]: total,
                    fieldnames[10]: commission,
                    fieldnames[11]: net_total
                    }
                writer.writerow(row)

    except:
        print("No transaction on HB")

if __name__ == '__main__':
    create_csv()
    update_csv()
