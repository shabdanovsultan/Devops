from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name)

# Настройка подключения к MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Замените на вашу 
строку подключения

# Выберите базу данных
db = client["mydatabase"]

# Выберите коллекцию (таблицу)
collection = db["mycollection"]

@app.route('/add_data', methods=['POST'])
def add_data():
    # Принимаем данные от клиента
    data = request.json

    # Добавляем данные в MongoDB
    inserted_data = collection.insert_one(data)

    return jsonify({"message": "Данные успешно добавлены", "id": 
str(inserted_data.inserted_id)})

@app.route('/get_data', methods=['GET'])
def get_data():
    # Получаем данные из MongoDB
    data = list(collection.find({}))

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)


