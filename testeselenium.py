from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

drive = webdriver.Chrome()
drive.get("https://www.google.com/")
drive.find_element(By.NAME, "q").click()
drive.find_element(By.NAME, "q").send_keys("github")
drive.find_element(By.NAME, "q").send_keys(Keys.ENTER)
drive.find_element(By.CSS_SELECTOR, ".tF2Cxc > .yuRUbf .LC20lb").click()
