from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/selects")
    print(driver.title)
    dropdown=Select(driver.find_element(By.XPATH,"//select[@class='h-10 w-64 rounded-lg border-2 border-black bg-purple-200 px-3 shadow-md transition hover:shadow-lg']"))
    dropdown.select_by_visible_text("Two")
    print("Selected option:",dropdown.first_selected_option.text)
    time.sleep(2)
    dropdown.select_by_value("four")
    print("Selected option:",dropdown.first_selected_option.text)
    time.sleep(2)
    dropdown.select_by_index(3)
    print("Selected option:",dropdown.first_selected_option.text)
    time.sleep(2)
    options=dropdown.options
    for opt in options:
        print(opt.text)
        
    
    