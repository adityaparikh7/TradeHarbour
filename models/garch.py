# use yahoo finance and garch model to make stock prediction

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from arch import arch_model

# download stock data
ticker = 'BAJFINANCE'
data = yf.download(ticker, start='2023-03-08', end='2024-03-08')['Adj Close']
returns = 100 * data.pct_change().dropna()

# fit GARCH(1, 1) model
model = arch_model(returns, vol = 'Garch', p = 1, q = 1)
model_fit = model.fit()

# make prediction
horizon = 5
forecasts = model_fit.forecast(horizon = horizon)
print(forecasts.mean.iloc[-1])
print(forecasts.residual_variance.iloc[-1])
print(forecasts.variance.iloc[-1])

# plot prediction
plt.plot(forecasts.mean.iloc[-1])
plt.plot(forecasts.variance.iloc[-1])
plt.xlabel('Days')
plt.ylabel('Return')
plt.title(f"{ticker} Stock Return Prediction")
plt.show()

# plot stock price
plt.plot(data)
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title(f"{ticker} Stock Price")
plt.show()

# # plot stock return
# plt.plot(returns)
# plt.show()

# # plot residual
# residual = model_fit.residual / model_fit.conditional_volatility
# plt.plot(residual)
# plt.show()