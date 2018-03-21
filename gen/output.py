import matplotlib.pyplot as plt


class GeneticOutputMixin:

    def output_population(self, generation=None):
        """Outputs every specimen of a generation."""
        if generation is not None:
            print('\nGeneration {}\n'.format(generation))
        for i, specimen in enumerate(self.population):
            print('Specimen {0}. {1}'.format(i, specimen))

    def fitness_population(self):
        """Yields every specimen for a fitness landscape view."""
        for i in range(int(self.specimen.RANGE) + 1):
            v = i - self.specimen.RANGE_OFFSET
            specimen = self.specimen(i, v, v)
            specimen.calculate_fitness()
            yield specimen

    def draw_fitness_landscape(self):
        """
        Draws a 2D fitness landscape.
        Scatters the initial population dispersion.
        """
        plt.figure()
        plt.title("Fitness landscape")

        ax, ay = zip(*[
            (specimen.x, specimen.fitness)
            for specimen in self.fitness_population()])
        plt.plot(ax, ay)

        print(self._generations[0])
        plt.scatter(
            *zip(*[(v[0], v[2]) for v in self._generations[0]]),
            color='pink')
        plt.draw()

    def draw_fitnesses_per_generation(self):
        """Draws the population fitnesses per generation."""
        plt.figure()
        plt.title("Population fitness per generation")
        plt.boxplot([
            [v[2] for v in generation] for generation in self._generations
        ])
        plt.draw()

    def draw_fitness_fall(self):
        """Draws the fitness fall (smallest fitness per generation)."""
        plt.figure()
        plt.title("Fitness fall")
        plt.plot([
            min([v[2] for v in generation])
            for generation in self._generations
        ])
        plt.draw()

    def show(self):
        """Shows all drawings and wait until they are closed."""
        plt.show()
