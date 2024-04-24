from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest

@pytest.mark.smoke
@allure.title("Verify that Web Page is opened")
@allure.description("Check Your free trial has expired")
def test_mini_project():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()
    user_name = driver.find_element(By.ID, "username")
    user_name.send_keys("augtest_040823@idrive.com")
    pass_word = driver.find_element(By.ID, "password")
    pass_word.send_keys("123456")
    sign_in = driver.find_element(By.ID, "frm-btn")
    sign_in.click()
    time.sleep(25)
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    verify_text = driver.find_element(By.XPATH, "//div/h5")
    print(verify_text)
    assert verify_text.text == "Your free trial has expired"
    allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)