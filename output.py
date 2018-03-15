import random

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


class GeneticOutputMixin:

    def output_population(self, generation=None):
        if generation is not None:
            print('\nGeneration {}\n'.format(generation))
        for i, specimen in enumerate(self.population):
            print('Specimen {0}. {1}'.format(i, specimen))

    def generate_fitness_population(self):
        population = []
        for i in range(int(self.specimen.RANGE) + 1):
            v = i - self.specimen.RANGE_OFFSET
            specimen = self.specimen(v, v)
            specimen.calculate_fitness()
            population.append(specimen)
        return population

    def plot_2d_fitness(self):
        population = self.generate_fitness_population()

        plt.plot(
            [specimen.x for specimen in population],
            [specimen.fitness for specimen in population])
        plt.show()

    def plot_3d_fitness(self):
        population = self.generate_fitness_population()

        figure = plt.figure()
        ax = plt.axes(projection='3d')

        ax.plot3D(
            [specimen.x for specimen in population],
            [specimen.y for specimen in population],
            [specimen.fitness for specimen in population])
        plt.show()
