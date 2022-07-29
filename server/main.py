from PIL import Image
from flask import Flask
from flask_cors import CORS
import pytesseract
from re import I
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait     
from selenium.webdriver.common.by import By     
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)
CORS(app)

@app.route("/members")
def members():

    ingredients = pytesseract.image_to_string(Image.open('download.jpg')) # string of entire picture

    ingredientsInstance = ingredients.find("INGREDIENTS: ") # index where ingredietns start

    start = 0
    strObj = ""
    if len(ingredients) > ingredientsInstance :
        strObj = ingredients[0: start:] + ingredients[ingredientsInstance+13::] # remove all chars up to 'INGREDIENTS:'. 13 is to cut of the ingreidnts word
    #^ add support for non american

    periodInstance = strObj.find(".") # index where PERIOD IS

    finalParse = ""
    if len(strObj) > periodInstance :
        finalParse = strObj[0: periodInstance:] + strObj[len(strObj)::] # remove all chars after the last ingredient

    barcodes = finalParse.split(",")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10) # this lets webdriver wait 10 seconds for the website to load
    driver.get("https://www.ewg.org/skindeep/")


    ingredientData = []

    for barcode in barcodes:
        text_box = driver.find_element(By.CLASS_NAME, "homepage-search-input")
        text_box.send_keys(barcode)


        elems = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "eac-item [href]")))

        itemLink = elems[0].get_attribute('href') # link of item were serching

        driver.get(itemLink)

    

        itemName = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/section[1]/div[1]/div[3]/div[1]/div[2]/h2").get_attribute('innerHTML')
        #item name

        about = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/section[1]/div[1]/div[3]/section/p").get_attribute('innerHTML')
        #item info

        dataAvailability = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/section[1]/div[1]/div[3]/div[1]/div[1]/p").get_attribute('innerHTML')
        #data level



        cancerInfo = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/section[1]/div[1]/div[3]/section/section/ul/li[1]/div[1]").text
        allergyInfo = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/section[1]/div[1]/div[3]/section/section/ul/li[2]/div[1]").text
        toxicInfo = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/section[1]/div[1]/div[3]/section/section/ul/li[3]/div[1]").text
        restrictInfo = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/section[1]/div[1]/div[3]/section/section/ul/li[4]/div[1]").text
        #common concerns data

        ingredientData.append("Ingredient;" + itemName + ":"+ "Information;" + about + ":" + "Amount of Research Done;" + dataAvailability + ":" + "Cancer;" + cancerInfo + ":" + "Allergies/Immunotoxicity;" + 
                            allergyInfo +":" + "Developmental Toxicity;" + toxicInfo + ":" + "Worldwide Restrictions on Use;" + restrictInfo)
                                            
    


    time.sleep(1000)
    driver.quit()   


    return {"members": barcodes}

if __name__ == "__main__":
    app.run(debug=True)


