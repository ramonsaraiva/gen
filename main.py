from algorithms import (
    SimpleGeneticAlgorithm,
    RouletteSelectionGeneticAlgorithm,
)

from specimens import WeirdSpecimen

if __name__ == '__main__':
    simple = SimpleGeneticAlgorithm()
    simple_and_weird = SimpleGeneticAlgorithm(specimen=WeirdSpecimen)
    roulette = RouletteSelectionGeneticAlgorithm()

    simple.run()
    simple_and_weird.run()
    roulette.run()