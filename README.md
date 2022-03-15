# SecurityBenefitExercise


## Exercise 1 : Testing Pandas

Attached is the exercise zip file,  Please extract and read ‘Instructions.txt’ to  complete the exercise.

link https://support.google.com/mail/answer/6590?hl=en#


---


## Exercise 2 : Black-Scholes and OOPS


Objective: Price different types of Options in Python using Object Oriented Programming

 

Description:

Using the concept of inheritance, price 3 different types of Options, namely:-

1. Call

2. Put

3. Call Spread (consists of 2 call options with different Strikes{Strike cap and Strike floor})

Pricing functions should use Black Scholes model

 

Create a python application/codebase which call the price functions for all 3 option types by assuming the inputs needed in Black Scholes within a reasonable data range.

 

Example Input for Black Sholes Model:

 

#Inputs for Black Scholes Model

spot = 396.86

volatility = 0.0857

growth_rate = 0.001046

discount_rate = 0.00077

dividend = 0

time_to_maturity = 1.0

strike = 392.93

 

Plot the relation between Spot and Call Price in line chart with atleast 5 data points and display the graph in output.

(Hint: Increase/Decrease the Spot with regular interval (keeping all other inputs constant) and note down the Calculated Price. Plot the data set(x:spot levels; y:Call price) in a line chart and display the graph in output)

 

Please respond to this email for any questions.




# Black Scholes Model

Call option:
$$C_0 = S_0 N(d_1) - Xe^{-rT}N(d_2)$$

Put Option:
$$P_0 = Xe^{-rT}N(-d_2) - S_0 N(-d_1)$$

$d_1$ and $d_2$:

$$d_1 = \frac{\ln \frac{S_0}{X} + (r + \frac{\sigma^2}{2})T}{\sigma \sqrt{T}}$$

$$d_2 = \frac{\ln \frac{S_0}{X} + (r - \frac{\sigma^2}{2})T}{\sigma \sqrt{T}}$$
 
 | Symbol | Description | Example Value |
| ----------- | ----------- | ----------- |
| $C_0$ | Price |  |
| $S_0$ | Stock Price (Spot Price) | 396.86 |
| $X$ | Exercise Price (strike price) | 392.93 |
| $r$ | Risk Free Interest Rate | 0.00077 |
| $T$ | Time to Expiration | 1.0 |
| $\sigma$ | volatility (sd of log-normal returns) | 0.0857 |


#Inputs for Black Scholes Model

growth_rate = 0.001046

discount_rate = 0.00077

dividend = 0



# Notes from wikipedia


General and market related:

$t$ is time in years, Generally $t=0$ is now

$r$ is the risk-free interest rate

Asset Related:

$S(t)$ is the price of the underlying Asset

$\mu$ is the drift rate of $S$

$\sigma$ is the standard deviation of the stock's log price

Option Related:

$V(S,t)$ is the price of an option as a function of the underlying asset $S$ at time $t$

$C(s,t)$ is the price of a call option

$P(s,t)$ is the price of a put option

$T$ time of option expiration

$\tau$ time until maturity, $\tau = T - t$

$K$ is the strike price

The equations are:

$$C(F,\tau) = D \left[ N(d_+) F - N(d_-) K \right]$$

$$d_+ = \frac{1}{\sigma \sqrt{\tau}} \left[ \ln \frac{F}{K} + \frac{1}{2}\sigma^2\tau\right]$$

$$d_- = d_+ - \sigma \sqrt{\tau}$$

And the auxiliary variables are 

$$D = e^{-r\tau}$$

$$F = e^{r\tau}S$$

Put Option:

$$P(F,\tau) = D \left[ N(-d_-) K - N(-d_+) F \right]$$
