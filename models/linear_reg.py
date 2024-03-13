import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Define the ticker symbol
ticker_symbol = 'AAPL'  # Example: Apple Inc.

# Fetch historical stock price data using yfinance
stock_data = yf.download(ticker_symbol, start='2023-03-08', end='2024-03-12')

# Assuming your data contains 'Close' prices
# You might need to preprocess the data, handle missing values, etc.

# Feature Engineering (Adding additional features if needed)
# For simplicity, let's assume no additional features are used in this example

# Splitting data into features (X) and target (y)
X = np.arange(len(stock_data)).reshape(-1, 1)  # Using index as a feature
y = stock_data['Close'].values  # Target variable

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Training the model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions
predictions = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, predictions)
print('Mean Squared Error:', mse)

# Visualizing the results
plt.figure(figsize=(10, 6))
# plt.scatter(y_test, predictions)
# Plotting the actual prices
plt.scatter(X_test, y_test, color='blue', label='Actual Price')

# Plotting the predicted prices
plt.plot(X_test, predictions, color='red', label='Predicted Price')

plt.xlabel('True Values')
plt.ylabel('Predictions')
# plt.xlabel('Time')
# plt.ylabel('Price')
plt.title('True vs. Predicted Stock Prices (Linear Regression)')
plt.show()
