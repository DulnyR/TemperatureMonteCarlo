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
    temperatures = np.zeros((numSamples, int(1/deltaT)))
    proportions = np.zeros(numSamples)

    for i in range(1, numSamples):
        temperatureChanges = np.random.normal(0, np.sqrt(deltaT), int(1/deltaT))
        temperatures[i, :] = np.cumsum(temperatureChanges)

        positive_count = np.sum(temperatures[i, :] >= 0)
        proportions[i] = positive_count / len(temperatureChanges)

    proportionPositive = np.mean(proportions)
    return proportions, proportionPositive

deltaTValues = [0.01, 0.001, 0.0001, 0.00001]
numSamples = 1000

results = []

for deltaT in deltaTValues:
    proportions, proportionPositive = monteCarloSimulation(deltaT, numSamples)
    results.append((deltaT, proportionPositive, proportions))

for deltaT, proportionPositive, _ in results:
    print(f"Delta_t: {deltaT}, Proportion Positive: {proportionPositive}")

fig, axes = plt.subplots(len(deltaTValues), 1, figsize=(10, 2 * len(deltaTValues)))

all_bin_values = []

for i, (deltaT, proportionPositive, proportions) in enumerate(results):
    # Histogram
    _, bin_edges, hist_values = axes[i].hist(proportions, bins=30, density=True, alpha=0.75)
    
    # Save bin values for each deltaT
    all_bin_values.append((deltaT, hist_values, bin_edges))

    axes[i].set_xlabel('Time')
    axes[i].set_ylabel('Probability Density')
    axes[i].set_title(f'Histogram (Delta_t={deltaT})')

plt.tight_layout()
plt.show()





