
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 5, 1
s = np.random.normal(mu, sigma, 165)
s2 = np.random.normal(mu, sigma, 165)
x = np.linspace(0, 165, 165)
events = np.zeros(165)


event_locations = [ 10, 25, 40, 50, 80, 88, 100, 120, 128, 135, 150, 160]
event_locations2 = [ 10, 32, 42, 50, 80, 93, 100, 120, 132, 150, 160]

for el in event_locations2:
    s2[el] += 2
    s2[el+1] += 3


for el in event_locations:
    s[el] += 4
    s[el+1] += 4


f, ax = plt.subplots(figsize=(18,5))
ax.plot(x, s)
plt.savefig('/Users/anthonydutcher/analysis/bold_fmri.eps', format='eps')

f, ax = plt.subplots(figsize=(18,5))
ax.plot(x, s2)
plt.savefig('/Users/anthonydutcher/analysis/bold_fmri2.eps', format='eps')


mu, sigma = 1, 0.25
s = np.random.normal(mu, sigma, 165)
x = np.linspace(0, 165, 165)
f, ax = plt.subplots(figsize=(18,5))
ax.plot(x, s)
plt.savefig('/Users/anthonydutcher/analysis/perceptual.eps', format='eps')