import itertools

# Distance matrix (symmetric)
# Example: 4 cities
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def travelling_salesperson(dist_matrix):
    n = len(dist_matrix)
    cities = range(n)
    best_path = None
    min_cost = float("inf")

    # Try all permutations of cities (excluding the first as start)
    for perm in itertools.permutations(cities[1:]):
        path = (0,) + perm + (0,)  # start and end at city 0
        cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
        
        if cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost

path, cost = travelling_salesperson(distances)
print("Best path:", path)
print("Minimum cost:", cost)
