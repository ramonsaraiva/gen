from algorithms import (
    RouletteSelectionGeneticAlgorithm,
    SimpleGeneticAlgorithm,
    StochasticSelectionGeneticAlgorithm,
    TournamentSelectionGeneticAlgorithm,
)


if __name__ == '__main__':
    simple = SimpleGeneticAlgorithm()
    roulette = RouletteSelectionGeneticAlgorithm()
    stochastic = StochasticSelectionGeneticAlgorithm()
    tournament = TournamentSelectionGeneticAlgorithm()

    #simple.run()
    #roulette.run()
    stochastic.run()
    #tournament.run()