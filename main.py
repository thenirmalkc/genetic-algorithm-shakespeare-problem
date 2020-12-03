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

# target to be reached
target = 'To be or not to be.'

# mutation rate
mulation_rate = 0.01

# size of population
population_size = 200



# main function
def main():

  p = Population(population_size, target, mulation_rate)

  p.generate_population()

  while True:
    # calculating fitness of individuals in population
    p.calc_fitness()

    # displaying info on screen
    print('\n')
    print('Best Individual:', ''.join(p.current.genes))
    print('Best Individual\'s fitness:', p.current.fitness * 100)
    print('\n')
    print('Total Generation:', p.generation)
    print('Average Fitness of', p.generation, 'generation population: ', p.avg_fitness * 100)
    print('\n')

    # checking if current best individual is equals to best individual
    if p.current.fitness == 1:
      break;

    # selecting parents for reproduction
    p.natural_selection()

    # reproducing new population
    p.reproduction()

    # clears screen
    clear()


main()
