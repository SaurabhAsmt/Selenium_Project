from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Disabling the Automation Indicator WebDriver Flags
options = webdriver.ChromeOptions() #creating chromeoptions instance
options.add_argument("--disable-blink-features=AutomationControlled") #adding arg
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options = options) #creating webdriver instance
driver.get("https://www.google.com/") #request url

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_elem = driver.find_element(By.CLASS_NAME, "gLFyf")
input_elem.send_keys("jasmine rice" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "jasmine rice"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "jasmine rice")
link.click()

time.sleep(10)
driver.close()