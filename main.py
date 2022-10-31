from weather import get_weather
from fx import get_fx
import csv
from datetime import date

fieldnames = [
    'Date',
    'Temperature',
    'USDTRY',
    'Tüccar(Trader)(Ton)',
    'Tariş(Taris Coop)(Ton)',
    ]




{'ÇEKİRDEKSİZ KURU ÜZÜM': '0,000', 'Çek.siz Kuru Üzüm 11 (+) (Jumbo)': '0,000', 'Çek.siz Kuru Üzüm 11 (+) (Std.)': '0,000', 'Çek.siz Kuru Üzüm 11 (+) (Med.)': '0,000', 'Çek.siz Kuru Üzüm 11 (+) (Small)': '0,000', 'Çek.siz Kuru Üzüm 11 (Std.) (Jumbo)': '0,000', 'Çek.siz Kuru Üzüm 11 (Std.) (Std.)': '0,000', 'Çek.siz Kuru Üzüm 11 (Std.) (Med.)': '0,000', 'Çek.siz Kuru Üzüm 11 (Std.) (Small)': '0,000', 'Çek.siz Kuru Üzüm 11 (-) (Jumbo)': '0,000', 'Çek.siz Kuru Üzüm 11 (-) (Std.)': '0,000', 'Çek.siz Kuru Üzüm 11 (-) (Med.)': '0,000', 'Çek.siz Kuru Üzüm 11 (-) (Small)': '0,000', 'Çek.siz Kuru Üzüm 10 (+) (Jumbo)': '0,000', 'Çek.siz Kuru Üzüm 10 (+) (Std.)': '0,000', 'Çek.siz Kuru Üzüm 10 (+) (Med.)': '0,000', 'Çek.siz Kuru Üzüm 10 (+) (Small)': '0,000', 'Çek.siz Kuru Üzüm 10 (Std.) (Jumbo)': '0,000', 'Çek.siz Kuru Üzüm 10 (Std.) (Std.)': '0,000', 'Çek.siz Kuru Üzüm 10 (Std.) (Med.)': '0,000', 'Çek.siz Kuru Üzüm 10 (Std.) (Small)': '0,000', 'Çek.siz Kuru Üzüm 10 (-) (Jumbo)': '0,000', 'Çek.siz Kuru Üzüm 10 (-) (Std.)': '0,000', 'Çek.siz Kuru Üzüm 10 (-) (Med.)': '0,000', 'Çek.siz Kuru Üzüm 10 (-) (Small)': '0,000', 'Çek.siz Kuru Üzüm 9 (+) (Jumbo)': '0,000', 'Çek.siz Kuru Üzüm 9 (+) (Std.)': '0,000', 'Çek.siz Kuru Üzüm 9 (+) (Med.)': '0,000', 'Çek.siz Kuru Üzüm 9 (+) (Small)': '0,000', 'Çek.siz Kuru Üzüm 9 (Std.) (Jumbo)': '0,000', 'Çek.siz Kuru Üzüm 9 (Std.) (Std.)': '22,500', 'Çek.siz Kuru Üzüm 9 (Std.) (Med.)': '0,000', 'Çek.siz Kuru Üzüm 9 (Std.) (Small)': '0,000', 'Çek.siz Kuru Üzüm 9 (-) (Jumbo)': '0,000', 'Çek.siz Kuru Üzüm 9 (-) (Std.)': '21,500', 'Çek.siz Kuru Üzüm 9 (-) (Med.)': '0,000', 'Çek.siz Kuru Üzüm 9 (-) (Small)': '0,000', 'Çek.siz Kuru Üzüm 8 (+) (Jumbo)': '0,000', 'Çek.siz Kuru Üzüm 8 (+) (Std.)': '0,000', 'Çek.siz Kuru Üzüm 8 (+) (Med.)': '0,000', 'Çek.siz Kuru Üzüm 8 (+) (Small)': '0,000', 'Çek.siz Kuru Üzüm 8 (Std.) (Jumbo)': '0,000', 'Çek.siz Kuru Üzüm 8 (Std.) (Std.)': '20,000', 'Çek.siz Kuru Üzüm 8 (Std.) (Med.)': '0,000', 'Çek.siz Kuru Üzüm 8 (Std.) (Small)': '0,000', 'Çek.siz Kuru Üzüm 8 (-) (Jumbo)': '0,000', 'Çek.siz Kuru Üzüm 8 (-) (Std.)': '0,000', 'Çek.siz Kuru Üzüm 8 (-) (Med.)': '0,000', 'Çek.siz Kuru Üzüm 8 (-) (Small)': '0,000', 'Çek.siz Kuru Üzüm 7 (+) (Jumbo)': '0,000', 'Çek.siz Kuru Üzüm 7 (+) (Std.)': '0,000', 'Çek.siz Kuru Üzüm 7 (+) (Med.)': '0,000', 'Çek.siz Kuru Üzüm 7 (+) (Small)': '0,000', 'Çek.siz Kuru Üzüm 7 (Std.) (Jumbo)': '0,000', 'Çek.siz Kuru Üzüm 7 (Std.) (Std.)': '0,000', 'Çek.siz Kuru Üzüm 7 (Std.) (Med.)': '0,000', 'Çek.siz Kuru Üzüm 7 (Std.) (Small)': '0,000', 'Çek.siz Kuru Üzüm 7 (-) (Small)': '0,000', 'Çek.siz Kuru Üzüm 7 (-) (Med.)': '0,000', 'Çek.siz Kuru Üzüm 7 (-) (Std.)': '0,000', 'Çek.siz Kuru Üzüm 7 (-) (Jumbo)': '0,000', 'Çek.siz Kuru Üzüm (Eski Mahsul)': '0,000', 'Çek.siz Kuru Üzüm Bandırmasız': '0,000', 'Çek.siz Kuru Üzüm Bandırmasız (-)': '0,000', 'Çek.siz Kuru Üzüm Bandırmasız (Eski Mahsül)': '0,000'}

def create_csv():
    with open('./raisin_data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


def update_csv():
    today = date.today()
    temperature = get_weather()
    usdtry = get_fx()
    new_row = {'Date': today, 'Temperature': temperature, 'USDTRY': usdtry}
    with open('./raisin_data.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(new_row)

if __name__ == '__main__':
    update_csv()
