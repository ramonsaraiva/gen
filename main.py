from algorithms import (
    RouletteSelectionGeneticAlgorithm,
    StochasticSelectionGeneticAlgorithm,
)


if __name__ == '__main__':
    roulette = RouletteSelectionGeneticAlgorithm()
    stochastic = StochasticSelectionGeneticAlgorithm()

    #roulette.run()
    #roulette.plot_2d_fitness()

    stochastic.run()