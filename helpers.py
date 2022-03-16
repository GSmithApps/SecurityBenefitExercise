import math
from scipy.stats import norm
import random


def d_plus(sig, t, F, K):
    """
    Returns the d+ value in the Black-Scholes model
    """
    return (math.log(F/K) + .5 * sig ** 2 * t)/(sig * math.sqrt(t))


def d_minus(d_plus, sig, t):
    """
    Returns the d- value in the Black-Scholes model
    """
    return d_plus - sig * math.sqrt(t)


def C(D, F, K, d_plus, d_minus):
    """
    Price of a call option using the alternative formulation
    """
    return D * (norm.cdf(d_plus) * F - norm.cdf(d_minus) * K)


def P(D, F, K, d_plus, d_minus):
    """
    Price of a put option using the alternative formulation
    """
    return D * (norm.cdf(-d_minus) * K - norm.cdf(-d_plus) * F)


def D(r, t):
    """
    D value in the alternative formulation
    """
    return math.exp(-r*t)


def F(r, t, S, q):
    """
    F value in the alternative formulation
    """
    return S * math.exp((r - q) * t)
