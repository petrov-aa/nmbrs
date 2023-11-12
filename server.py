import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow import keras

app = Flask(__name__)
CORS(app)  # Включаем CORS для всего приложения

model = keras.saving.load_model('model.keras')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Получаем JSON-массив из тела запроса
        data = request.get_json()

        input = np.array(data)
        input = input.reshape((1, 28, 28))
        predict = model.predict(input).tolist()

        number = np.argmax(predict)

        # Возвращаем успешный ответ
        return jsonify({'number': number, 'predict': predict})
    except Exception as e:
        # В случае ошибки возвращаем сообщение об ошибке
        return jsonify({'status': 'error', 'message': str(e)})


if __name__ == '__main__':
    # Запуск сервера на порте 5000
    app.run(host='0.0.0.0', port=5000)
