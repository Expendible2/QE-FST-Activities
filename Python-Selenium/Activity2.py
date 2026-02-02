from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/login-form")
    print(driver.title)
    driver.find_element(By.ID,"username").send_keys("admin")
    driver.find_element(By.ID,"password").send_keys("password")
    driver.find_element(By.XPATH,"//button[@class='svelte-1pdjkmx']").click()
    print(driver.title)
    time.sleep(4)
    driver.quit()
    
    
    