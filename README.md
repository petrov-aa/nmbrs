Simple MNIST recognition project with Web App Gui
===

## Technologies

* Python
* Keras
* ChatGPT

## Description

This project is just my first attempt of Neural networks. Model is trained under MNIST dataset with code from official
Keras documentation examples. I attempted to add Web App with interface to test trained network.

The Web App is 100% written by ChatGPT, backend is 50% written by ChatGPT.

## Demo

[https://nmbrs.prpd.xyz](https://nmbrs.prpd.xyz)

## How to run

After cloning the repository you are firstly recommended to create venv by running:

```bash
python3 -m venv venv
```

Then you need to activate venv:

```bash
source venv/bin/activate
```

Then you can install all required packages:

```bash
pip install -r requirements
```

And then run the app:


```bash
gunicorn server:app
```
