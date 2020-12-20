import random as rand
import math


class DNA:

  def __init__(self, genes_len):
    self.genes_len = genes_len
    self.genes = []
    self.fitness = 0
    self.prob = 0


  # generates random genes
  def generate_random_genes(self):
    self.genes = []

    for i in range(self.genes_len):
      self.genes.append(random_char())


  # calculates fitness of genes
  def calc_fitness(self, target):
    self.fitness = 0

    for i in range(self.genes_len):
      if self.genes[i] == target[i]:
        self.fitness += 1

    self.fitness = self.fitness / self.genes_len


  # performs cross over
  @staticmethod
  def cross_over(parents, genes_len):
    dna = DNA(genes_len)
    mid_point = rand.randrange(genes_len - 2) + 1
    parents = parents.copy()
    parent1 = parents.pop(rand.randrange(len(parents)))
    parent2 = parents.pop(rand.randrange(len(parents)))

    for i in range(genes_len):
      if i < mid_point:
        dna.genes.append(parent1.genes[i])
      else:
        dna.genes.append(parent2.genes[i])

    return dna


  # mutates genes
  def mutate(self, mutation_rate):
    for i in range(self.genes_len):
      if mutation_rate > rand.random():
        self.genes[i] = random_char()



# generates random characters
def random_char():
  return chr(rand.randrange(32, 127))