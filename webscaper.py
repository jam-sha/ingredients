from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10) # this lets webdriver wait 10 seconds for the website to load
driver.get("https://www.ewg.org/skindeep/")

barcodes = ["Dimethiconol"]
for barcode in barcodes:
    text_box = driver.find_element_by_css_selector('eac-item') # input selector
    text_box.send_keys(barcode) # enter text in input

    driver.find_element_by_xpath('//*[@id="eac-container-search"]/ul/li/div').click() # click the submit button

driver.quit()   