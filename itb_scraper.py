from bs4 import BeautifulSoup
import requests

URL = "https://itb.org.tr/ajaxSalon.php?icerik=UzumSalonu"

soup = BeautifulSoup(requests.get(URL).content, features="html.parser")

tables = soup.find_all("table")

def get_volumes():
    daily_volume = {}
    vol_table = tables[0]
    table_headers = vol_table.find_all("th")
    table_data = vol_table.find_all("td")
    volume_total = 0

    for i in range(1,3):
        daily_volume[table_headers[i].text.strip()] = int(table_data[i].text.strip())
        volume_total += int(table_data[i].text.strip())

    daily_volume['Total Volume'] = volume_total

    return daily_volume
    #{'Tüccar(Trader)(Ton)': 60, 'Tariş(Taris Coop)(Ton)': 0, 'Total Volume': 60}

def get_prices():
    if get_volumes().get('Total Volume') > 0:
        data = []
        prices = {}
        vol_table = tables[1]
        table_rows = vol_table.find_all("td")
        for row in table_rows:
            data.append(row.text.strip())
        data_len = int(len(data) / 2)
        for i in range(data_len):
            row = 2 * i
            price = int(data[row + 1].replace(',', '')) / 1000
            if price > 0:
                prices[data[row]] = price
        print(prices)
            #print(row_data.text.strip())
        #row_data = table_rows.find_all("td")
        #for header in table_headers:
            #print(header.text.strip()[-4:])

def get_itb_data():
    pass

if __name__ == '__main__':
    get_prices()
