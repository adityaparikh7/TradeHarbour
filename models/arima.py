import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# Define the ticker symbol
ticker_symbol = 'AAPL'  # Example: Apple Inc.

# Fetch historical stock price data using yfinance
stock_data = yf.download(ticker_symbol, start='2023-01-01', end='2024-03-01')

# Assuming your data contains 'Close' prices
# You might need to preprocess the data, handle missing values, etc.

# Splitting data into training and testing sets
train_size = int(len(stock_data) * 0.8)
train_data, test_data = stock_data[:train_size], stock_data[train_size:]

# Fit ARIMA model
model = ARIMA(train_data['Close'], order=(5, 1, 0))
model_fit = model.fit()

# Make predictions
predictions = model_fit.forecast(steps=len(test_data))[0]

# Calculate Mean Squared Error
mse = mean_squared_error(test_data['Close'], predictions)
print('Mean Squared Error:', mse)

# Visualize results
plt.figure(figsize=(10, 6))
plt.plot(test_data.index, test_data['Close'], label='Actual')
plt.plot(test_data.index, predictions, color='red', label='Predicted')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Actual vs. Predicted Stock Prices (ARIMA)')
plt.legend()
plt.show()
