from PIL import Image
from flask import Flask
from flask_cors import CORS
import pytesseract

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

    ingredientsList = finalParse.split(",")
    return {"members": ingredientsList}

if __name__ == "__main__":
    app.run(debug=True)


