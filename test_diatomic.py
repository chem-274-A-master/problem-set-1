"""
Tests for the diatomic class
"""

import math
import numpy as np


from diatomic import Diatomic, DiatomicMassError


def test_constructor():

    # Should have different values for each parameter so that assignment is
    # properly tested.
    diatomic = Diatomic(
        reduced_mass=1, force_constant=2, initial_separation=3, initial_velocity=4
    )

    # Check values specified in the constructor.
    assert diatomic.reduced_mass == 1.0
    assert diatomic.force_constant == 2.0
    assert diatomic.separation == 3.0
    assert diatomic.velocity == 4.0

    # Check calculated values.
    assert math.isclose(diatomic.omega, math.sqrt(2))
    assert math.isclose(diatomic.amplitude, math.sqrt(17.0))
    assert math.isclose(diatomic.phi, 0.7559694104)


def test_constructor_error():
    # They weren't asked to do this, and there are other ways to do this with testing
    # frameworks, but this is something they should be able to do now.

    try:
        Diatomic(
            reduced_mass=-1,
            force_constant=2,
            initial_separation=3,
            initial_velocity=4.0,
        )
    except DiatomicMassError:
        pass
    else:
        # Would probably be more appropriate to make another error.
        raise ValueError("Mass error was not raised.")


def test_analytical_position():
    """Test analytical position."""

    # Their test might be a lot different than this, we're just looking to see that
    # they actually checked the output of their function.

    diatomic = Diatomic(
        reduced_mass=1, force_constant=2, initial_separation=3, initial_velocity=4
    )

    # Test actual calculation at some points.
    period = 2 * math.pi * math.sqrt(1 / 2)

    # At time 0 should be equal to initial separation.
    assert math.isclose(diatomic.analytical_position(0), 3.0)

    # Should be at the negative position at 0.5 period
    assert math.isclose(diatomic.analytical_position(0.5 * period), -3.0)

    # Should be at same position at 1 period
    assert math.isclose(diatomic.analytical_position(period), 3.0)


def test_analytical_velocity():

    # Their test might be a lot different than this, we're just looking to see that
    # they actually checked the output of their function.

    diatomic = Diatomic(
        reduced_mass=1, force_constant=2, initial_separation=3, initial_velocity=-4
    )

    # Test actual calculation at some points.
    period = 2 * math.pi * math.sqrt(1 / 2)

    # At time 0 should be equal to initial analytical velocity.
    # The formula of analytical velocity is always going to start with
    # a negative number, so I should think how to phrase this question
    # next time. Should be fixable by setting the phase differently.
    assert math.isclose(diatomic.analytical_velocity(0), -4.0)

    # Should be at the negative of starting at 0.5 period
    assert math.isclose(diatomic.analytical_velocity(0.5 * period), 4.0)

    # Should be at same velocity at 1 period
    assert math.isclose(diatomic.analytical_velocity(period), -4.0)


def test_analytical_position_bounds():
    """This test looks at the max and min observed positions and
    and compares it to the theoretical maximum and minimum (based on amplitude)"""

    diatomic = Diatomic(
        reduced_mass=1, force_constant=2, initial_separation=3, initial_velocity=4
    )

    period = 2 * math.pi * math.sqrt(1 / 2)

    times = np.linspace(0, 2 * period, 1000)

    positions = diatomic.analytical_position(times)

    max_observed = positions.max()
    min_observed = positions.min()

    assert max_observed <= diatomic.amplitude
    assert math.isclose(max_observed, diatomic.amplitude, abs_tol=0.00001)

    assert min_observed >= -diatomic.amplitude
    assert math.isclose(min_observed, -diatomic.amplitude, abs_tol=0.00001)
