from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
action = ActionChains(driver)
driver.get("https://demoqa.com/checkbox")
driver.find_element(By.XPATH,"//li[@class='rct-node rct-node-parent rct-node-collapsed']/span/label").click()