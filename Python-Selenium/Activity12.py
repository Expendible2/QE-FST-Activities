from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Firefox() as driver:
    wait=WebDriverWait(driver,30)
    driver.get("https://training-support.net/webelements/dynamic-content")

    print(driver.title)
    button_click=driver.find_element(By.XPATH,"//button[@id='genButton']")
    button_click.click()  
    wait.until(EC.text_to_be_present_in_element((By.XPATH,"//h2[@id='word']"),"release"))   
    e1=driver.find_element(By.XPATH,"//h2[@id='word']")

    print("text is found",e1.text)
    