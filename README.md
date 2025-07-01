# Stock Predictor

A Python-based desktop application using **Tkinter** for GUI and **Scikit-learn (1.7.0)** for machine learning.  
It predicts future stock prices using Linear Regression and shows results via Matplotlib.
The purpose of this project is to learn about linear regression in a practical and a theoretical way.

---

## Features

- Login screen with validation (from `users.csv`)
- Predicts future stock prices using historical data (CSV)
- Trained model caching using Pickle
- Matplotlib graph display of prediction vs actual
- Auto-cleaning of models after usage

---

## Project Structure

stock_predictor/
│
├── app/
│ ├── init.py
│ ├── main.py # Main tkinter GUI
│ ├── login.py # Login logic
│ ├── prediction.py # ML logic (Linear Regression)
│ └── assets/
│ ├── background.jpg
│ ├── google.png
│ ├── facebook.png
│ └── ...
│
├── data/
│ ├── users.csv
│ ├── GOOG.csv
│ ├── FB.csv
│ └── ...
│
├── model/
│ └── linearregression.pickle # Auto-generated during prediction and then discarded as well
│
├── README.md
├── requirements.txt
├── .gitignore
└── run.py