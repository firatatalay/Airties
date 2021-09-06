from flask import Flask
from db import getData
from models import Person

app = Flask(__name__)


@app.route('/persons')
def get_persons():
    ''''''
    persons = [Person(*person).serialize() for person in getData()]
    return {'persons': persons}, 200


if __name__ == "__main__":
    app.run()
