import random as rand

from dna import DNA


class Population:

  def __init__(self, population_size, target, mutation_rate):
    # target
    self.target = target
    self.population_size = population_size
    self.mutation_rate = mutation_rate
    self.population = []
    self.generation = 0

    # total fitness of current generation
    self.total_fitness = 0
    # individual with best genes at current generation
    self.best_individual = None

    self.parents_size = 8 # minimum 2
    self.parents = []


  # generating random population
  def generate_population(self):
    self.population = []

    for i in range(self.population_size):
      # generating DNA of an individual
      self.population.append(DNA(len(self.target)))
      # generating random genes of an individual
      self.population[i].generate_random_genes()

    self.generation += 1


  # calculating fitness of the population
  def calc_fitness(self):
    self.best_individual = None
    self.total_fitness = 0

    for i in range(self.population_size):
      self.population[i].calc_fitness(self.target)
      if self.best_individual == None or self.best_individual.fitness < self.population[i].fitness:
        self.best_individual = self.population[i]
      self.total_fitness += self.population[i].fitness


  # selecting parents for reproduction
  def natural_selection(self):
    self.parents = []
    self.parents.append(self.best_individual)

    # calculating probability for selecting parent
    for i in range(self.population_size):
      self.population[i].prob = self.population[i].fitness / self.total_fitness

    # selecting parents for reproduction
    for i in range(self.parents_size - 1):
      temp = rand.random()

      for j in range(self.population_size):
        temp -= self.population[j].prob
        if temp <= 0:
          self.parents.append(self.population[j])
          break


  # reproducing new population from parents
  def reproduction(self):
    new_population = []

    for i in range(self.population_size):
      individual = DNA.cross_over(self.parents, len(self.target))
      individual.mutate(self.mutation_rate)
      new_population.append(individual)

    self.population = new_population
    self.generation += 1