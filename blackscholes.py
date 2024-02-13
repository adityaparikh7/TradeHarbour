# black scholes for indian market
import math
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

# Calculate option prices
call_price = black_scholes_call_option(S, K, T, r, sigma)
put_price = black_scholes_put_option(S, K, T, r, sigma)

# Display results
print(f"Black-Scholes Call Option Price: {call_price:.2f} Indian Rupees")
print(f"Black-Scholes Put Option Price: {put_price:.2f} Indian Rupees")
