import random

from specimens import (
    SimpleSpecimen,
    Specimen,
    WeirdSpecimen,
)


class GeneticAlgorithm:

    specimen = Specimen

    population_size = 0.0
    generations = 0.0
    mutation_probability = 0.0

    def __init__(self, specimen=None):
        specimen = specimen or self.specimen
        self.population = [specimen() for _ in range(self.population_size)]

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

    def mutation(self):
        raise NotImplementedError()

    def process_generation(self, generation):
        raise NotImplementedError()

    def run(self):
        self.generate_population()
        self.calculate_fitness()

        for generation in range(self.generations):
            self.process_generation(generation)


class GeneticOutputMixin:

    def output_population(self, generation=None):
        if generation is not None:
            print('\nGeneration {}\n'.format(generation))
        for i, specimen in enumerate(self.population):
            print('Specimen {0}. {1}'.format(i, specimen))


class SingleSelectionGeneticAlgorithm(GeneticAlgorithm):

    def crossover(self, selected):
        for specimen in self.population:
            specimen.crossover(selected)

    def mutation(self, selected):
        raise NotImplementedError

    def process_generation(self, generation):
        selected = self.selection()
        self.crossover(selected)
        self.mutation(selected)
        self.calculate_fitness()


class SimpleGeneticAlgorithm(GeneticOutputMixin,
                             SingleSelectionGeneticAlgorithm):
    specimen = SimpleSpecimen

    population_size = 10
    generations = 10
    mutation_probability = 0.2

    def selection(self):
        return min(self.population)

    def mutation(self, selected):
        """Gauss mutation with elitism"""
        for specimen in self.population:
            if specimen == selected:
                continue
            if random.random() < self.mutation_probability:
                specimen.mutate()

    def process_generation(self, generation):
        super().process_generation(generation)
        self.output_population(generation)


class RouletteSelectionGeneticAlgorithm(SimpleGeneticAlgorithm):

    specimen = WeirdSpecimen