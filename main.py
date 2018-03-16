from algorithms import (
    RouletteSelectionGeneticAlgorithm,
    SimpleGeneticAlgorithm,
)


if __name__ == '__main__':
    roulette = RouletteSelectionGeneticAlgorithm()
    roulette.run()
    roulette.plot_2d_fitness()