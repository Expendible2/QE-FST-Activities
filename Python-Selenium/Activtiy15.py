from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/dynamic-attributes")
    print(driver.title)
    user=driver.find_element(By.XPATH,"//input[@placeholder='Full name']")
    user.send_keys("Person1")
    pas=driver.find_element(By.XPATH,"//input[@placeholder='Email Address']")
    pas.send_keys("abc@gmail.com")
    dat=driver.find_element(By.XPATH,"//input[contains(@name,'-event-date-')]")
    dat.send_keys("2025-01-24")
    add_det=driver.find_element(By.XPATH,"//textarea[contains(@name,'-additional-details-')]")
    add_det.send_keys("nothing")
    submit=driver.find_element(By.XPATH,"//button[@class='font-bold svelte-7bqce9']")
    submit.click()
    res=driver.find_element(By.XPATH,"//h3[@id='action-confirmation']")
    print(res.text)
    time.sleep(3)