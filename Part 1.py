# Consider a scenario where the temperature X(t) varies randomly over a continuous time interval
# t, where t is in the range from 0 to 1. We begin with the assumption that X(0) = 0, which means
# that the temperature at time 0 is 0. Now, if we choose a small time increment represented by
# ∆t, we can make the assumption that the change in temperature from time t to t + ∆t, denoted
# as X(t+ ∆t)− X(t), follows a normal distribution. This normal distribution is characterized by
# a mean of 0 and a variance of ∆t.

# 1. Let P be the random variable denoting the proportion of time in [0, 1] such that the
# temperature is positive. Estimate the distribution of P by Monte Carlo simulation and
# experimenting with various values of ∆t (e.g. ∆t = 0.01, 0.001, 0.0001, · · · .)

# 2. Let Tmax be the random variable denoting the time in [0, 1] such that the temperature
# is at its maximum. Estimate the distribution of Tmax by Monte Carlo simulation and
# experimenting with various values of ∆t (e.g. ∆t = 0.01, 0.001, 0.0001, · · · .)

# sources
# - random normal - https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
# - mean - https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# - pyplot - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

import numpy as np
import matplotlib.pyplot as plt


def monteCarloSimulation(deltaT, numSamples):
    temperatureChanges = np.random.normal(0, np.sqrt(deltaT), size = numSamples) 
    proportionPositive = np.mean(temperatureChanges > 0) 
    return proportionPositive

deltaTValues = [0.01, 0.001, 0.0001, 0.00001]
numSamples = 1000000

results = []

for deltaT in deltaTValues:
    proportionPositive = monteCarloSimulation(deltaT, numSamples)
    results.append((deltaT, proportionPositive))

for deltaT, proportionPositive in results:
    print(f"Delta_t: {deltaT}, Proportion Positive: {proportionPositive}")



