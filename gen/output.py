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

    def draw_2d_fitness(self):
        plt.figure()
        plt.title("Fitness landscape")
        ax, ay = [], []
        for specimen in self.fitness_population():
            ax.append(specimen.x)
            ay.append(specimen.fitness)

        plt.plot(ax, ay)
        plt.scatter(
            *zip(*[(v[0], v[2]) for v in self._generations[0]]),  # ugly
            color='pink')
        plt.draw()

    def draw_2d_rounds(self):
        plt.figure()
        plt.title("Population per generation")
        plt.boxplot([
            [v[2] for v in generation] for generation in self._generations
        ])
        plt.draw()

    def draw_2d_fitness_fall(self):
        plt.figure()
        plt.title("Fitness fall")
        plt.plot([
            min([v[2] for v in generation])
            for generation in self._generations
        ])
        plt.draw()

    def show(self):
        plt.show()