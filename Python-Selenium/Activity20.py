from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Firefox() as driver:    
    driver.get("https://training-support.net/webelements/alerts")
    print(driver.title)
    prompt=driver.find_element(By.XPATH,"//button[@id='prompt']")
    prompt.click()
    time.sleep(2)
    alert3=driver.switch_to.alert
    print(alert3.text)
    alert3.send_keys("Exit")
    alert3.accept()
    res=driver.find_element(By.XPATH,"//p[@id='result']")
    print(res.text)
    time.sleep(2)