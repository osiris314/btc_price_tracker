import requests
import time
from bs4 import BeautifulSoup
import datetime
from colorama import (init, Fore)
import os
from playsound import playsound

init()
os.system('cls')

def run_tracker():
    url = 'https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD&.tsrc=fin-srch'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    price = soup.find_all('div', {'class':'D(ib) smartphone_Mb(10px) W(70%) W(100%)--mobp smartphone_Mt(6px)'})[0].find('span').text
    return price

last_price = 0.0
float_last_price = float(last_price)

print('Current Btc value: ', run_tracker(), '$')
bell_value = input('Notify me if value is under: ')
print('')

while True:
    ts = datetime.datetime.now()
    current_price = run_tracker()
    corrected_current_price_1 = current_price.replace('.','')
    corrected_current_price_final = corrected_current_price_1.replace(',','')
    corrected_current_price_final = float(corrected_current_price_final)

    def bell_check():
        if (int(corrected_current_price_final/100) < int(bell_value)) :
            print(' 🔔')
            playsound('alert.wav')

    if (corrected_current_price_final > float_last_price):
        change = corrected_current_price_final - float_last_price
        print ('BitCoin: ', end = '')
        print(run_tracker(), '$', end = '')
        print (' | ', end = '')
        print(ts, end = '')
        print (' | ', end = '')
        print(Fore.GREEN + ' UP', end = '')
        print (' +', end = '')
        print(change / 100, end = '')
        print(' $', end = '')
        print(Fore.WHITE + '', end = '')
        float_last_price = corrected_current_price_final
        bell_check()
        print('')

    elif (corrected_current_price_final < float_last_price):
        change = float_last_price - corrected_current_price_final
        print ('BitCoin: ', end = '')
        print(run_tracker(), '$', end = '')
        print (' | ', end = '')
        print(ts, end = '')
        print (' | ', end = '')
        print(Fore.RED + ' DOWN', end = '')
        print (' -', end = '')
        print(change / 100, end = '')
        print(' $', end = '')
        print(Fore.WHITE + '', end = '')
        float_last_price = corrected_current_price_final
        bell_check()
        print('')

    time.sleep(5)
