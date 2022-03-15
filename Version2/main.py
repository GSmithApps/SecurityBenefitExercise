
import matplotlib.pyplot as plt
from options import call


rate = float(input("Enter the interest rate: ") or .00077)
volatility = float(input("Enter the volatility: ") or .0857)
tau = float(input("Enter the time (years): ") or 1.0)
strike_price = float(input("Enter the strike price: ") or 392.0)
spot_price_low = float(input("Enter the low spot price: ") or 300.)
spot_price_high = float(input("Enter the high spot price: ") or 380.)

import numpy as np

spot_prices = np.linspace(spot_price_low,spot_price_high,10)

call_prices = [call(
        S=graph_spot_price,
        K=strike_price,
        r=rate,
        sig=volatility,
        tau=tau
    ) for graph_spot_price in spot_prices]

fig, ax = plt.subplots()

ax.set_title(f"Call Vs. Spot at Strike: ${round(strike_price,1)}")
ax.set_xlabel("Spot Price")
ax.set_ylabel("Call Price")

ax.plot(spot_prices,call_prices)

plt.show()
# del plt
