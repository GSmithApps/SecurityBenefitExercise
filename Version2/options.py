import random
from helpers import d_plus, d_minus, F, D, C, P

def call(S,K,r,sig,tau):
    F_val = F(r,tau,S)
    d_plus_val = d_plus(sig,tau,F_val,K)
    return C(
        D=D(r,tau),
        F=F_val,
        K=K,
        d_plus = d_plus_val,
        d_minus = d_minus(d_plus_val,sig,tau)
    )

# test 1

max_spot = random.uniform(250,350)

assert abs(call(
    S=random.uniform(200,max_spot),
    K=random.uniform(max_spot,700),
    r=.0000,
    sig=0.00000001,
    tau=random.uniform(1,50)
)) < 1e-5

del max_spot


# test 2

spot_price = random.uniform(200,350)
strike_price = random.uniform(spot_price,spot_price+50)
time = random.uniform(1,50)

# assert abs(call(
#     S=spot_price,
#     K=strike_price,
#     r=0.00077,
#     sig=0.0857,
#     tau=time
# ) - C0(
#     S0=spot_price,
#     X=strike_price,
#     r=0.00077,
#     sig=0.0857,
#     T=time
# )) < 1e-5

del spot_price
del strike_price
del time


def put(S,K,r,sig,tau):
    F_val = F(r,tau,S)
    d_plus_val = d_plus(sig,tau,F_val,K)
    return P(
        D=D(r,tau),
        F=F_val,
        K=K,
        d_plus=d_plus_val,
        d_minus=d_minus(d_plus_val,sig,tau)
    )

