from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/tables")
    print(driver.title)
    tcol=driver.find_elements(By.XPATH,"//table/thead/tr//th")
    print("total column:",len(tcol))
    trow=driver.find_elements(By.XPATH,"//table/tbody//tr")
    print("total rows:",len(trow))
    thirdr=driver.find_element(By.XPATH,"//table/tbody//tr[3]")
    print("the data in:",thirdr.text)
    secondrow=driver.find_element(By.XPATH,"//table/tbody//tr[2]/td[2]")
    print("data is second row and second column is:",secondrow.text)