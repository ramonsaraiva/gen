import random

class GaussianElitismMutationMixin:

    @property
    def gaussian_multiplier(self):
        q = random.random()
        q = (q * 2.0) - 1.0
        q = q / 4.0
        return 1.0 + q

    def mutate(self, selected):
        self.x = self.x * self.gaussian_multiplier
        self.y = self.y * self.gaussian_multiplier