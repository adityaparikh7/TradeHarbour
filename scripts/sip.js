function calculateSIP() {
  const investment = parseFloat(document.getElementById("investment").value);
  const rate = parseFloat(document.getElementById("rate").value);
  const time = parseFloat(document.getElementById("time").value);

  const monthlyRate = rate / 12 / 100; // Convert annual rate to monthly rate
  const months = time * 12; // Convert years to months

  // Calculate total investment and total returns
  const totalInvestment = investment * months;
  const totalReturns = calculateFutureValue(investment, monthlyRate, months);

  // Display results
  document.getElementById(
    "totalInvestment"
  ).textContent = `Total Investment: ${totalInvestment.toFixed(2)}`;
  document.getElementById(
    "totalReturns"
  ).textContent = `Total Returns: ${totalReturns.toFixed(2)}`;
}

function calculateFutureValue(investment, monthlyRate, months) {
  let futureValue = 0;
  for (let i = 0; i < months; i++) {
    futureValue = (futureValue + investment) * (1 + monthlyRate);
  }
  return futureValue;
}
