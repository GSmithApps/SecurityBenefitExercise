import random
from helpers import d_plus, d_minus, F, D, C
from base_option import option


class call_spread(option):
    """
    A call-spread option
    """

    def __init__(self,
                 S=396.86,
                 K_floor=392.93,
                 K_cap=392.93,
                 r_growth=0.001046,
                 r_discount=0.00077,
                 sig=0.0857,
                 t=1,
                 q=0
                 ):
        """
        initialize and valuate the call-spread
        """
        F_val = F(r_growth, t, S, q)
        d_plus_val_low = d_plus(sig, t, F_val, K_floor)
        d_plus_val_high = d_plus(sig, t, F_val, K_cap)
        C_floor = C(
            D=D(r_discount, t),
            F=F_val,
            K=K_floor,
            d_plus=d_plus_val_low,
            d_minus=d_minus(d_plus_val_low, sig, t)
        )
        C_cap = C(
            D=D(r_discount, t),
            F=F_val,
            K=K_cap,
            d_plus=d_plus_val_high,
            d_minus=d_minus(d_plus_val_high, sig, t)
        )
        self.valuation = C_floor - C_cap


# Default values should provide a zero-valued call spread because the cap and floor are the same
assert call_spread().valuation == 0

# If cap > floor (which is normal), then price > 0
assert call_spread(K_cap=410).valuation > 0

# If cap < floor (which is abnormal), then price < 0.
assert call_spread(K_cap=350).valuation < 0

# if the spot price is near the strike prices, the call-spread should be more valuable than
# if the spot price is far below the strike prices
# (assuming the same strike prices in both cases)
K_cap = 410
K_floor = 400
assert call_spread(K_cap=K_cap, K_floor=K_floor, S=380).valuation \
    > call_spread(K_cap=K_cap, K_floor=K_floor, S=300).valuation
del K_cap
del K_floor
