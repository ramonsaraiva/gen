import matplotlib.pyplot as plt


class GeneticOutputMixin:

    def output_population(self, generation=None):
        if generation is not None:
            print('\nGeneration {}\n'.format(generation))
        for i, specimen in enumerate(self.population):
            print('Specimen {0}. {1}'.format(i, specimen))

    def fitness_population(self):
        for i in range(int(self.specimen.RANGE) + 1):
            v = i - self.specimen.RANGE_OFFSET
            specimen = self.specimen(i, v, v)
            specimen.calculate_fitness()
            yield specimen

    def plot_2d_fitness(self):
        ax, ay = [], []
        for specimen in self.fitness_population():
            ax.append(specimen.x)
            ay.append(specimen.fitness)

        plt.plot(ax, ay)
        plt.show()
