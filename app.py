from flask import Flask, render_template, request, redirect, url_for
from database import db
from models import *
import sqlite3
import io
import pytesseract
from PIL import Image
import data_manipulation
import detection


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///AllMeds.db"
db.init_app(app)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(allMeds))
    all_meds = result.scalars()

    return render_template('index.html', all_meds=all_meds)


@app.route("/extract_text_with_pytesseract")
def extract_text_with_pytesseract():
    image_path = 'static/med_1.png'
    response = detection.text_extraction_from_image(image_path)
    # with Image.open(image_path) as img:
    #
    #     extracted_text = pytesseract.image_to_string(img)
    #     extracted_text = extracted_text.lower()
    #     # return render_template('display.html', extracted_text=extracted_text)
    #     words = extracted_text.split()
    #     alphabets = data_manipulation.vec
    #     fake = False
    #     cnt = 0
    #     for word in words:
    #         if word.isdigit():
    #             first_char = word[0]
    #             if word not in alphabets[first_char]:
    #                 fake = True
    #                 break
    #         cnt += 1
    #         if cnt==5:
    #             break
    # return render_template("display.html", extracted_text=extracted_text, fake=fake)
    return render_template("display.html", response=response, image_path=image_path)


if __name__ == "__main__":
    app.run(debug=True)
