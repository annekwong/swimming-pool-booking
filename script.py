from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException

from time import time, sleep

# from time import sleep
import regex
from glob import glob

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
        sleep(0.5)
        page_ready = driver.execute_script("return document.readyState")
    # print("Wait finished!")
    
def xpath(driver, x):
    return driver.find_element_by_xpath(x)
def xpaths(driver, x):
    return driver.find_elements_by_xpath(x)


def slow_type(element, text, delay=0.05):
    for character in text:
        element.send_keys(character)
        sleep(delay)

def CheckServerTime(url):
    requests.get(url).headers['Date']

url = "https://myrichmond.richmond.ca"
credentials = {
    # "my_login": "take3this@yahoo.com",
    # "my_password": "PoolTest7",
    "login": "Monylawk@yahoo.ca",
    "password": "Richmond1"
}
click_prefix = "https://richmondcity.perfectmind.com"

# --- --- ---     --- --- ---



big_timeout = 60
medium_timeout = 10
timeout = 5

def login():
    # if(test):
        # cred_login = credentials['my_login']
        # cred_pass  = credentials['my_password']
    # else:
    cred_login = credentials['login']
    cred_pass  = credentials['password']
    
    login = WebDriverWait(driver, big_timeout).until(EC.visibility_of_element_located((By.XPATH, "*//input[@type='text']")))
    sleep(0.5)
    login.click()
    sleep(0.25)
    slow_type(login, cred_login)
    
    sleep(0.5)
    
    password = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//input[@type='password']")))
    password.click()
    sleep(0.25)
    slow_type(password, cred_pass)
    
    login_button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//input[@id='loginButton_0']")))
    sleep(0.5)
    login_button.click()
    
def Minoru():
    # WAIT FOR MY RICHMOND TO LOAD
    # drawer_button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//button[@aria-label='open drawer']")))
    # drawer_button.click()
    
    login()
    
    flag = True
    sleep_wait = 5
    while(flag):
        try:
            sleep(sleep_wait)
            activities_button = WebDriverWait(driver, medium_timeout).until(EC.element_to_be_clickable((By.XPATH, "*//div/ul/a[contains(@href, 'richmondcity.perfectmind.com')]")))
        except ElementClickInterceptedException:
            # print("Click intercepted")
            pass
        except:
            sleep_wait += 5
            driver.refresh()
        else:
            flag = False
            sleep(1)
            activities_button.click()
    
    # switch to another tab
    driver.switch_to.window(driver.window_handles[1])
    WaitPageLoad(driver)
    # print("Perfect mind!")
    
    minoru_centre = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//h2[contains(text(), 'Registered Visits')]/following-sibling::ul/li/a[contains(text(), 'Minoru Centre for Active Living')]")))
    minoru_centre.click()




# - wait for table[@id='classes'] to load
# - got it.
# register_buttons = xpaths(driver, "*//span[contains(text(), 'REGISTERED VISIT - LANE SWIMMING')]/ancestor::div[@class='bm-class-container'] / *//span[contains(text(),'9:00am - ')]/ancestor::div[@class='bm-class-container']")
# xpath(register_buttons[0], ".//input[@type='button']").click()


def go(i):
    global driver
    global days
    global register_buttons
    days = register_buttons[7:]
    driver.get(days[i])
    
def s():
    global driver
    body_elements = xpaths(driver, "*//body")
    for b in body_elements:
        count = len(glob("*.html"))
        name = "{:02d}.html".format(count)
        open("{:02d}.html".format(count), "w", encoding='utf8').write(b.get_attribute('outerHTML'))
        print("> wrote {:s}".format(name))
    
def clickalert():
    # what speed do these appear with?
    try:
        # xpath(driver, "*//div[@class='message'][@role='alert']").click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "*//div[@class='message'][@role='alert']"))).click()
    except: 
        pass
    else:
        print("Alert found and clicked away")
    sleep(0.5)

"""
def register():
    register_flag = True
    while(register_flag):
        try:
            button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//a[contains(@class,'book-button')]")))
            # xpath(driver, "*//a[contains(@class,'book-button')]").click()
            button.click()
        except KeyboardInterrupt:
            register_flag = False
            break
        except:
            sleep(1)
        finally:
            register_flag = False
"""

def next0():
    print("Going next0")
    xpath(driver, "*//span[text()='Next']").click()

def next1():
    print("Going next1")
    xpath(driver, "*//a[@title='Next']").click()


# - test up to questionnaire
# --- go the the page, THEN launch this. That way can test irrespective of where we are
def process():
    clickalert()
    
    reg_flag = True
    while(reg_flag):
        try:
            register_button = WebDriverWait(driver, 0.5).until(EC.element_to_be_clickable((By.XPATH, "*//a[contains(@class,'book-button')]")))
        except TimeoutException:
            driver.refresh()
        else:
            reg_flag = False
    # register_button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//a[contains(@class,'book-button')]")))
    clickalert()
    
    register_button.click()
    
    sleep(0.5)
    
    # --- ATTENDEES
    checkbox = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, ".//table//label[contains(text(), '(You)')]/ancestor::tr//input[@type='checkbox']")))
    clickalert()
    if not checkbox.is_selected():
        checkbox.click()
    next0()
    
    sleep(0.5)
    
    
    # --- QUESTIONNAIRE
    start = time()
    WaitPageLoad(driver)
    end = time()
    print("> load wait: {:3.2f}".format(end-start))
    
    consent_check = xpath(driver, "*//*[@class='reg-form']//div[@class='questionField']//input")
    consent_press = xpath(driver, "*//*[@class='reg-form']//div[@class='questionField']//label")
    if not consent_check.is_selected:
        consent_press.click()
    sleep(0.25)
    next1()
    
    
    # --- FEES AND EXTRAS
    pick_fee = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//div[@class='fee-section']//span[contains(text(), 'Aquatic & Fitness Membership')]/preceding-sibling::span[@class='outer-circle']")))
    clickalert()
    pick_fee.click()
    next0()
    
    
    # --- PAYMENT
    # - oh, this has an iframe. How quaint!
    WaitPageLoad(driver)
    WebDriverWait(driver, medium_timeout).until(EC.visibility_of_element_located((By.XPATH, "*//iframe[@name='iframe']")))
    driver.switch_to.frame(xpath(driver, "*//iframe[@name='iframe']")) # can wait until it loads
    order_button = WebDriverWait(driver, medium_timeout).until(EC.element_to_be_clickable((By.XPATH, "*//button[@class='process-now'][contains(text(), 'Place My Order')]")))
    print("Got to the order button")
    try:
        order_button = WebDriverWait(driver, medium_timeout).until(EC.element_to_be_clickable((By.XPATH, "*//button[@class='process-now'][contains(text(), 'Place My Order')]")))
    except:
        print("Can't find order button")
    else:
        order_button.click()
    

# register_buttons = xpaths(driver, "*//span[contains(text(), 'REGISTERED VISIT - LANE SWIMMING')]/ancestor::div[@class='bm-class-container'] / *//span[contains(text(),'9:00am - ')]/ancestor::div[@class='bm-class-container']//input[@type='button']")
def RegisterButtons(type_str, time_str):
    register_buttons = xpaths(driver, "*//span[contains(text(), '{:s}')]/ancestor::div[@class='bm-class-container'] / *//span[contains(text(),'{:s} ')]/ancestor::div[@class='bm-class-container']//input[@type='button']".format(type_str, time_str))
    return [click_prefix+regex.compile(r"\(\'(.*)\'\)").search(x.get_attribute('onclick'))[1] for x in register_buttons]





### ----- FLOW -----
driver = get_chrome()
driver.get(url)

start = time()
Minoru()
end = time()
print("> Login+Minoru: {:3.2f} seconds".format(end-start))

# - wait for the table to appear
start = time()
WebDriverWait(driver, big_timeout).until(EC.visibility_of_element_located((By.XPATH, "*//table[@id='classes']")))
end = time()
print("> Classes: {:3.2f} seconds".format(end-start))
# --- DETERMINES THE VENUES TO BOOK
# - for testing at least, can make this return things based on search string from predetermined set

# - the main order one
# register_buttons = RegisterButtons('REGISTERED VISIT - LANE SWIMMING', '9:00am -')
# days = register_buttons[7:]
register_buttons = RegisterButtons('REGISTERED VISIT - FITNESS CENTRE', '6:45pm -')

driver.get(register_buttons[0])
process()




# testrun()
# fullrun()


