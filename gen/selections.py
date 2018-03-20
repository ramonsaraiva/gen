import bisect
import itertools
import random

import numpy as np


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
        cumulative_fitnesses = np.cumsum(self.fitnesses)
        total = cumulative_fitnesses[-1]

        for _ in range(self.selection_size):
            yield self.population[
                bisect.bisect(cumulative_fitnesses, random.uniform(0, total))]


class StochasticSelectionMixin:
    """
    Similar idea to the Roulette Selection, but adds a static interval to
    the starting random offset, for each specimen to be selected.
    """

    def selection(self):
        cumulative_fitnesses = np.cumsum(self.fitnesses)
        total = cumulative_fitnesses[-1]
        avg = total / self.selection_size
        rand = random.random() * avg

        slices = itertools.islice(
            itertools.count(rand, avg), self.selection_size)
        for index in slices:
            yield self.population[bisect.bisect(cumulative_fitnesses, index)]

class TournamentThreeTwoSelectionMixin:
    """
    Selects N specimens, starting with 3 random ones and yielding the one
    with better fitness.
    """

    def selection(self):
        for _ in range(self.selection_size):
            yield max(random.sample(self.population, 3))