import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = os.environ.get("BASE_URL", "http://localhost:8091")


@pytest.fixture
def driver():
    options = Options()
    options.binary_location = "/usr/bin/chromium"
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,800")
    options.add_argument("--user-data-dir=/tmp/chrome-profile")
    drv = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=options)
    yield drv
    drv.quit()


def test_page_title(driver):
    driver.get(BASE_URL)
    assert driver.title == "CI/CD Assignment - Sadat Ali"


def test_heading(driver):
    driver.get(BASE_URL)
    heading = driver.find_element(By.ID, "title")
    assert heading.text == "Automated CI/CD Pipeline for a Web Application"


def test_name_and_roll_number(driver):
    driver.get(BASE_URL)
    assert driver.find_element(By.ID, "name").text == "Name: Sadat Ali"
    assert driver.find_element(By.ID, "roll").text == "Roll Number: FA23-BCT-034"


def test_button_click_shows_message(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "show-msg").click()
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.ID, "msg"), "Welcome")
    )
    assert driver.find_element(By.ID, "msg").text == "Welcome! This page was deployed by Jenkins."


def test_text_box_input(driver):
    driver.get(BASE_URL)
    box = driver.find_element(By.ID, "user-text")
    box.send_keys("Hello Jenkins")
    driver.find_element(By.ID, "submit-btn").click()
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.ID, "output"), "Hello Jenkins")
    )
    assert driver.find_element(By.ID, "output").text == "You entered: Hello Jenkins"
    driver.save_screenshot("screenshot.png")
