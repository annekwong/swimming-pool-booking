from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# from time import sleep


driver_path = 'K:\\[Newest Core]\\Tools\\chromedriver.exe'
def get_chrome():
    options = Options()
    options.add_argument("--log-level=3");
    
    driver = webdriver.Chrome(driver_path, options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => false})");
    return driver
def headless_chrome():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--log-level=3");
    
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => false})");
    return driver


def WaitPageLoad(driver):
    # print("Wait starting...")
    page_ready = ''
    while(page_ready != 'complete'):
        # print("Wait continuing...")
        driver.implicitly_wait(0.5)
        page_ready = driver.execute_script("return document.readyState")
    # print("Wait finished!")
    
def xpath(driver, x):
    return driver.find_element_by_xpath(x)
def xpaths(driver, x):
    return driver.find_elements_by_xpath(x)


def slow_type(element, text, delay=0.25):
    for character in text:
        element.send_keys(character)
        driver.implicitly_wait(delay)


url = "https://myrichmond.richmond.ca"
credentials = {
    "login": "take3this@yahoo.com",
    "password": "PoolTest7"
}

client_credentials = {
    "login": "Monylawk@yahoo.ca",
    "password": "Richmond1"
}

# --- --- ---     --- --- ---

driver = get_chrome()
driver.get(url)

timeout = 60


login = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//input[@type='text']")))
login.click()
driver.implicitly_wait(1)
slow_type(login, credentials['login'])

password = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//input[@type='password']")))
password.click()
driver.implicitly_wait(1)
slow_type(password, credentials['password'])

login_button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//input[@id='loginButton_0']")))
driver.implicitly_wait(1)
login_button.click()