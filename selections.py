import numpy as np
import random


class RouletteSelection:

    def selection(self):
        fitnesses = self.fitnesses
        total_fitness = sum(fitnesses)

        relational_fitnesses = [
            fitness / total_fitness for fitness in fitnesses]

        rand = random.random()
        probability_sum = 0
        for i, relational_fitness in enumerate(relational_fitnesses):
            probability_sum += relational_fitness
            if rand < probability_sum:
                return self.population[i]


class StochasticUniversalSamplingSelection:

    def selection(self, n):
        # TODO: move relational fitnesses calculation to a common place
        fitnesses = self.fitnesses
        total_fitness = sum(fitnesses)

        relational_fitnesses = [
            fitness / total_fitness for fitness in fitnesses]
        probabilities = np.cumsum(relational_fitnesses)

        initial_offset = random.random()
        spacing = 1 / len(self.population)
        offsets = [
            ((i * spacing) + initial_offset) % 1
            for i in range(n)
        ]

        for offset in offsets:
            for i, probability in enumerate(probabilities):
                if offset < probability:
                    yield self.population[i]
                    break