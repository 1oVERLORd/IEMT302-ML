#!/usr/bin/env python3
"""
Simplest Machine Learning Example: Linear Regression
Demonstrates supervised learning by finding the mathematical relationship (y = 2x)
from training data without hardcoding the formula.
"""

from sklearn.linear_model import LinearRegression


def run_ml_demo():
    # 1. Training Data (Features X, Target Outputs y)
    X_train = [[1.0], [2.0], [3.0], [4.0], [5.0]]
    y_train = [2.0, 4.0, 6.0, 8.0, 10.0]

    # 2. Instantiate Model
    model = LinearRegression()

    # 3. Train Model
    print("Training the Linear Regression model on data...")
    model.fit(X_train, y_train)
    print("Training complete!")

    # 4. Predict
    X_test = [[6.0], [10.0], [25.0]]
    predictions = model.predict(X_test)

    # 5. Output Results
    print("\n--- Model Predictions ---")
    for input_val, pred in zip(X_test, predictions):
        print(f"Input X = {input_val[0]:<5} ---> Predicted y = {pred:.1f}")

    weight = model.coef_[0]
    bias = model.intercept_
    print("\n--- Learned Parameters ---")
    print(f"Learned Equation: y = ({weight:.2f} * x) + {bias:.2f}")


if __name__ == "__main__":
    run_ml_demo()