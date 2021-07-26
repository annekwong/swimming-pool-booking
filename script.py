from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException

from time import time, sleep
from datetime import datetime
import json
import os

from sys import argv

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
    options.add_argument('window-size=1920x1080');
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

def login(driver):
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
    
    
def Minoru(driver):
    login(driver)
    
    flag = True
    # sleep_wait = 10
    while(flag):
        try:
            # sleep(sleep_wait)
            activities_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "*//div/ul/a[contains(@href, 'richmondcity.perfectmind.com')]")))
        except ElementClickInterceptedException:
            # print("Click intercepted")
            pass
        except:
            print("Probably maintenance... F5-ing")
            # sleep_wait += 2
            driver.refresh() # this block should be sufficient against maintenance... COULDA TESTED IT THEN
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


# def go(i):
    # global driver
    # global days
    # global register_buttons
    # days = register_buttons[-7:]
    # driver.get(days[i])
    
# def s():
    # global driver
    # body_elements = xpaths(driver, "*//body")
    # for b in body_elements:
        # count = len(glob("*.html"))
        # name = "{:02d}.html".format(count)
        # open("{:02d}.html".format(count), "w", encoding='utf8').write(b.get_attribute('outerHTML'))
        # print("> wrote {:s}".format(name))
    
# are these necessary?...
def clickalert(driver):
    # what speed do these appear with?
    try:
        # xpath(driver, "*//div[@class='message'][@role='alert']").click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "*//div[@class='message'][@role='alert']"))).click()
    except: 
        pass
    else:
        pass
        # print("Alert found and clicked away")
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

def next0(driver):
    # print("Going next0")
    xpath(driver, "*//span[text()='Next']").click()

def next1(driver):
    # print("Going next1")
    xpath(driver, "*//a[@title='Next']").click()

def Timestamp():
    return datetime.now().strftime("%d-%m-%y_%H-%M-%S")


# - test up to questionnaire
# --- go the the page, THEN launch this. That way can test irrespective of where we are
def process_v0(driver):
    clickalert(driver)
    
    reg_flag = True
    while(reg_flag):
        try:
            register_button = WebDriverWait(driver, 1.0).until(EC.element_to_be_clickable((By.XPATH, "*//a[contains(@class,'book-button')]")))
        except TimeoutException:
            driver.refresh()
        else:
            reg_flag = False
    # register_button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//a[contains(@class,'book-button')]")))
    clickalert(driver)
    
    register_button.click()
    
    sleep(0.5)
    
    # --- ATTENDEES
    checkbox = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, ".//table//label[contains(text(), '(You)')]/ancestor::tr//input[@type='checkbox']")))
    clickalert()
    if not checkbox.is_selected():
        checkbox.click()
    next0(driver)
    
    sleep(0.5)
    
    
    # --- QUESTIONNAIRE
    start = time()
    WaitPageLoad(driver)
    end = time()
    # print("> load wait: {:3.2f}".format(end-start))
    
    consent_check = xpath(driver, "*//*[@class='reg-form']//div[@class='questionField']//input")
    consent_press = xpath(driver, "*//*[@class='reg-form']//div[@class='questionField']//label")
    if not consent_check.is_selected:
        consent_press.click()
    sleep(0.25)
    next1(driver)
    
    
    # --- FEES AND EXTRAS
    pick_fee = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//div[@class='fee-section']//span[contains(text(), 'Aquatic & Fitness Membership')]/preceding-sibling::span[@class='outer-circle']")))
    # clickalert()
    pick_fee.click()
    next0(driver)
    
    
    # --- PAYMENT
    # - oh, this has an iframe. How quaint!
    WaitPageLoad(driver)
    WebDriverWait(driver, medium_timeout).until(EC.visibility_of_element_located((By.XPATH, "*//iframe[@name='iframe']")))
    driver.switch_to.frame(xpath(driver, "*//iframe[@name='iframe']")) # can wait until it loads
    order_button = WebDriverWait(driver, medium_timeout).until(EC.element_to_be_clickable((By.XPATH, "*//button[@class='process-now'][contains(text(), 'Place My Order')]")))
    # print("Got to the order button")
    try:
        order_button = WebDriverWait(driver, medium_timeout).until(EC.element_to_be_clickable((By.XPATH, "*//button[@class='process-now'][contains(text(), 'Place My Order')]")))
    except:
        pass
        # print("Can't find order button")
    else:
        order_button.click()
    
    
    
    # --- session confirmation
    WaitPageLoad(driver)
    
    # session   = xpath(driver, "*//div[@id='main-content']//div[@class='bm-event-info']//h2/span").text
    # book_date = xpath(driver, "*//div[@id='main-content']//div[@class='bm-event-info']//span/span[@class='bm-date']").text.split(", ")[-1]
    # book_time = xpath(driver, "*//div[@id='main-content']//div[@class='bm-event-info']//span/span[@class='bm-subject']").text
    session_el  = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "*//div[@id='main-content']//div[@class='bm-event-info']//h2/span")))
    bookdate_el = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "*//div[@id='main-content']//div[@class='bm-event-info']//span/span[@class='bm-date']")))
    booktime_el = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "*//div[@id='main-content']//div[@class='bm-event-info']//span/span[@class='bm-subject']")))
    
    session = session_el.text
    book_date = bookdate_el.text.split(", ")[-1]
    book_time = booktime_el.text
    
    d = {
        "session" : session,
        "date" : book_date,
        "time" : book_time
    }
    
    # - not the best place for a folder declaration, boa
    save_folder = ".\\temp\\"
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    
    # timestamp = datetime.now().strftime("%H-%M-%S")
    timestamp = datetime.now().strftime("%d-%m-%y %H-%M-%S")
    json.dump(d, open(save_folder+"session_results-{:s}.json".format(timestamp), "w"), indent=4)
    xpath(driver, "*//body").screenshot(save_folder+"screenshot-{:s}.png".format(timestamp))
def process(driver):
    try:
        WebDriverWait(driver, 10.0).until(EC.element_to_be_clickable((By.XPATH, "*//div[@class='message'][@role='alert']")))
        clickalert(driver)
    except TimeoutException:
        pass
    
    reg_flag = True
    while(reg_flag):
        try:
            register_button = WebDriverWait(driver, 1.0).until(EC.element_to_be_clickable((By.XPATH, "*//a[contains(@class,'book-button')]")))
        except TimeoutException:
            print("Waiting for the button...")
            driver.refresh()
        else:
            reg_flag = False
    
    register_button.click()
    
    sleep(0.5)
    
    # --- ATTENDEES
    # if the checkbox is blocked, it's probably because we can't 
    try:
        checkbox = WebDriverWait(driver, 2.5).until(EC.element_to_be_clickable((By.XPATH, ".//table//label[contains(text(), '(You)')]/ancestor::tr//input[@type='checkbox']")))
    except TimeoutException:
        try:
            xpath(driver, "*//tr[contains(@title, 'Already Registered')]")
            print("Already registered, moving on")
            return
        except NoSuchElementException:
            pass
    
    clickalert(driver)
    if not checkbox.is_selected():
        checkbox.click()
    next0(driver)
    
    sleep(0.5)
    
    
    # --- QUESTIONNAIRE
    start = time()
    WaitPageLoad(driver)
    end = time()
    # print("> load wait: {:3.2f}".format(end-start))
    
    consent_check = xpath(driver, "*//*[@class='reg-form']//div[@class='questionField']//input")
    consent_press = xpath(driver, "*//*[@class='reg-form']//div[@class='questionField']//label")
    if not consent_check.is_selected:
        consent_press.click()
    sleep(0.25)
    next1(driver)
    
    
    # --- FEES AND EXTRAS
    pick_fee = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "*//div[@class='fee-section']//span[contains(text(), 'Aquatic & Fitness Membership')]/preceding-sibling::span[@class='outer-circle']")))
    # clickalert()
    pick_fee.click()
    next0(driver)
    
    
    # --- PAYMENT
    # - oh, this has an iframe. How quaint!
    WaitPageLoad(driver)
    WebDriverWait(driver, medium_timeout).until(EC.visibility_of_element_located((By.XPATH, "*//iframe[@name='iframe']")))
    driver.switch_to.frame(xpath(driver, "*//iframe[@name='iframe']")) # can wait until it loads
    order_button = WebDriverWait(driver, medium_timeout).until(EC.element_to_be_clickable((By.XPATH, "*//button[@class='process-now'][contains(text(), 'Place My Order')]")))
    # print("Got to the order button")
    try:
        order_button = WebDriverWait(driver, medium_timeout).until(EC.element_to_be_clickable((By.XPATH, "*//button[@class='process-now'][contains(text(), 'Place My Order')]")))
    except:
        pass
        # print("Can't find order button")
    else:
        order_button.click()
    
    
    
    # --- session confirmation
    WaitPageLoad(driver)
    
    # session   = xpath(driver, "*//div[@id='main-content']//div[@class='bm-event-info']//h2/span").text
    # book_date = xpath(driver, "*//div[@id='main-content']//div[@class='bm-event-info']//span/span[@class='bm-date']").text.split(", ")[-1]
    # book_time = xpath(driver, "*//div[@id='main-content']//div[@class='bm-event-info']//span/span[@class='bm-subject']").text
    
    flag = True
    while(flag):
        try:
            session_el = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "*//div[@id='main-content']//div[@class='bm-event-info']//h2/span")))
            flag = False
        except NoSuchWindowException:
            print("Window exception.")
            sleep(1)
    
    bookdate_el = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "*//div[@id='main-content']//div[@class='bm-event-info']//span/span[@class='bm-date']")))
    booktime_el = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "*//div[@id='main-content']//div[@class='bm-event-info']//span/span[@class='bm-subject']")))
    
    session = session_el.text
    book_date = bookdate_el.text.split(", ")[-1]
    book_time = booktime_el.text
    
    d = {
        "session" : session,
        "date" : book_date,
        "time" : book_time
    }
    
    # - not the best place for a folder declaration, boa
    save_folder = ".\\temp\\"
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    
    # timestamp = datetime.now().strftime("%H-%M-%S")
    # timestamp = datetime.now().strftime("%d-%m-%y %H-%M-%S")
    timestamp = Timestamp()
    
    json.dump(d, open(save_folder+"session_results-{:s}.json".format(timestamp), "w"), indent=4)
    xpath(driver, "*//body").screenshot(save_folder+"screenshot-{:s}.png".format(timestamp))
    print("Booked {:s}, {:s}, {:s}".format(session, book_date, book_time))
    

# register_buttons = xpaths(driver, "*//span[contains(text(), 'REGISTERED VISIT - LANE SWIMMING')]/ancestor::div[@class='bm-class-container'] / *//span[contains(text(),'9:00am - ')]/ancestor::div[@class='bm-class-container']//input[@type='button']")
def RegisterButtons_v0(type_str, time_str):
    register_buttons = xpaths(driver, "*//span[contains(text(), '{:s}')]/ancestor::div[@class='bm-class-container'] / *//span[contains(text(),'{:s} ')]/ancestor::div[@class='bm-class-container']//input[@type='button']".format(type_str, time_str))
    return [click_prefix+regex.compile(r"\(\'(.*)\'\)").search(x.get_attribute('onclick'))[1] for x in register_buttons if x.get_attribute('value')=='REGISTER']
# renamed
def SlotNodes(driver):
    # date = "./preceding-sibling::tr[@class='bm-marker-row'][1]").text
    
    classes_table = xpath(driver, "*//table[@id='classes']")
    # class_type = xpath(_, ".//span[@class='bm-event-description']").get_attribute('innerHTML')
    
    # date = xpath(entries[0], "./preceding-sibling::tr[@class='bm-marker-row'][1]").text
    # entries = xpaths(classes_table, ".//div[@class='bm-class-header-wrapper']//span[contains(text(), '{:s}')]/ancestor::tr / .//div[@class='bm-group-item-desc']//span[contains(text(), '{:s}')]/ancestor::tr".format('LANE SWIMMING', '9:00am -'))
    # control = {
        # "type" : "REGISTERED VISIT - LANE SWIMMING",
        # "time" : "9:00 am"
    # }
    
    # control = json.load(open("control_test.json","r"))
    control = json.load(open("control_release.json","r"))
    print("Book type: {:s}".format(control['type']))
    print("Book time: {:s}".format(control['time']))
    
    nodes = xpaths(classes_table, ".//div[@class='bm-class-header-wrapper']//span[contains(text(), '{:s}')]/ancestor::tr / .//div[@class='bm-group-item-desc']//span[contains(text(), '{:s} -')]/ancestor::tr".format(control['type'], control['time']))
    # return [click_prefix+regex.compile(r"\(\'(.*)\'\)").search(xpath(x, ".//input").get_attribute('onclick'))[1] for x in entries]
    
    links = [click_prefix+regex.compile(r"\(\'(.*)\'\)").search(xpath(x, ".//input").get_attribute('onclick'))[1] for x in nodes]
    
    infos = []
    # for each entry, let's grab type, 
    for i in range(len(nodes)):
        d = {}
        d['element'] = nodes[i]
        d['link']    = links[i]
        
        swim_type = xpath(nodes[i], ".//div[@class='bm-class-header-wrapper']//span[@class='bm-event-description']").get_attribute('innerHTML')
        d['type'] = swim_type
        
        date = xpath(nodes[i], "./preceding-sibling::tr[@class='bm-marker-row'][1]").text
        d['date'] = date
        
        slot_time = xpath(nodes[i], ".//div[@class='bm-group-item-desc']//span[contains(@aria-label, 'Event time')]").text
        d['time'] = slot_time
        
        try:
            spots = xpath(nodes[i], ".//div[@class='bm-spots-left-label']/span[@aria-label]").text
        except NoSuchElementException:
            spots = 'None'
        
        d['spots'] = spots
        
        # - fuck printing's slow...
        print("{:s}, {:s}, {:s}, {:s}".format(swim_type, date, slot_time, spots))
        
        infos.append(d)
    
    return infos


if __name__ == "__main__":
    
    
    ### ----- FLOW -----
    driver = get_chrome()
    driver.get(url)
    
    start = time()
    Minoru(driver)
    end = time()
    print("> Login+Minoru: {:3.2f} seconds".format(end-start))
    
    # - wait for the table to appear
    start = time()
    WebDriverWait(driver, big_timeout).until(EC.visibility_of_element_located((By.XPATH, "*//table[@id='classes']")))
    end = time()
    print("> Classes: {:3.2f} seconds".format(end-start))
    
    
    slot_nodes = SlotNodes(driver, settings)
    
    print("{}:{}:{}".format(settings['start'], settings['stop'], settings['step']))
    for s in slot_nodes[settings['start']:settings['stop']:settings['step']]:
        print("{:s}, {:s}, {:s}, {:s}".format(s['type'], s['date'], s['time'], s['spots']))
    
    for sn in slot_nodes[settings['start']:settings['stop']:settings['step']]:
        # process full
        if(sn['spots'] != 'Full'):
            driver.get(sn['link'])
            
            # process full
            try:
                full_el = xpath(driver, "*//label[@class='spots']/span").text
            except NoSuchElementException:
                full_el = None
            
            if(full_el != 'Full'):
                process(driver)
                sleep(1)
            
            
    # - do some sort of check, THEN decide to close; possibly go through them again
    driver.close()
    driver.quit()
    
    # scoop up "temp" folder, archive contents, send in an email
    
    
    exit(0)
    
    