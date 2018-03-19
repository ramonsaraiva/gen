import math
import random


class Specimen:

    def __init__(self, id, x=None, y=None):
        self.id = id
        self.x = x
        self.y = y
        self.fitness = 0

    def generate(self):
        raise NotImplementedError()

    def calculate_fitness(self):
        raise NotImplementedError()

    def crossover(self, other):
        raise NotImplementedError()

    def mutate(self):
        raise NotImplementedError()


class SimpleSpecimen(Specimen):

    RANGE = 20.0
    RANGE_OFFSET = 10.0

    def __str__(self):
        return '{0:.3f} {1:.3f} {2:.3f}'.format(self.x, self.y, self.fitness)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.fitness < other.fitness

    def generate(self):
        self.x = (random.random() * self.RANGE) - self.RANGE_OFFSET
        self.y = (random.random() * self.RANGE) - self.RANGE_OFFSET

    def calculate_fitness(self):
        self.fitness = pow(self.x, 2) + pow(self.y, 2)

    def crossover(self, other):
        self.x = (self.x + other.x) / 2
        self.y = (self.y + other.y) / 2

    def mutate(self):
        self.x = self.x * self.gaussian_multiplier()
        self.y = self.y * self.gaussian_multiplier()

    def gaussian_multiplier(self):
        q = random.random()
        q = (q * 2.0) - 1.0
        q = q / 4.0
        return 1.0 + q


class WeirdSpecimen(SimpleSpecimen):

    RANGE = 200.0
    RANGE_OFFSET = 100.0

    def calculate_fitness(self):
        self.fitness = sum([
            math.sin(pow(self.x, 3.0)),
            math.sqrt(pow(self.x, 2.0)), # mod x?
            math.sin(self.y) * 3.0,
            math.sqrt(math.sqrt(math.sqrt(pow(self.x, 2) + pow(self.y, 2))))
        ])
