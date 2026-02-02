from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/alerts") 
    print(driver.title)
    simple=driver.find_element(By.XPATH,"//button[@id='simple']")
    simple.click()
    alert=driver.switch_to.alert
    print(alert.text)
    alert.accept()
    time.sleep(3)
    print(driver.find_element(By.XPATH,"//p[@id='result']").text)
    