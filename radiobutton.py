import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
action = ActionChains(driver)
driver.get("https://demoqa.com/radio-button")


def verify_radio_button(radio_button_ID, expected_selection):
    radio_button = driver.find_element(By.ID, radio_button_ID)

    action.move_to_element(radio_button).click().perform()

    success_message = driver.find_element(By.CSS_SELECTOR, ".mt-3").text
    time.sleep(2)
    expected_message = f"You have selected {expected_selection}"

    assert success_message == expected_message, f"expected_message:{expected_message} but got:{success_message} "

    print(f"{success_message}:{expected_message}")


verify_radio_button("yesRadio", "Yes")
verify_radio_button("impressiveRadio", "Impressive")
