from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import ElementClickInterceptedException

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

def CheckServerTime(url):
    requests.get(url).headers['Date']

url = "https://myrichmond.richmond.ca"
credentials = {
    "my_login": "take3this@yahoo.com",
    "my_password": "PoolTest7",
    "login": "Monylawk@yahoo.ca",
    "password": "Richmond1"
}
click_prefix = "https://richmondcity.perfectmind.com"

# --- --- ---     --- --- ---

driver = get_chrome()
driver.get(url)

big_timeout = 60
timeout = 5

def login(test=True):
    if(test):
        cred_login = credentials['my_login']
        cred_pass  = credentials['my_password']
    else:
        cred_login = credentials['login']
        cred_pass  = credentials['password']

    login = WebDriverWait(driver, big_timeout).until(EC.visibility_of_element_located((By.XPATH, "*//input[@type='text']")))
    # login = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//input[@type='text']")))
    login.click()
    driver.implicitly_wait(1)
    slow_type(login, cred_login)

    password = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//input[@type='password']")))
    password.click()
    driver.implicitly_wait(1)
    slow_type(password, cred_pass)

    login_button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//input[@id='loginButton_0']")))
    driver.implicitly_wait(1)
    login_button.click()

    # WAIT FOR MY RICHMOND TO LOAD
    # drawer_button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//button[@aria-label='open drawer']")))
    # drawer_button.click()

    flag = True
    while(flag):
        try:
            activities_button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//div/ul/a[contains(@href, 'richmondcity.perfectmind.com')]")))
            driver.implicitly_wait(1)
            activities_button.click()
        except ElementClickInterceptedException:
            print("Click intercepted")
        finally:
            flag = False
    activities_button.click()
    
    # switch to another tab
    driver.switch_to.window(driver.window_handles[1])
    WaitPageLoad(driver)
    print("Perfect mind!")

    # - in Chrome xpath query, this gave me what I wanted
    # *//span[contains(text(), 'REGISTERED VISIT - LANE SWIMMING')]/ancestor::div[@class='bm-class-container'] / *//span[contains(text(), '9:00am -')]/ancestor::div[@class='bm-class-container']


    # - click to "Minoru Centre for Active Living"
    # xpath(driver, "*//h2[contains(text(), 'Registered Visits')]/following-sibling::ul/li/a[contains(text(), 'Minoru Centre for Active Living')]").click()
    minoru_centre = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//h2[contains(text(), 'Registered Visits')]/following-sibling::ul/li/a[contains(text(), 'Minoru Centre for Active Living')]")))
    minoru_centre.click()

# - wait for table[@id='classes'] to load
# - got it.
# register_buttons = xpaths(driver, "*//span[contains(text(), 'REGISTERED VISIT - LANE SWIMMING')]/ancestor::div[@class='bm-class-container'] / *//span[contains(text(),'9:00am - ')]/ancestor::div[@class='bm-class-container']")
# xpath(register_buttons[0], ".//input[@type='button']").click()


def go(i):
    global driver
    global days
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
        xpath(driver, "*//div[@class='message'][@role='alert']").click()
        print("Alert found and clicked away")
    except: 
        pass

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






### ----- FLOW -----
login(False)

# - wait for the table to appear
WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "*//table[@id='classes']")))
# --- DETERMINES THE VENUES TO BOOK
# - for testing at least, can make this return things based on search string from predetermined set
register_buttons = xpaths(driver, "*//span[contains(text(), 'REGISTERED VISIT - LANE SWIMMING')]/ancestor::div[@class='bm-class-container'] / *//span[contains(text(),'9:00am - ')]/ancestor::div[@class='bm-class-container']//input[@type='button']")
days = [click_prefix+regex.compile(r"\(\'(.*)\'\)").search(x.get_attribute('onclick'))[1] for x in register_buttons[7:]]

# testrun()
# fullrun()


def next0():
    print("Going next0")
    xpath(driver, "*//span[text()='Next']").click()

def next1():
    print("Going next1")
    xpath(driver, "*//a[@title='Next']").click()


# - test up to questionnaire
# --- go the the page, THEN launch this. That way can test irrespective of where we are
def process():
    
    # WaitPageLoad(driver)  # - are these necessary when I use WebDriverWait everywhere?
    register_button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//a[contains(@class,'book-button')]")))
    clickalert()  # ?
    register_button.click()
    
    
    # --- ATTENDEES
    # attendees = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "*//div[@id='event-attendees']")))
    clickalert()
    # label = xpath(attendees, ".//table//label[contains(text(), '(You)')]")
    # checkbox = xpath(label, "./ancestor::tr//input[@type='checkbox']")
    checkbox = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, ".//table//label[contains(text(), '(You)')]/ancestor::tr//input[@type='checkbox']")))
    if not checkbox.is_selected():
        checkbox.click()
    clickalert()
    next0()
    
    
    # --- QUESTIONNAIRE
    WaitPageLoad(driver)
    next1()
    
    
    # --- FEES AND EXTRAS
    # div[@class='fee-section']//span[contains(text(), 'Aquatic & Fitness Membership)]
    # WaitPageLoad(driver)
    pick_fee = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//div[@class='fee-section']//span[contains(text(), 'Free')]")))
    # pick_fee = xpath(driver, "*//div[@class='fee-section']//span[contains(text(), 'Free')]/ancestor::tr//input[@type='radio']")
    
    # pick_flag = True
    # while(pick_flag):
        # try:
            # pick_fee = xpath(driver, "*//div[@class='fee-section']//span[contains(text(), 'Free')]/ancestor::tr//input[@type='radio']")
        # except:
            # sleep(0.5)
        # finally:
            # pick_fee.click()
            
    next0()
    
    return
    
    # --- PAYMENT
    order_button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//button[contains(text(), 'Place My Order')]")))
    # order_button = xpath(driver, "*//button[contains(text(), 'Place My Order')]")
    order_button.click()

# day(0)

def hide():

    # for day in days:
    for i in range(len(days)):
        go(i)
        
        # WaitPageLoad(driver)  # - are these necessary when I use WebDriverWait everywhere?
        register_button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//a[contains(@class,'book-button')]")))
        clickalert()  # ?
        register_button.click()

        # --- ATTENDEES
        # attendees = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "*//div[@id='event-attendees']")))
        clickalert()
        # label = xpath(attendees, ".//table//label[contains(text(), '(You)')]")
        # checkbox = xpath(label, "./ancestor::tr//input[@type='checkbox']")
        checkbox = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, ".//table//label[contains(text(), '(You)')]/ancestor::tr//input[@type='checkbox']")))
        if not checkbox.is_selected():
            checkbox.click()
        next0()
        
        # --- QUESTIONNAIRE
        # - click the covid checkbox if unchecked
        
        
        clickalert()
        # - next1
        # xpath(driver, "*//a[@title='Next']").click()

        # --- FEES & EXTRAS
        # - select FREE or '$0.00'



        # - next0
        # xpath(driver, "*//span[text()='Next']").click()



        # --- PAYMENT






