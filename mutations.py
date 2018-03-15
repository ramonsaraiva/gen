import random

class GaussianElitismMutationMixin:

    def mutation(self, selected):
        for specimen in self.population:
            if specimen == selected:
                continue
            if random.random() < self.mutation_probability:
                specimen.mutate()