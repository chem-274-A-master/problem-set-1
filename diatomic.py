"""
A class to represent a diatomic molecule.
"""

import math

import numpy as np


class DiatomicMassError(ValueError):
    pass


class Diatomic:
    def __init__(
        self, reduced_mass, force_constant, initial_separation, initial_velocity
    ):

        if reduced_mass <= 0:
            raise DiatomicMassError("Invalid mass for diatomic.")

        # Input quantities (constants)
        self.reduced_mass = reduced_mass
        self.force_constant = force_constant
        self.separation = initial_separation
        self.velocity = initial_velocity
        self.total_energy = self.potential_energy() + self.kinetic_energy()

        # Calculated quantities (constants)
        self.omega = math.sqrt(self.force_constant / self.reduced_mass)
        self.amplitude = math.sqrt(2 * self.total_energy / self.force_constant)

        self.phi = math.acos(self.separation / self.amplitude)

    def potential_energy(self):
        return 0.5 * self.force_constant * self.separation**2

    def kinetic_energy(self):
        return 0.5 * self.reduced_mass * self.velocity**2

    def analytical_position(self, t):
        return self.amplitude * np.cos(self.omega * t + self.phi)

    def analytical_velocity(self, t):
        return -self.amplitude * self.omega * np.sin(self.omega * t + self.phi)
