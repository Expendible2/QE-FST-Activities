from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/drag-drop")
    print(driver.title)
    driver.maximize_window()
    ball=driver.find_element(By.XPATH,"//img[@id='ball']")
    drop=driver.find_element(By.XPATH,"//div[@id='dropzone2']")
    droptext=driver.find_element(By.XPATH,"//div[@id='dropzone2']//span[@class='dropzone-text svelte-lit24y']")
    actions=webdriver.ActionChains(driver)
    actions.drag_and_drop(ball,drop).perform()
    time.sleep(2)
    print(droptext.text)
    
    