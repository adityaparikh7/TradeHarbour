# black scholes for indian market
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def black_scholes_call_option(S, K, T, r, sigma):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    return call_price

def black_scholes_put_option(S, K, T, r, sigma):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    put_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price

# User input for the Indian market
S = float(input("Enter the current stock price in Indian Rupees: "))
K = float(input("Enter the option strike price in Indian Rupees: "))
T = float(input("Enter the time to expiration in years: "))
r = float(input("Enter the risk-free interest rate for the Indian market: "))
sigma = float(input("Enter the volatility of the underlying stock for the Indian market: "))

# Generate a range of stock prices
S_values = np.linspace(0.5 * S, 1.5 * S, 100)

# Calculate option prices
call_price = black_scholes_call_option(S, K, T, r, sigma)
put_price = black_scholes_put_option(S, K, T, r, sigma)

# Display results
print(f"Black-Scholes Call Option Price: {call_price:.2f} Indian Rupees")
print(f"Black-Scholes Put Option Price: {put_price:.2f} Indian Rupees")

# # Plotting the results
# plt.figure(figsize=(10, 6))
# plt.plot(S, call_price, label='Call Option Price', color='blue')
# plt.plot(S, put_price, label='Put Option Price', color='red')
# plt.axvline(x=S, linestyle='--', color='black', label='Current Stock Price')

# plt.title('Black-Scholes Option Pricing Model')
# plt.xlabel('Underlying Stock Price')
# plt.ylabel('Option Price')
# plt.legend()
# plt.grid(True)
# plt.show()


# import math
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.stats import norm


# def black_scholes_call_option(S, K, T, r, sigma):
#     d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
#     d2 = d1 - sigma * math.sqrt(T)
#     call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
#     return call_price


# def black_scholes_put_option(S, K, T, r, sigma):
#     d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
#     d2 = d1 - sigma * math.sqrt(T)
#     put_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
#     return put_price


# def get_input(prompt):
#     while True:
#         try:
#             value = float(input(prompt))
#             if value < 0:
#                 raise ValueError("Value cannot be negative.")
#             return value
#         except ValueError:
#             print("Invalid input. Please enter a valid numerical value.")


# def plot_option_prices(S_values, option_prices, option_type, S, K):
#     plt.figure(figsize=(10, 6))
#     if isinstance(option_prices, np.ndarray):
#         plt.plot(S_values, option_prices,
#                  label=f'{option_type} Option Price', color='blue')
#     else:
#         plt.axhline(y=option_prices, linestyle='--', color='blue',
#                     label=f'{option_type} Option Price')
#     plt.axvline(x=S, linestyle='--', color='black',
#                 label='Current Stock Price')
#     plt.axhline(y=K, linestyle='--', color='green', label='Strike Price')
#     plt.title(f'Black-Scholes {option_type} Option Pricing Model')
#     plt.xlabel('Underlying Stock Price')
#     plt.ylabel('Option Price')
#     plt.legend()
#     plt.grid(True)
#     plt.show()



# def main():
#     try:
#         S = get_input("Enter the current stock price in Indian Rupees: ")
#         K = get_input("Enter the option strike price in Indian Rupees: ")
#         T = get_input("Enter the time to expiration in years: ")
#         r = get_input(
#             "Enter the risk-free interest rate for the Indian market: ")
#         sigma = get_input(
#             "Enter the volatility of the underlying stock for the Indian market: ")

#         S_values = np.linspace(0.5 * S, 1.5 * S, 100)

#         option_type = input(
#             "Enter 'call' for call option, 'put' for put option, or 'both' for both options: ").lower()
#         if option_type == 'call':
#             option_prices = black_scholes_call_option(S_values, K, T, r, sigma)
#             plot_option_prices(S_values, option_prices, 'Call', S, K)
#         elif option_type == 'put':
#             option_prices = black_scholes_put_option(S_values, K, T, r, sigma)
#             plot_option_prices(S_values, option_prices, 'Put', S, K)
#         elif option_type == 'both':
#             call_prices = black_scholes_call_option(S_values, K, T, r, sigma)
#             put_prices = black_scholes_put_option(S_values, K, T, r, sigma)
#             plt.figure(figsize=(10, 6))
#             plt.plot(S_values, call_prices,
#                      label='Call Option Price', color='blue')
#             plt.plot(S_values, put_prices,
#                      label='Put Option Price', color='red')
#             plt.axvline(x=S, linestyle='--', color='black',
#                         label='Current Stock Price')
#             plt.axhline(y=K, linestyle='--', color='green',
#                         label='Strike Price')
#             plt.title('Black-Scholes Option Pricing Model')
#             plt.xlabel('Underlying Stock Price')
#             plt.ylabel('Option Price')
#             plt.legend()
#             plt.grid(True)
#             plt.show()
#         else:
#             print("Invalid option type. Please enter 'call', 'put', or 'both'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# if __name__ == "__main__":
#     main()
