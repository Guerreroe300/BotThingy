from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import telegram_send
import time

from datetime import datetime

options = Options()
options.headless = True
browser  = webdriver.Chrome(ChromeDriverManager().install(), options = options)

browser.get('https://asset.party/get/developer/preview')

telegram_send.send(messages=["Prueba"])

while True:
    test = browser.find_element(By.CSS_SELECTOR, ".card > controls:nth-child(2) > div:nth-child(1)").text

    separado = test.split()

    keys = int(separado[1])

    gente = int(separado[3])

    now = datetime.now()

    timen = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

    while keys != 0:
        test = browser.find_element(By.CSS_SELECTOR, ".card > controls:nth-child(2) > div:nth-child(1)").text
        separado = test.split()
        keys = int(separado[1])
        gente = int(separado[3])
        
        telegram_send.send(messages=["Rifa de s&box ahora " + str(keys) + " disponibles"])
        time.sleep(3)

    if int(now.minute) == 0 and int(now.second) >= 0 and int(now.second) <= 20:
        telegram_send.send(messages=["Todo bien son las: " + timen])
    
    if (int(now.minute) == 0 or int(now.minute) == 30) and int(now.second) >= 0 and int(now.second) <= 20:
        print("Las llaves ahorita son " + str(keys) + " y la gente " + str(gente) + " son las " + timen)

    time.sleep(10)