import random
from helpers import d_plus, d_minus, F, D, P
from base_option import option


class put(option):
    """
    A class for a put option. It derives from the base option class
    """

    def __init__(
        self,
        S=396.86,
        sig=0.0857,
        r_growth=0.001046,
        r_discount=0.00077,
        q=0,
        t=1,
        K=392.93,
    ):
        """
        Initialize and valuate a put option
        """
        F_val = F(r_growth, t, S, q)
        d_plus_val = d_plus(sig, t, F_val, K)
        self.valuation = P(
            D=D(r_discount, t),
            F=F_val,
            K=K,
            d_plus=d_plus_val,
            d_minus=d_minus(d_plus_val, sig, t)
        )


# assert that a put option with no growth or volatility
# should be zero if the strike price is below the spot price

assert put(
    r_growth=0.000001,
    r_discount=0.00001,
    sig=0.00001
).valuation < 1E-5


# assert that a put option with no growth or volatility
# should be priced at the difference between the strike and spot

strike_price = 380
spot_price = 390

assert abs(put(
    r_growth=0.000001,
    r_discount=0.00001,
    sig=0.00001,
    S=spot_price,
    K=strike_price
).valuation) - abs(spot_price - strike_price) < 1E-5

del strike_price
del spot_price

# assert that the value of a put (or call, for that matter)
# increases with volatility

assert put(sig=.0857+.01).valuation > put(sig=.0857).valuation
