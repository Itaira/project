import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("/Users/itairaviv/Downloads/chromedriver_mac_arm64/chromedriver"))
driver.implicitly_wait(10) #Wait max 10 seconds to find element

driver.get("http://localhost:5001/users/get_user_data/1") #Open the driver on google.com

