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

    #TODO сюда отправляем параметр, который получили по ссылке
    return jsonify(main())


if __name__ == '__main__':
    app.run(debug=True)
