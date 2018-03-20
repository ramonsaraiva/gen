import numpy as np
import random


class SimpleSelectionMixin: 
    """Simple selection replicating the SimpleAG.cpp selection behaviour."""

    def selection(self):
        return [min(self.population)]


class RouletteSelectionMixin:
    """
    Selects N specimens, randomizing an offset and retrieving a specific
    specimen from the cumulative sum of each relative fitness.
    """

    def selection(self):
        fitnesses = self.fitnesses
        total_fitness = sum(fitnesses)

        relational_fitnesses = [
            fitness / total_fitness for fitness in fitnesses]

        for _ in range(self.selection_size):
            rand = random.random()
            probability_sum = 0
            for i, relational_fitness in enumerate(relational_fitnesses):
                probability_sum += relational_fitness
                if rand < probability_sum:
                    yield self.population[i]
                    break


class StochasticSelectionMixin:
    """
    Similar idea to the Roulette Selection, but adds a static interval to
    the starting random offset, for each specimen to be selected.
    (1 / length of the population)
    """

    def selection(self):
        fitnesses = self.fitnesses
        total_fitness = sum(fitnesses)

        probabilities = np.cumsum([
            fitness / total_fitness for fitness in fitnesses])

        initial_offset = random.random()
        spacing = 1 / len(self.population)
        offsets = [
            ((i * spacing) + initial_offset) % 1
            for i in range(self.selection_size)
        ]

        for offset in offsets:
            for i, probability in enumerate(probabilities):
                if offset < probability:
                    yield self.population[i]
                    break


class TournamentThreeTwoSelectionMixin:
    """
    Selects N specimens, starting with 3 random ones and yielding the one
    with better fitness. 
    """

    def selection(self):
        for _ in range(self.selection_size):
            yield max([
                self.population[random.randint(0, len(self.population) - 1)]
                for _ in range(3)])
