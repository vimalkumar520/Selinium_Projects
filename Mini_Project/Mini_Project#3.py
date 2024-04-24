from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import allure
import time
import pytest

@pytest.mark.smoke
@allure.title("Verify that Registration page is opened ")
@allure.description("TC#1 - Enter email,password,confirm password and click submit button.")
def test_mini_project():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    driver.maximize_window()
    time.sleep(3)
    driver.switch_to.frame(driver.find_element(By.ID, "result"))
    usr_element = driver.find_element(By.XPATH, "//input[@id='email']")
    usr_element.send_keys("john.wick@abc.com")
    pass_element = driver.find_element(By.XPATH, "//input[@id='password']")
    pass_element.send_keys("ThisIsNotAPassword")
    cn_pass_element = driver.find_element(By.XPATH, "//input[@id='password2']")
    cn_pass_element.send_keys("ThisIsNotAPassword")
    sub_mit = driver.find_element(By.XPATH, "//button[text()='Submit']")
    sub_mit.click()
    time.sleep(5)
    verify_text = driver.find_element(By.XPATH, "//input[@id='username']/following::small")
    print(verify_text)
    assert verify_text.text == "Username must be at least 3 characters"
    allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)