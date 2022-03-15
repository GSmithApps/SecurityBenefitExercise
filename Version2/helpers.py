import math
from scipy.stats import norm
import random

def d_plus(sig, tau, F, K):
    return (math.log(F/K) + .5 * sig ** 2 * tau)/(sig * math.sqrt(tau))

def d_minus(d_plus, sig, tau):
    return d_plus - sig * math.sqrt(tau)

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

def D(r, tau):
    """
    D value in the alternative formulation
    """
    return math.exp(-r*tau)

def F(r,tau,S):
    """
    F value in the alternative formulation
    """
    return S* math.exp(r * tau)
