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

def monteCarloSimulation(deltaT, currentTemperature):
    temperatureChange = np.random.normal(0, np.sqrt(deltaT)) 
    return currentTemperature + temperatureChange

currentTemperature = 0
maxTemperature = 0
maxTemperatureTime = 0
results = []
timePoints = []
deltaT = 0.01

for i in range(1, int(1/deltaT)):
    results.append(currentTemperature)
    currentTemperature = monteCarloSimulation(deltaT, currentTemperature)
    if (currentTemperature > maxTemperature):
        maxTemperature = currentTemperature
        maxTemperatureTime = i * deltaT

for i in range(1, int(1/deltaT)):
    timePoints.append(i * deltaT)

print(maxTemperatureTime)

plt.plot(timePoints, results, marker='o')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Monte Carlo Simulation of Temperature Changes')
plt.show()


