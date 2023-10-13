from random import randint

class Individual:
    def __init__(self, route="", fitness=0):
        self.route = route
        self.fitness = fitness

    def __lt__(self, other):
        return self.fitness < other.fitness
    
    def __gt__(self, other):
        return self.fitness > other.fitness

class TSPSolver:
    def __init__(self, tsp_matrix, num_cities=7, population_size=10):
        self.num_cities = num_cities
        self.population_size = population_size
        self.tsp_matrix = tsp_matrix

    def random_number(self, start, end):
        return randint(start, end-1)
    
    def has_repeat(self, s, ch):
        return ch in s

    def mutate_gene(self, route):
        route = list(route)
        while True:
            r = self.random_number(1, self.num_cities)
            r1 = self.random_number(1, self.num_cities)
            if r1 != r:
                temp = route[r]
                route[r] = route[r1]
                route[r1] = temp
                break
        return ''.join(route)

    def create_route(self):
        route = "0"
        while True:
            if len(route) == self.num_cities:
                route += route[0]
                break

            temp = self.random_number(1, self.num_cities)
            if not self.has_repeat(route, str(temp)):
                route += str(temp)

        return route

    def calculate_fitness(self, route):
        fitness = 0
        for i in range(len(route) - 1):
            if self.tsp_matrix[int(route[i])][int(route[i + 1])] == -1:
                return -1
            fitness += self.tsp_matrix[int(route[i])][int(route[i + 1])]

        return fitness

    def cooldown_temperature(self, temp):
        return (90 * temp) / 100

    def tsp_util(self):
        generation = 1
        generation_threshold = 100

        population = []
        
        for i in range(self.population_size):
            route = self.create_route()
            fitness = self.calculate_fitness(route)
            individual = Individual(route, fitness)
            population.append(individual)

        print("\nInitial population: \nROUTE     FITNESS VALUE\n")
        for individual in population:
            print(individual.route, individual.fitness)
        print()

        temperature = 10000

        while temperature > 1000 and generation <= generation_threshold:
            population.sort()
            print("\nCurrent temp: ", temperature)
            print("\n")
            new_population = []

            for i in range(self.population_size):
                p1 = population[i]

                while True:
                    new_route = self.mutate_gene(p1.route)
                    new_fitness = self.calculate_fitness(new_route)
                    new_individual = Individual(new_route, new_fitness)

                    if new_individual.fitness <= p1.fitness:
                        new_population.append(new_individual)
                        break

                    else:
                        prob = pow(
                            2.7,
                            -1
                            * (
                                (float)(new_individual.fitness - p1.fitness)
                                / temperature
                            ),
                        )
                        if prob > 0.5:
                            new_population.append(new_individual)
                            break

            temperature = self.cooldown_temperature(temperature)
            population = new_population
            print("Generation", generation)
            print("ROUTE  FITNESS VALUE")

            for individual in population:
                print(individual.route, individual.fitness)
            generation += 1

tsp_matrix = [ 
    [0, 12, 10, -1, -1, -1, 12],
    [12, 0, 8, 12, -1, -1, -1],
    [10, 8, 0, 11, 3, -1, 9],
    [-1, 12, 11, 0, 11, 10, -1],
    [-1, -1, 3, 11, 0, 6, 7],
    [-1, -1, -1, 10, 6, 0, 9],
    [12, -1, 9, -1, 7, 9, 0]
]

solver = TSPSolver(tsp_matrix)
solver.tsp_util()
