import time

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from ParserAvitoTest import main

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getData', methods=["POST"])
def getdata():
    data = request.json
    print(data)
    print(data.get("link"))
    time.sleep(5)
    data = [
        {
            "id": "1",
            "link": "#",
            "square_field": "200",
            "square_house": "60",
            "price": "2000000",
            "price_per_meter": "1000",
            "phone": "988123123",
            "views_count": "6000",
        },
        {
            "id": "2",
            "link": "#",
            "square_field": "400",
            "square_house": "50",
            "price": "22340000",
            "price_per_meter": "234000",
            "phone": "18812223123",
            "views_count": "6500",
        },
    ]
    #TODO сюда отправляем параметр, который получили по ссылке
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
