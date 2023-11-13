import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from tensorflow import keras

app = Flask(__name__)
CORS(app)  # Включаем CORS для всего приложения

model = keras.saving.load_model('model.keras')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', host='localhost:8000')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Получаем JSON-массив из тела запроса
        data = request.get_json()

        input = np.array(data)
        input = input.reshape((1, 28, 28))
        predict = model.predict(input)

        number = np.argmax(predict)

        # Возвращаем успешный ответ
        return jsonify({'number': int(number), 'predict': predict.tolist()})
    except Exception as e:
        # В случае ошибки возвращаем сообщение об ошибке
        return jsonify({'status': 'error', 'message': str(e)})
