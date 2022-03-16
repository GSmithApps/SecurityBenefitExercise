# Security Benefit Black Scholes Exerecise

## Usage

- Input option data in [input_data.json](./input_data.json)
- Run main.py.
- A MatPlotLib plot will display the call price against spot levels.

## Model
 
 | Symbol | Description | Example Value |
| ----------- | ----------- | ----------- |
| $S$ | Spot Price | 396.86 |
| $\sigma$ | Volatility (sd of log-normal returns) | 0.0857 |
| $r_g$ | Growth Rate | 0.001046 |
| $r_f$ | Discount Rate | 0.00077 |
| q | Dividend | 0 |
| $t$ | Time To Maturity | 1 |
| $K$ | Strike Price | 392.93 |
| $C$ | Price of a call option | |
| $P$ | Price of a put option |  |
| $Z$ | Price of Call Spread | |

### Formulas

$$C = D \left[ N(d_+) F - N(d_-) K \right]$$

$$P = D \left[ N(-d_-) K - N(-d_+) F \right]$$

$$d_+ = \frac{1}{\sigma \sqrt{t}} \left[ \ln \frac{F}{K} + \frac{1}{2}\sigma^2t\right]$$

$$d_- = d_+ - \sigma \sqrt{t}$$

$$D = e^{-r_ft}$$

$$F = Se^{(r_g-q)t}$$

$$Z = C(K_{floor}) - C(K_{cap})$$

