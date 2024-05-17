from typing import Any

import pandas as pd
from loguru import logger
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from statsmodels.tsa.arima.model import ARIMA



def prepare_data():
    data = pd.read_csv("src/data/train.csv", header=0)
    logger.debug(data.head())

    # Preprocessing
    X = data[["district_id", "age_bin_id", "gender_id", "as_of_date_id"]]
    y = data["count"]

    # Split the data
    return train_test_split(X, y, test_size=0.2, random_state=42)


def get_model(model: Any):
    X_train, X_test, y_train, y_test = prepare_data()

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    logger.success(f"Model: {model.__class__.__name__}")
    logger.success(f"RMSE: {root_mean_squared_error(y_test, predictions)}")

    return model


def apply_model(model: Any):
    model = get_model(model)

    # Use the model to make predictions
    district_id = 10
    age_bin_id = 3
    gender_id = 1
    as_of_date_id = 130
    prediction = model.predict([[district_id, age_bin_id, gender_id, as_of_date_id]])
    logger.success(f"Predicted population count: {prediction[0]}")


def test_arima_model():
    # Prepare the data
    X_train, X_test, y_train, y_test = prepare_data()

    # Train the model
    model = ARIMA(y_train, order=(5, 1, 0))
    model_fit = model.fit(disp=0)

    # Evaluate the model
    predictions = model_fit.forecast(steps=len(y_test))[0]
    logger.success(f"Model: {model.__class__.__name__}")
    logger.success(f"RMSE: {root_mean_squared_error(y_test, predictions)}")

    return model_fit


def test():
    apply_model(LinearRegression())
    apply_model(DecisionTreeRegressor())
    apply_model(RandomForestRegressor())
    apply_model(
        GradientBoostingRegressor(
            n_estimators=100, learning_rate=0.1, max_depth=1, random_state=0, loss="ls"
        )
    )
    apply_model(SVR())
    apply_model(MLPRegressor(max_iter=500))


def generate_results():
    model = get_model(GradientBoostingRegressor())

    test_data = pd.read_csv("src/data/test.csv", header=0)
    X_test = test_data[["district_id", "age_bin_id", "gender_id", "as_of_date_id"]]

    predictions = model.predict(X_test)
    output = pd.DataFrame({"ID": test_data["ID"], "count": predictions})

    output.to_csv("submission.csv", index=False)


if __name__ == "__main__":
    # generate_results()
    test_arima_model()
