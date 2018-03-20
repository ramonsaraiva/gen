import random

class GaussianMutationMixin:

    @property
    def gaussian_multiplier(self):
        """Multiplier used for the mutation of each value of a specimen."""
        q = random.random()
        q = (q * 2.0) - 1.0
        q = q / 4.0
        return 1.0 + q

    def mutate(self):
        self.x = self.x * self.gaussian_multiplier
        self.y = self.y * self.gaussian_multiplier