import random
pop, size, rate = [[random.randint(0,7) for i in range (8)] for i in range(100)], 8, 0.5
def fitness_function(c):
    attacks = sum(1 for i in range(8) for j in range(i+1, 8) if c[i]==c[j] or abs(c[i]-c[j])==j-i)
    return 28 - attacks

for gen in range(1, 5000):
    pop = sorted(pop, key=fitness_function, reverse=True)
    if fitness_function(pop[0]) == 28:
        print(f" {gen} Perfect Board: {pop[0]}"); break

    if gen % 100 == 1: print(f" Generation: {gen} Best Fitness: {fitness_function(pop[0])}/28")

    Nxt_gen = [pop[0]]
    while len(Nxt_gen) < 100:
        parent1, parent2 = random.choices(pop[:50], k=2)
        mix = random.randint(1, 7)
        Nxt_gen.append(parent1[:mix] + parent2[mix:])

    pop = [[random.randint(0, 7) if random.random() < rate else r for r in ind] for ind in Nxt_gen]




