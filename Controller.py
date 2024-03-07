from flask import Flask, render_template, jsonify, request
from ParserAvitoTest import main

app = Flask(__name__)

# Глобальная переменная для хранения данных
all_data = []


@app.route('/')
def index():
    # Передаем данные в шаблон и отображаем страницу
    return render_template('index.html', all_data=all_data) # не возвращается templane


@app.route('/getData', methods=["POST"])
def getdata():
    link = request.args.get("link")
    return jsonify(main(link))


if __name__ == '__main__':
    app.run(debug=True)
