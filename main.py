from weather import get_weather
from fx import get_fx
import csv
from datetime import date


def create_csv():
    with open('./raisin_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Temperature', 'USDTRY']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


def update_csv():
    fieldnames = ['Date', 'Temperature', 'USDTRY']
    today = date.today()
    temperature = get_weather()
    usdtry = get_fx()
    print(temperature)
    print(usdtry)
    new_row = {'Date': today, 'Temperature': temperature, 'USDTRY': usdtry}
    with open('./raisin_data.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(new_row)

if __name__ == '__main__':
    update_csv()
