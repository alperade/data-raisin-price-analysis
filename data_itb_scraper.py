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

    daily_volume['Total Volume (Ton)'] = volume_total

    return daily_volume

def get_prices():
    if get_volumes().get('Total Volume (Ton)') > 0:
        data = []
        prices_raw = {}
        prices = {}
        price_table = tables[1]
        atypical = ['Çek.siz Kuru Üzüm Bandırmasız', 'Çek.siz Kuru Üzüm Bandırmasız (-)', 'Çek.siz Kuru Üzüm Bandırmasız (Eski Mahsül)']
        table_rows = price_table.find_all("td")
        for row in table_rows:
            data.append(row.text.strip())
        data_len = len(data) // 2
        for i in range(data_len):
            row = 2 * i
            price = int(data[row + 1].replace(',', '')) / 1000
            prices_raw[data[row]] = price

        for key in prices_raw:
            if key[-6:] == '(Std.)':
                prices[key[18:-7]] = prices_raw[key]
        for type in atypical:
            prices[type[18:]] = prices_raw[type]
        prices['ÇEKİRDEKSİZ KURU ÜZÜM'] = prices_raw['ÇEKİRDEKSİZ KURU ÜZÜM']

        return prices


def get_itb_data():
    if get_volumes().get('Total Volume (Ton)') > 0:
        volume = get_volumes()
        prices = get_prices()
        return volume | prices


if __name__ == '__main__':
    print(get_itb_data())
