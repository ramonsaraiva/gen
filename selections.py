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

    def selection(self):
        pass