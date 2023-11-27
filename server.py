import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from tensorflow import keras
from scipy import ndimage

app = Flask(__name__)
CORS(app)  # Включаем CORS для всего приложения

model = keras.saving.load_model('model.keras')


def scale_and_center_symbol(image):
    labeled_objects, num_objects = ndimage.label(image)
    slices = ndimage.find_objects(labeled_objects)
    symbol_slice = slices[0]
    symbol = image[symbol_slice]

    target_size = 18

    ratio = min(target_size / symbol.shape[0], target_size / symbol.shape[1])
    scaled_symbol = ndimage.zoom(symbol, (ratio, ratio), order=0)
    new_image = np.zeros((28, 28))

    x_start = int((28 - scaled_symbol.shape[0]) / 2)
    x_end = x_start + scaled_symbol.shape[0]
    y_start = int((28 - scaled_symbol.shape[1]) / 2)
    y_end = y_start + scaled_symbol.shape[1]

    new_image[x_start:x_end, y_start:y_end] = scaled_symbol
    return new_image


def get_scheme_and_host():
    scheme = request.headers.get('X-Forwarded-Proto', request.scheme)
    host = request.headers.get('X-Forwarded-Host', request.host)

    return scheme, host


@app.route('/', methods=['GET'])
def index():
    scheme, host = get_scheme_and_host()
    return render_template('index.html', host=f'{scheme}://{host}')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Получаем JSON-массив из тела запроса
        data = request.get_json()

        input = np.array(data)

        prepared_image = scale_and_center_symbol(input.reshape((28, 28)))

        model_input = prepared_image.reshape((1, 28, 28, 1)).astype('float32') / 255
        predict = model.predict(model_input, verbose=False)

        number = np.argmax(predict)

        # Возвращаем успешный ответ
        return jsonify({'number': int(number), 'predict': predict.tolist()})
    except Exception as e:
        # В случае ошибки возвращаем сообщение об ошибке
        return jsonify({'status': 'error', 'message': str(e)})


if __name__ == '__main__':
    app.run('127.0.0.1', 8000)
