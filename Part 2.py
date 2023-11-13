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
# 

import numpy as np
import matplotlib.pyplot as plt

def monteCarloSimulation(deltaT, numSamples):
    temperatures = np.cumsum(np.random.normal(0, np.sqrt(deltaT), (numSamples, int(1/deltaT))), axis=1)
    timeOfMaximums = np.argmax(temperatures, axis=1) * deltaT
    meanTimeOfMaximum = np.mean(timeOfMaximums)
    return meanTimeOfMaximum, timeOfMaximums

deltaTValues = [0.01, 0.001, 0.0001, 0.00001]
numSamples = 1000

results = []

for deltaT in deltaTValues:
    meanTimeOfMaximum, timeOfMaximums = monteCarloSimulation(deltaT, numSamples)
    results.append((deltaT, meanTimeOfMaximum, timeOfMaximums))

for deltaT, timeOfMaximum, _ in results:
    print(f"Delta_t: {deltaT}, Time Of Maximum: {timeOfMaximum}")

fig, axes = plt.subplots(len(deltaTValues), 1, figsize=(10, 2 * len(deltaTValues)))

for i, (deltaT, meantTimeOfMaximum, timeOfMaximums) in enumerate(results):
    # Histogram
    axes[i,].hist(timeOfMaximums, bins=30, density=True, alpha=0.75)
    axes[i].set_xlabel('Time Maximum Temperature Reached')
    axes[i].set_ylabel('Probability Density')
    axes[i].set_title(f'Histogram (Delta_t={deltaT})')

plt.tight_layout()
plt.show()

