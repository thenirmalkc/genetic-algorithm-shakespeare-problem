from os import system, name
import random as rand

from population import Population


# clears screen
def clear():
  # for linux & mac
  if name == 'posix':
    system('clear')
  # for windows
  else:
    system('cls')


# Genetic Algorithm

# target
target = 'To be or not to be.'
# mutation rate
mutation_rate = 0.01
# size of population
population_size = 400


# main function
def main():
  p = Population(population_size, target, mutation_rate)
  p.generate_population()

  while True:
    # calculating fitness of individuals in population
    p.calc_fitness()

    print('\n')
    print(''.join(p.best_individual.genes))
    print('\n')
    print('Generation:', p.generation)
    print('Mutation Rate:', p.mutation_rate * 100, '%')
    print('Average Fitness: ', p.total_fitness / p.population_size * 100, '%')

    # checking if current best individual is equals to best individual
    if p.best_individual.fitness == 1:
      break

    # selecting parents for reproduction
    p.natural_selection()

    # reproducing new population
    p.reproduction()

    # clears screen
    clear()


main()