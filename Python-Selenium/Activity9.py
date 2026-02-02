from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys
with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/keyboard-events")
    print(driver.title)
    time.sleep(3)
    search=driver.find_element(By.XPATH,"//h1[@class='mt-3 text-center text-4xl font-semibold text-black']")
    actions=webdriver.ActionChains(driver)
    actions.click(search).key_down(Keys.SHIFT).send_keys('s').key_up(Keys.SHIFT).send_keys('elenium').send_keys(Keys.RETURN).perform()
    