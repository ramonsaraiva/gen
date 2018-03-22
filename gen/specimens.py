import math
import random

from .mutations import GaussianMutationMixin


class Specimen:
    """Base class for a specimen."""

    def __init__(self, id, x=None, y=None):
        self.id = id
        self.x = x
        self.y = y
        self.fitness = 0

    def __str__(self):
        return '{0:.3f} {1:.3f} {2:.3f}'.format(self.x, self.y, self.fitness)

    def __lt__(self, other):
        """Less than operator for specimen fitness comparison."""
        return self.fitness < other.fitness

    def __gt__(self, other):
        """Greater than operator for specimen fitness comparison."""
        return self.fitness > other.fitness

    def __eq__(self, other):
        """Proper equality check with pre-defined specimen ids."""
        return self.id == other.id

    def generate(self):
        raise NotImplementedError()

    def calculate_fitness(self):
        raise NotImplementedError()

    def crossover(self, other):
        raise NotImplementedError()

    def mutate(self):
        raise NotImplementedError()


class SimpleSpecimen(GaussianMutationMixin, Specimen):
    """Simple specimen replicating SimpleAG.cpp algorithm behaviour."""

    RANGE = 20.0
    RANGE_OFFSET = 10.0

    def generate(self):
        """Generates random X and Y values in a specific range."""
        self.x = (random.random() * self.RANGE) - self.RANGE_OFFSET
        self.y = (random.random() * self.RANGE) - self.RANGE_OFFSET

    def calculate_fitness(self):
        """Calculates a simple sum of powers fitness."""
        self.fitness = pow(self.x, 2) + pow(self.y, 2)

    def crossover(self, other):
        """Crosses over another specimen."""
        self.x = (self.x + other.x) / 2
        self.y = (self.y + other.y) / 2


class WeirdSpecimen(SimpleSpecimen):
    """Similar to a SimpleSpecimen but with a different fitness calculation."""

    RANGE = 100
    RANGE_OFFSET = 50

    def calculate_fitness(self):
        """Calculates a pretty weird fitness."""
        self.fitness = sum([
            math.sin(pow(self.x, 3.0)),
            math.sqrt(pow(self.x, 2.0)),  # mod x?
            math.sin(self.y) * 3.0,
            math.sqrt(math.sqrt(math.sqrt(pow(self.x, 2) + pow(self.y, 2))))
        ])
