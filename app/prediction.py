def prediction(filepath):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn import preprocessing
    import math, os, pickle

    df = pd.read_csv(filepath)
    df = df[['Open', 'High', 'Low', 'Adj Close', 'Volume']]
    df['HL_PCT'] = (df['High'] - df['Low']) / df['Adj Close'] * 100.0
    df['PCT_change'] = (df['Adj Close'] - df['Open']) / df['Open'] * 100.0
    df = df[['Adj Close', 'HL_PCT', 'PCT_change', 'Volume']]

    forecast_col = 'Adj Close'
    df.fillna(value=-99999, inplace=True)
    forecast_out = int(math.ceil(0.01 * len(df)))
    df['label'] = df[forecast_col].shift(-forecast_out)

    X = np.array(df.drop(['label'], axis=1))
    X = preprocessing.scale(X)
    X_lately = X[-forecast_out:]
    X = X[:-forecast_out]

    df.dropna(inplace=True)
    y = np.array(df['label'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model_path = os.path.join(os.path.dirname(__file__), '../models/linearregression.pickle')

    clf = LinearRegression(n_jobs=-1)
    clf.fit(X_train, y_train)
    with open(model_path, 'wb') as f:
        pickle.dump(clf, f)
    with open(model_path, 'rb') as f:
        clf = pickle.load(f)

    forecast_set = clf.predict(X_lately)
    df['Forecast'] = np.nan

    last_date = df.index[-1]
    next_unix = last_date + 1

    for i in forecast_set:
        df.loc[next_unix] = [np.nan for _ in range(len(df.columns) - 1)] + [i]
        next_unix += 1

    df['Adj Close'].plot()
    df['Forecast'].plot()
    plt.legend(loc=4)
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.show()

    os.remove(model_path)