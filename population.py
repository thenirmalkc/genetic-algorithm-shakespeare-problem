import random as rand

from dna import DNA


class Population:

  def __init__(self, population_len, target, mutation_rate):

    # individual with best genes
    self.best = target

    self.generation = 0
    # average fitness of current generation
    self.avg_fitness = 0
    self.population_len = population_len
    self.population = []
    self.mutation_rate = mutation_rate

    # individual with current best genes
    self.current = None

    # for reproduction
    # minimum 2
    self.parents_len = 4
    self.parents = []

  # generating random population
  def generate_population(self):
    self.population = []

    for i in range(self.population_len):
      # generating DNA of an individual
      self.population.append(DNA(len(self.best)))
      # generating random genes of an individual
      self.population[i].generate_genes()

    self.generation += 1


  # calculating fitness of the population
  def calc_fitness(self):

    for i in range(self.population_len):
      # calculating fitness of an individual
      self.population[i].calc_fitness(self.best)

      if self.current == None or self.current.fitness < self.population[i].fitness:
        self.current = self.population[i]

      self.avg_fitness += self.population[i].fitness

    self.avg_fitness = self.avg_fitness / self.population_len


  # selecting parents for reproduction
  def natural_selection(self):
    self.parents = []
    # including current best individual as a parent
    self.parents.append(self.current)

    pool = []

    for i in range(self.population_len):
      custom_fitness = int(self.population[i].fitness * 10 + 1)

      for j in range(custom_fitness):
        pool.append(self.population[i])

    for i in range(self.parents_len - 1):
      self.parents.append(pool[rand.randrange(len(pool))])



  # reproducing new population from parents
  def reproduction(self):
    new_population = []

    for i in range(self.population_len):
      individual = DNA.cross_over(self.parents.copy(), len(self.best))
      individual.mutate(self.mutation_rate)

      new_population.append(individual)

    self.population = new_population
    self.generation += 1