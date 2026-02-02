from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Firefox() as driver:
    driver.implicitly_wait(10)
    driver.get("https://training-support.net/webelements/dynamic-controls")
    print(driver.title)
    check=driver.find_element(By.XPATH,"//input[@id='checkbox']")
    toggle=driver.find_element(By.XPATH,"(//button[@class='svelte-sfj3o4'])[1]")
    toggle.click()
    toggle.click()
    check.click()