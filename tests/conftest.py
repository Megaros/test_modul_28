import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrom_options


@pytest.fixture()
def get_chrome_options():
    options = chrom_options()
    options.add_argument('chrome')
    # options.add_argument('--headlees')
    return options


@pytest.fixture(scope='function')
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path= 'C:\selenium_course\pythonProject1\chromedriver', options=options)
    return driver


@pytest.fixture()
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.ozon.ru/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    print('\nЗакрываем браузер')
    driver.quit()
