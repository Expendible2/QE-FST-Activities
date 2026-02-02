from selenium import webdriver
from selenium.webdriver.common.by import By
import time

    
with webdriver.Firefox() as driver:    
    driver.get("https://training-support.net/webelements/alerts")
    print(driver.title)
    confirm=driver.find_element(By.XPATH,"//button[@id='confirmation']")
    confirm.click()
    alert=driver.switch_to.alert
    print(alert.text)
    alert.accept()
    time.sleep(2)
    res=driver.find_element(By.XPATH,"//p[@id='result']")
    print(res.text)
    confirm.click()
    alert.dismiss()
    time.sleep(2)
    print(res.text)
    