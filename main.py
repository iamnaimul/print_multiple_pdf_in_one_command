from selenium import webdriver
from time import sleep
import os

urls = []
for file in os.listdir():
    a, b = os.path.splitext(file)
    if b == '.pdf':
        urls.append(os.path.join(os.getcwd(), file))
        
for url in urls:
    path = "C:\Program Files (x86)\chromedriver.exe"
    browser = webdriver.Chrome(path)
    browser.maximize_window()
    browser.get(url)
    browser.implicitly_wait(1)

    browser.execute_script('window.print();')

    sleep(5)
    browser.close()
