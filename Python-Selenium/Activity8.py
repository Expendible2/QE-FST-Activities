from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
with webdriver.Firefox() as driver:
    
    driver.get("https://training-support.net/webelements/mouse-events")
    print(driver.title)
    e1=driver.find_element(By.XPATH,"//h1[contains(text(),'Cargo.lock')]")
    actions=ActionChains(driver)
    actions.click(e1).perform()
    e2=driver.find_element(By.XPATH,"//h1[contains(text(),'Cargo.toml')]")
    actions.move_to_element(e2).perform()
    actions.click(e2).perform()
    print(driver.find_element(By.XPATH,"//p[@id='result']").text)
    e3=driver.find_element(By.XPATH,"//h1[contains(text(),'src']")
    actions.move_to_element(e3).perform()
    actions.double_click(e3).perform()
    e4=driver.find_element(By.XPATH,"//h1[contains(text(),'target')]")
    actions.move_to_element(e4).perform()
    actions.context_click(e4).perform()
    print(driver.find_element(By.XPATH,"//p[@id='result']").text)
    
    