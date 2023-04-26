import csv
import os

from flask import Flask, render_template, request
from models import *

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("fruits.csv")
    reader = csv.reader(f)
    for id, name, family, calories, carbohydrates in reader:
        fruit = Fruit(id=id, name=name, family=family, calories=calories, carbohydrates=carbohydrates)
        db.session.add(fruit)
        print(f"Added {name} from {family} with {calories} calories and {carbohydrates} g carbohydrates.")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
