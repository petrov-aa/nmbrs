Simple MNIST recognition project with Web App Gui
===

This project is just my first attempt of Neural networks. Model is trained under MNIST dataset with code from official
Keras documentation examples. I attempted to add Web App with interface to test trained network.

My first try to implement deep learning with Neural Networks. Model is trained on the MNIST dataset. The web user interface
is inferred added to test trained model. You can draw a number and the backend will try to guess what number
was drawn.

The Web App is 100% written by ChatGPT, backend is 50% written by ChatGPT.

## Demo

[https://nmbrs.prpd.xyz](https://nmbrs.prpd.xyz)

## Stack

* Python 3.9
* Keras
* ChatGPT

## Changelog

### v2.0

1. The layers of the neural network were tuned according to the thoughts from the artile https://machinelearningmastery.com/display-deep-learning-model-training-history-in-keras/
2. Additional user input pre-processing added. The drawn number is scaled and centered before being sent to the neural network.

### v1.0

The neural network was built following the example from the official Keras documentation https://keras.io/examples/vision/mnist_convnet/.

## How to run

Tested on Python version 3.9.

1. Clone this repository and create the virtual environment:
    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

3. Install required libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:
    ```bash
    gunicorn server:app
    ```
