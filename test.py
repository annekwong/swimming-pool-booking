from script import *


# driver = get_chrome()
driver = headless_chrome()
driver.get(url)
WaitPageLoad(driver)

start = time()
Minoru(driver)
end = time()
print("> Login+Minoru: {:3.2f} seconds".format(end-start))

# - wait for the table to appear
start = time()
WebDriverWait(driver, big_timeout).until(EC.visibility_of_element_located((By.XPATH, "*//table[@id='classes']")))
end = time()
print("> Classes: {:3.2f} seconds".format(end-start))

# settings = ParseConfig("test.json") # test
settings = ParseConfig("settings.json") # release

slot_nodes = SlotNodes(driver, settings)

print("{}:{}:{}".format(settings['start'], settings['stop'], settings['step']))
for s in slot_nodes[settings['start']:settings['stop']:settings['step']]:
    # print("{:s}, {:s}, {:s}, {:s}".format(swim_type, date, slot_time, spots))
    print("{:s}, {:s}, {:s}, {:s}".format(s['type'], s['date'], s['time'], s['spots']))

# days = [x['link'] for x in slot_nodes[1:8]] # test
days = [x['link'] for x in slot_nodes[-7:]] # release

for i in range(len(days)):
    driver.get(days[i])
    process(driver)
    sleep(1)
print("> All booked")



# --- bow out.
driver.quit()
print("> All done.")
exit(0)