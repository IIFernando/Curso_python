# import pandas as pd
from time import sleep as slp
# from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('Endereço para acesso')
slp(5)
browser.close()