from selenium import webdriver
import time
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/target-practice")
    print(driver.title)
    print(driver.find_element(By.XPATH,"//h3[@class='text-3xl font-bold text-orange-600']").text)
    e1=driver.find_element(By.XPATH,"//h5[@class='text-3xl font-bold text-purple-600']")
    print(e1.value_of_css_property("color"))
    e2=driver.find_element(By.CLASS_NAME,"bg-purple-200")
    print(e2.get_attribute("class"))
    print(driver.find_element(By.CLASS_NAME,"bg-slate-200").text)    
    driver.quit()
        