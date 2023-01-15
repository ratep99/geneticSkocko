import random

choiceList = ["Skocko", "Tref", "Pik", "Srce", "Karo", "Zvezda"]
# Fitness function
def fitness(combination):
    score = 0
    rightElements=0
    wrongElements=0
    for i in range(4):
        if combination[i] == target[i]:
            rightElements+=1
            score += 1
        elif combination[i] in target:
            score += 0.5
            wrongElements+=1
    if(rightElements+wrongElements==4):
        for i in choiceList:
            if(i not in combination):
                choiceList.remove(i)
    return score

# Generate a population of combinations
def generate_population(size):
    population = []
    for i in range(size):
        combination = []
        for j in range(4):
            combination.append(random.choice(["Skocko", "Tref", "Pik", "Srce", "Karo", "Zvezda"]))
        population.append(combination)
    return population

# Select fittest combinations to be used as parents
def selection(population, fitness_scores):
    # Sort the population list by fitness score
    population = [combination for _, combination in sorted(zip(fitness_scores, population), key=lambda pair: pair[0])]
    parents = []
    # Set a minimum threshold for fitness scores
    min_threshold = 0.5
    for i in range(len(population)):
        if fitness_scores[i] > min_threshold:
            parents.append(population[i])
    # If no combinations have a fitness score above the threshold, select a random combination as a parent
    if not parents:
        parents.append(random.choice(population))
    return parents

# Create offspring from parent combinations using crossover and mutation
def crossover_and_mutation(parents, fitness_scores):
    offspring = []
    for i in range(int(len(parents)/2)):
        parent1 = parents[i]
        parent2 = parents[len(parents)-1-i]
        child = []
        # Use the number of right and wrong positions to determine which parent to choose
        for j in range(4):
            if fitness_scores[i][0] > fitness_scores[len(parents)-1-i][0]:
                child.append(parent1[j])
            elif fitness_scores[i][0] < fitness_scores[len(parents)-1-i][0]:
                child.append(parent2[j])
            elif fitness_scores[i][1] > fitness_scores[len(parents)-1-i][1]:
                child.append(parent1[j])
            else:
                child.append(parent2[j])
        # Mutate child with a small probability
        if random.uniform(0, 1) < 0.1:
            child[random.randint(0, 3)] = random.choice(["Skocko", "Tref", "Pik", "Srce", "Karo", "Zvezda"])
        offspring.append(child)
    return offspring

    # Set the target combination
target = ["Tref", "Pik", "Skocko", "Srce"]

# Set the population size
pop_size = 100

# Generate initial population
population = generate_population(pop_size)
print(f'Generated population: {population}')

# Run the genetic algorithm
generation = 0
while True:
    # Evaluate fitness of each combination
    fitness_scores = [fitness(combination) for combination in population]
    print(f'Generation {generation}: {max(fitness_scores)}')
    print(f'Fitness scores: {fitness_scores}')
    if max(fitness_scores) == 4:
        break
    parents = selection(population, fitness_scores)
    print(f'Selected parents: {parents}')
    offspring = crossover_and_mutation(parents,fitness_scores)
    population = offspring
    generation += 1
