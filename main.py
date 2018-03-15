from algorithms import (
    RouletteSelectionGeneticAlgorithm,
    SimpleGeneticAlgorithm,
)

if __name__ == '__main__':

    roulette = RouletteSelectionGeneticAlgorithm()
    roulette.plot_2d_fitness()
    roulette.plot_3d_fitness()
