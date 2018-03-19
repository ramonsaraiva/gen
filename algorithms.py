from mutations import GaussianElitismMutationMixin
from output import GeneticOutputMixin
from selections import (
    RouletteSelectionMixin,
    SimpleSelectionMixin,
    StochasticSelectionMixin,
    TournamentThreeTwoSelectionMixin,
)
from specimens import (
    SimpleSpecimen,
    Specimen,
    WeirdSpecimen,
)


class GeneticAlgorithm:
    """
    Base class for a genetic algorithm
    """

    specimen = Specimen

    population_size = 0
    selection_size = 1
    generations = 0
    mutation_probability = 0.0

    def __init__(self, specimen=None):
        specimen = specimen or self.specimen
        self.population = [specimen(i) for i in range(self.population_size)]

    @property
    def fitnesses(self):
        return [specimen.fitness for specimen in self.population]

    def generate_population(self):
        for specimen in self.population:
            specimen.generate()

    def calculate_fitness(self):
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
        self.generate_population()
        self.calculate_fitness()

        for generation in range(self.generations):
            self.process_generation(generation)

        self.post()


class MetaGeneticAlgorithm(GeneticOutputMixin, GeneticAlgorithm):
    """
    A meta genetic algorithm follows the simple order of:
      * selection
      * crossover
      * mutation
      * fitness calculation
    """
    population_size = 10
    generations = 10
    mutation_probability = 0.2

    def crossover(self, selected):
        offset = 0
        for specimen in self.population:
            if specimen == selected[offset % len(selected)]:
                continue
            specimen.crossover(selected[offset % len(selected)])
            offset += 1

    def process_generation(self, generation):
        selected = list(self.selection())
        self.crossover(selected)
        self.mutation(selected)
        self.calculate_fitness()
        self.output_population(generation)


class SimpleGeneticAlgorithm(SimpleSelectionMixin, GaussianElitismMutationMixin,
                             MetaGeneticAlgorithm):
    """
    Simple genetic algorithm replicating what SimpleAG.cpp does
    """
    specimen = SimpleSpecimen


class RouletteSelectionGeneticAlgorithm(RouletteSelectionMixin,
                                        SimpleGeneticAlgorithm):
    specimen = WeirdSpecimen


class StochasticSelectionGeneticAlgorithm(StochasticSelectionMixin,
                                          GaussianElitismMutationMixin,
                                          MetaGeneticAlgorithm):
    specimen = WeirdSpecimen
    selection_size = 4


class TournamentSelectionGeneticAlgorithm(TournamentThreeTwoSelectionMixin,
                                          GaussianElitismMutationMixin,
                                          MetaGeneticAlgorithm):
    specimen = WeirdSpecimen