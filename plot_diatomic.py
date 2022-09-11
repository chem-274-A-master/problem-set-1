"""
Make plots for diatomic.
"""

import math
import numpy as np
import matplotlib.pyplot as plt

from diatomic import Diatomic

k = 1
reduced_mass = 1
initial_separation = 1
initial_velocity = 1

period = 2 * math.pi * math.sqrt(reduced_mass / k)

times = np.linspace(0, 2 * period, 100)

diatomic = Diatomic(
    reduced_mass=reduced_mass,
    initial_separation=initial_separation,
    initial_velocity=initial_velocity,
    force_constant=k,
)

positions = diatomic.analytical_position(times)
velocities = diatomic.analytical_velocity(times)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(
    times,
    positions,
    color="#2565E8",
    label="Analytical Positions",
    markersize=5,
    marker="o",
)
ax.set_xlabel("Time")
ax.set_ylabel("Analytical Position")
ax.legend()
fig.savefig("analytical_positions.png", dpi=300)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(
    times,
    velocities,
    color="#D2042D",
    label="Analytical Velocity",
    markersize=5,
    marker="o",
)
ax.set_xlabel("Time")
ax.set_ylabel("Analytical Velocity")
ax.legend()
fig.savefig("analytical_velocities.png", dpi=300)

# With a twin axis
# not part of assignment
fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twinx()
ax.plot(
    times,
    velocities,
    color="#D2042D",
    label="Analytical Velocity",
    markersize=5,
)
ax.set_xlabel("Time")
ax.set_ylabel("Analytical Velocity")
ax2.plot(
    times,
    positions,
    color="#2565E8",
    label="Analytical Positions",
    markersize=5,
)
ax2.set_ylabel("Analytical Position")
ax.legend()
ax2.legend()
fig.savefig("twin_axes.png", dpi=300)
