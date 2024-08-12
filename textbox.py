import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

username = "Rajamegam"
valid_email = "rajamegam@gmail.com"
invalid_email = "rajamegam@gmail"
current_address = "98852 Nitzsche Lakes, Murraymouth, OK 31021"
permanent_address = "98852 Nitzsche Lakes, Murraymouth, OK 31021"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
action = ActionChains(driver)
driver.get("https://demoqa.com/text-box")

# webelements for the textboxes
username_WE = driver.find_element(By.ID, "userName")
valid_email_WE = driver.find_element(By.ID, "userEmail")
current_address_WE = driver.find_element(By.ID, "currentAddress")
permanent_address_WE = driver.find_element(By.ID, "permanentAddress")
submit_button = driver.find_element(By.ID, "submit")

# Fill the form by sending valid email ID
username_WE.send_keys(username)
valid_email_WE.send_keys(valid_email)
current_address_WE.send_keys(current_address)
permanent_address_WE.send_keys(permanent_address)

# scrolling to the element and perform the click action using ActionChains class
driver.execute_script("arguments[0].scrollIntoView();", submit_button)
action.move_to_element(submit_button).click().perform()

# scrolling to the bottom of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

# extract the results and assert with the test data
output_name = driver.find_element(By.ID, "name").text
output_email = driver.find_element(By.ID, "email").text
assert username == output_name.split(":")[1]
assert valid_email == output_email.split(":")[1]
