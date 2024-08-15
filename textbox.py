import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

username = "Rajamegam"

invalid_email = "rajamegam@gmail"
current_address = "98852 Nitzsche Lakes, Murraymouth, OK 31021"
permanent_address = "98852 Nitzsche Lakes, Murraymouth, OK 31021"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
action = ActionChains(driver)
driver.get("https://demoqa.com/text-box")


def explicit_wait(by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located((by, value)))


# webelements for the textboxes
username_input = explicit_wait(By.ID, "userName")
valid_email_input = explicit_wait(By.ID, "userEmail")
current_address_input = explicit_wait(By.ID, "currentAddress")
permanent_address_input = explicit_wait(By.ID, "permanentAddress")
submit_button = explicit_wait(By.ID, "submit")


# Fill the form
def fill_form(email):
    username_input.send_keys(username)
    valid_email_input.send_keys(email)
    current_address_input.send_keys(current_address)
    permanent_address_input.send_keys(permanent_address)
    return email


email_ID = fill_form("rajamegam7@gmail.com")  # valid emailID


# scrolling to the element and perform the click action using ActionChains class
driver.execute_script("arguments[0].scrollIntoView();", submit_button)
action.move_to_element(submit_button).click().perform()

time.sleep(2)

# scrolling to the bottom of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

# extract the results and assert with the test data
output_name = driver.find_element(By.ID, "name").text
output_email = driver.find_element(By.ID, "email").text
assert username == output_name.split(":")[1]
print(username)
assert email_ID == output_email.split(":")[1]
print(email_ID)
