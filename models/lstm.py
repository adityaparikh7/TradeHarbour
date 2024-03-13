from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import yfinance as yf
from keras.models import load_model
import streamlit as st

start = '2020-01-01'
end = '2024-03-12'

st.title('TradeHarbour - Stock Price Prediction')

user_input = st.text_input('Enter the stock symbol', 'AAPL')
df = yf.download(user_input, start=start, end=end)

st.subheader('Data from Jan 2020 to March 2024')
st.write(df.describe())

st.subheader('Closing Price vs Time chart')
fig = plt.figure(figsize=(12, 6))
plt.plot(df['Close'])
st.pyplot(fig)

# st.subheader('Closing Price vs Time chart with 100MA')
# ma100 = df.Close.rolling(100).mean()
# fig = plt.figure(figsize=(12, 6))
# plt.plot(ma100)
# plt.plot(df.Close)
# st.pyplot(fig)

st.subheader('Closing Price vs Time chart with 100MA & 200MA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize=(12, 6))
plt.plot(ma100, 'r', label='100 Day MA')
plt.plot(ma200, 'g', label= '200 Day MA')
plt.plot(df.Close, 'b')
plt.legend(loc=0)
st.pyplot(fig)

# splitting data into training and testing
data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])

scaler = MinMaxScaler(feature_range=(0, 1))

data_training_array = scaler.fit_transform(data_training)

# splitting data into x_train and y_train
x_train = []
y_train = []

for i in range(100, data_training_array.shape[0]):
    x_train.append(data_training_array[i-100:i])
    y_train.append(data_training_array[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)

# building the LSTM model
# model = load_model('./keras_model.h5')
model = load_model('./LSTM_model.h5')

# testing the model
past_100_days = data_training.tail(100)
final_df = past_100_days.append(data_testing, ignore_index=True)
input_data = scaler.fit_transform(final_df)

x_test = []
y_test = []

for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i-100:i])
    y_test.append(input_data[i, 0])

x_test, y_test = np.array(x_test), np.array(y_test)
y_predicted = model.predict(x_test)
scaler = scaler.scale_

scale_factor = 1/0.00101725
y_predicted = y_predicted*scale_factor
y_test = y_test*scale_factor


# final plots
st.subheader('Predicted vs Actual Price')
fig2 = plt.figure(figsize=(12, 6))
plt.plot(y_test, 'b', label='Original Price')
plt.plot(y_predicted, 'r', label='Predicted Price')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
st.pyplot(fig2)

# cd models
# streamlit run lstm.py