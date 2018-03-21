import itertools
import random

from .output import GeneticOutputMixin
from .selections import (
    RouletteSelectionMixin,
    SimpleSelectionMixin,
    StochasticSelectionMixin,
    TournamentThreeTwoSelectionMixin,
)
from .specimens import (
    SimpleSpecimen,
    Specimen,
    WeirdSpecimen,
)


class GeneticAlgorithm:
    """Base class for a genetic algorithm"""

    specimen = Specimen

    population_size = 0
    selection_size = 1
    generations = 0
    mutation_probability = 0.0

    def __init__(self, specimen=None):
        specimen = specimen or self.specimen
        self.population = [specimen(i) for i in range(self.population_size)]
        self._generations = []

    @property
    def fitnesses(self):
        """Returns a list of fitnesses of every specimen in the population."""
        return [specimen.fitness for specimen in self.population]

    def generate_population(self):
        """Generates the data for each pre-allocated specimen."""
        for specimen in self.population:
            specimen.generate()

    def calculate_fitness(self):
        """Calculates the fitness for each specimen in the population."""
        for specimen in self.population:
            specimen.calculate_fitness()

    def selection(self):
        raise NotImplementedError()

    def crossover(self, selected):
        raise NotImplementedError()

    def mutation(self, selected):
        raise NotImplementedError()

    def process_generation(self, generation):
        raise NotImplementedError()

    def post(self):
        pass

    def run(self):
        """
        Runs the whole algorithm, generating a population, calculating its
        fitnesses and processing every generation.
        """
        self.generate_population()
        self.calculate_fitness()

        for generation in range(self.generations):
            self.process_generation(generation)

        self.post()


class MetaGeneticAlgorithm(GeneticOutputMixin, GeneticAlgorithm):
    """
    A meta genetic algorithm follows the simple order of:
      1. selection
      2. crossover
      3. mutation
      4. fitness re-calculation
    """
    population_size = 10
    generations = 10
    mutation_probability = 0.2

    def crossover(self, selected):
        """Crosses every specimen to one of the selected ones."""
        selected = itertools.cycle(selected)
        for specimen in self.population:
            current = next(selected)
            if specimen != current:
                specimen.crossover(current)

    def mutation(self, selected):
        """Mutates every unselected specimen based on a probability."""
        for specimen in self.population:
            mutate = random.random() < self.mutation_probability
            if specimen not in selected and mutate:
                specimen.mutate()

    def process_generation(self, generation):
        """Processes a generation, following the meta steps."""
        self._generations.append([
            (specimen.x, specimen.y, specimen.fitness)
            for specimen in self.population])

        selected = list(self.selection())
        self.crossover(selected)
        self.mutation(selected)
        self.calculate_fitness()

        self.output_population(generation)

    def post(self):
        self.draw_fitness_landscape()
        self.draw_fitnesses_per_generation()
        self.draw_fitness_fall()
        self.show()


class SimpleGeneticAlgorithm(SimpleSelectionMixin, MetaGeneticAlgorithm):
    """Simple genetic algorithm replicating SimpleAG algorithm behaviour."""
    specimen = SimpleSpecimen


class RouletteSelectionGeneticAlgorithm(RouletteSelectionMixin,
                                        MetaGeneticAlgorithm):
    """Roulette Selection with different specimen."""
    specimen = WeirdSpecimen
    selection_size = 1


class StochasticSelectionGeneticAlgorithm(StochasticSelectionMixin,
                                          MetaGeneticAlgorithm):
    """Stochastic Selection with different specimen."""
    specimen = WeirdSpecimen
    selection_size = 4


class TournamentSelectionGeneticAlgorithm(TournamentThreeTwoSelectionMixin,
                                          MetaGeneticAlgorithm):
    """Tournament (of three, of two) Selection with different specimen."""
    specimen = WeirdSpecimen
