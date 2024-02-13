function calculateOptionPrices() {
  var S = parseFloat(document.getElementById("stockPrice").value);
  var K = parseFloat(document.getElementById("strikePrice").value);
  var T = parseFloat(document.getElementById("timeToExpiration").value);
  var r = parseFloat(document.getElementById("interestRate").value);
  var sigma = parseFloat(document.getElementById("volatility").value);

  var d1 =
    (Math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * Math.sqrt(T));
  var d2 = d1 - sigma * Math.sqrt(T);

  var callPrice =
    S * cumulativeDistributionFunction(d1) -
    K * Math.exp(-r * T) * cumulativeDistributionFunction(d2);
  var putPrice =
    K * Math.exp(-r * T) * cumulativeDistributionFunction(-d2) -
    S * cumulativeDistributionFunction(-d1);

  document.getElementById("callPrice").textContent =
    "Black-Scholes Call Option Price: " + callPrice.toFixed(2);
  document.getElementById("putPrice").textContent =
    "Black-Scholes Put Option Price: " + putPrice.toFixed(2);
}

// Cumulative Distribution Function (CDF) for the standard normal distribution
function cumulativeDistributionFunction(x) {
  return (1 + erf(x / Math.sqrt(2))) / 2;
}

// Error Function (erf) approximation
function erf(x) {
  var sign = x >= 0 ? 1 : -1;
  x = Math.abs(x);

  // Coefficients for the approximation
  var a1 = 0.254829592;
  var a2 = -0.284496736;
  var a3 = 1.421413741;
  var a4 = -1.453152027;
  var a5 = 1.061405429;
  var p = 0.3275911;

  // Calculation
  var t = 1.0 / (1.0 + p * x);
  var y = (((a5 * t + a4) * t + a3) * t + a2) * t + a1;
  return sign * (1.0 - y * Math.exp(-x * x));
}
