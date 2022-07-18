import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait     
from selenium.webdriver.common.by import By     
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10) # this lets webdriver wait 10 seconds for the website to load
#driver.get("https://www.ewg.org/skindeep/")


barcodes = ["Dimethiconol"]
for barcode in barcodes:
 #   text_box = driver.find_element(By.CLASS_NAME, "homepage-search-input")
  #  text_box.send_keys(barcode)


  #  elems = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "eac-item [href]")))

  #  itemData = elems[0].get_attribute('href') # link of item were serching
    itemLink = "https://www.ewg.org/skindeep/ingredients/702044-dimethiconol"

    driver.get(itemLink)

    about = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/section[1]/div[1]/div[3]/section/p").get_attribute('innerHTML')
    #item info

    dataAvailability = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/section[1]/div[1]/div[3]/div[1]/div[1]/p").get_attribute('innerHTML')
    #data level

    
 
                                        
   


time.sleep(1000)
driver.quit()   