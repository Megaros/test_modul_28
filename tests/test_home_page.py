import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures('setup')
class TestHomePage:
    def test_homepage(self):
        driver = webdriver.Chrome()
        waite = WebDriverWait(driver, 10, 1)
        waite.until(ec.visibility_of_element_located(By.CSS_SELECTOR, '#stickyHeader > div.cn7 > div > div.ui-c1 > button > span'))
        element = driver.find_element(By.CSS_SELECTOR, '#stickyHeader > div.cn7 > div > div.ui-c1 > button > span')
        element.click()

