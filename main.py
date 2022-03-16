
import matplotlib.pyplot as plt
from option_call import call
import json
import numpy as np

with open('input_data.json') as f:
    input_data = json.load(f)
call_data = input_data['call']

spot_prices = np.linspace(
    call_data['spot_price_low'], call_data['spot_price_high'], 10)

call_prices = [call(
    S=graph_spot_price,
    sig=call_data['volatility'],
    r_growth=call_data['rate_growth'],
    r_discount=call_data['rate_risk_free'],
    q=call_data['dividend_rate'],
    t=call_data['t'],
    K=call_data['strike_price']
).valuation for graph_spot_price in spot_prices]

fig, ax = plt.subplots()

ax.set_title(f"Call Vs. Spot at Strike: ${round(call_data['strike_price'],1)}")
ax.set_xlabel("Spot Price ($)")
ax.set_ylabel("Call Price ($)")

ax.plot(spot_prices, call_prices)

plt.show()
# del plt
