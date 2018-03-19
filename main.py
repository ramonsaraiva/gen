import argparse
import sys

from gen.algorithms import (
    RouletteSelectionGeneticAlgorithm,
    SimpleGeneticAlgorithm,
    StochasticSelectionGeneticAlgorithm,
    TournamentSelectionGeneticAlgorithm,
)


ALGORITHMS = {
    'simple': SimpleGeneticAlgorithm,
    'roulette': RouletteSelectionGeneticAlgorithm,
    'stochastic': StochasticSelectionGeneticAlgorithm,
    'tournament': TournamentSelectionGeneticAlgorithm,
}


def parse_args():
    parser = argparse.ArgumentParser(
        description='Genetic Algorithm selection methods')
    parser.add_argument(
        'algorithm', type=str, help='Genetic Algorithm type',
        choices=list(ALGORITHMS))
    return parser.parse_args(sys.argv[1:])


if __name__ == '__main__':
    # TODO: possibility to create generic algorithm with specific
    # selection, mutation, generations, selection_size, etc..
    args = parse_args()
    algorithm = ALGORITHMS[args.algorithm]()
    algorithm.run()

    algorithm.plot_2d_fitness()
