import random
from helpers import d_plus, d_minus, F, D, C
from base_option import option

class call(option):
    """
    Call option class
    """

    def __init__(
        self,
        S = 396.86,
        sig = 0.0857,
        r_growth = 0.001046,
        r_discount = 0.00077,
        q = 0.0,
        t = 1.0,
        K = 392.93
    ):
        """
        Initialize and valuate a call option
        """
        F_val = F(r_growth,t,S, q)
        d_plus_val = d_plus(sig,t,F_val,K)
        self.valuation = C(
            D=D(r_discount,t),
            F=F_val,
            K=K,
            d_plus = d_plus_val,
            d_minus = d_minus(d_plus_val,sig,t)
        )


# assert that if the volatility, growth, and discount are zero, then
# then if the strike price is greater than the spot price,
# the value is zero

max_spot = random.uniform(250,350)

assert abs(call(
    S=random.uniform(200,max_spot),
    sig=0.00000001,
    r_growth=.0000,
    r_discount=.0000,
    q=0,
    t=random.uniform(1,50),
    K=random.uniform(max_spot,700)
).valuation) < 1e-5


# assert that the value of a call (or put, for that matter)
# increases with volatility

assert call(sig=.0857+.01).valuation > call(sig=.0857).valuation