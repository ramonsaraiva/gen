import random

from mutations import GaussianElitismMutationMixin
from output import GeneticOutputMixin
from specimens import (
    SimpleSpecimen,
    Specimen,
    WeirdSpecimen,
)


class GeneticAlgorithm:

    specimen = Specimen

    population_size = 0
    generations = 0
    mutation_probability = 0.0

    def __init__(self, specimen=None):
        specimen = specimen or self.specimen
        self.population = [specimen() for _ in range(self.population_size)]

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

    def mutation(self):
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


class SimpleGeneticAlgorithm(GeneticOutputMixin, GaussianElitismMutationMixin,
                             GeneticAlgorithm):
    specimen = SimpleSpecimen

    population_size = 10
    generations = 10
    mutation_probability = 0.2

    def selection(self):
        return min(self.population)

    def crossover(self, selected):
        for specimen in self.population:
            specimen.crossover(selected)

    def process_generation(self, generation):
        selected = self.selection()
        self.crossover(selected)
        self.mutation(selected)
        self.calculate_fitness()
        self.output_population(generation)


class RouletteSelectionGeneticAlgorithm(SimpleGeneticAlgorithm):

    specimen = WeirdSpecimen

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