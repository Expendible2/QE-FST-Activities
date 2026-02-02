from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/tables")
    print(driver.title)
    driver.get("https://training-support.net/webelements/tables")
    print(driver.title)
    tcol=driver.find_elements(By.XPATH,"//table/thead/tr//th")
    print("total column:",len(tcol))
    trow=driver.find_elements(By.XPATH,"//table/tbody//tr")
    print("total rows:",len(trow))
    book_5=driver.find_element(By.XPATH,"//table/tbody/tr[5]/td[2]")
    print("The Book_name in the 5th row is:",book_5.text)
    price=driver.find_element(By.XPATH,"//th[@data-svelte-h='svelte-18koz4z']")
    price.click()
    print("The Book_name in the 5th row after sorting is:",driver.find_element(By.XPATH,"//table/tbody/tr[5]/td[2]").text)