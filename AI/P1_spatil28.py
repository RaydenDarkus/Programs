# Shreyas Patil
# G01382371
# Project 1 CS580

import numpy as np
import random
from math import comb
import math

# Define the objective function to minimize (number of uncovered pairs)
def objective_function(matrix):
    uncovered = set()
    f=0
    a = {(0,0),(0,1),(1,0),(1,1)}
    for col1 in range(k):
        for col2 in range(col1+1,k):
            for row in range(len(matrix)):
                if (matrix[row][col1], matrix[row][col2]) in a:
                    uncovered.add((matrix[row][col1], matrix[row][col2]))
            f = f + abs(len(uncovered)-len(a))
            uncovered.clear()
    return f

# Define the neighbor function (swap two values in a row)
def neighborhood(current_solution):
    n_rows, n_cols = len(current_solution), len(current_solution[0])
    # randomly select a column to swap the symbols of each row
    j = random.randint(0, n_cols-1)
    neighbors = []
    for i in range(n_rows):
        # create a new solution by swapping the symbol in cell (i,j)
        new_solution = [list(row) for row in current_solution]
        new_solution[i][j] = 1 - new_solution[i][j]
        neighbors.append(new_solution)
    return neighbors

# def acceptance_probability(delta_e,temperature):
#     if temperature<threshold:
#         return 0.0
#     else:
#         return 1.0/(1.0 + np.exp(-delta_e/temperature))

def simulated_annealing(initial_matrix,frozen_factor,cooling):
    current_matrix = initial_matrix
    current_cost = objective_function(current_matrix)
    best_matrix = current_matrix
    best_cost = current_cost
    temperature = float(initial_temp)
    iteration = 0
    criterion = ''
    f_iteration = 0
    while(temperature>0):
        if(objective_function(best_matrix) == 0):
            # f_iteration = 0
            criterion = 'Solution achieved'
            best_matrix = current_matrix
            best_cost = current_cost
            break
        if(temperature == 0):
            # f_iteration = 0
            criterion = 'Final Temperature Archived'
            best_matrix = current_matrix
            best_cost = current_cost
            break
        if(f_iteration == frozen_factor):
            criterion = 'Frozen'
            best_matrix = current_matrix
            best_cost = current_cost
            break
        neighbors = neighborhood(current_matrix)
        # best_neighbor = min(neighbors, key=objective_function)
        # best_neighbor_cost = objective_function(best_neighbor)
        #In case of a tie in the objective_function cost the best_neigbor chooses a random neighbor
        objective_values = [objective_function(neighbor) for neighbor in neighbors]
        min_value = min(objective_values)
        min_neighbors = [neighbors[i] for i in range(len(neighbors)) if objective_values[i] == min_value]
        best_neighbor = random.choice(min_neighbors)
        best_neighbor_cost = min_value
        delta_e = best_neighbor_cost - current_cost
        # print(temperature)
        if(delta_e<0):
            f_iteration = 0
            current_matrix = best_neighbor
            current_cost = best_neighbor_cost
        else:
            f_iteration+=1
            # new_val = round(new_val,6)
            prob = np.exp(-delta_e/temperature)
            # prob = round(prob,6)
            if np.random.rand()<prob:
                current_matrix = best_neighbor
                current_cost = best_neighbor_cost
        if current_cost < best_cost:
            best_matrix = current_matrix
            best_cost = current_cost
        temperature *= cooling
        iteration +=1
    return best_matrix,iteration,criterion,best_cost

#The values of the matrix
v = [0,1]
#The number of parameters
t=2
k=0
cooling = 0.99
threshold=0.5
f_iteration = 0
while(k!=5 and k!=6 and k!=7):
    k=int(input('Enter the value of k?5,6 or 7: '))

frozen_factor = pow(len(v),t) * comb(k,t)
initial_temp = k

for i in range(30):
    initial_matrix = [[random.choice(v) for j in range(k)] for i in range(6)]
    # initial_matrix = [[0, 0, 0, 0, 0,1,0], [0, 0, 0, 0, 0,0,0], [0, 0, 0, 0, 0,0,0], [0, 1, 0, 1, 0,1,0], [0,0,0,0,0,0,0],[0,0,0,0,0,1,1]]
    # initial_matrix = [[1, 0, 0, 1, 1], [0, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 1, 0]]

    print('The initial matrix is:')
    for i in range(6):
        for j in range(k):
            print(initial_matrix[i][j],end=' ')
        print()

    print('Initial Cost:',objective_function(initial_matrix))
    # neighbors = neighborhood(initial_matrix)
    # best_neighbor = min(neighbors, key=objective_function)
    solution_matrix,iterations,stop_criterion,best_cost =  simulated_annealing(initial_matrix,frozen_factor,cooling)
    print('Solution matrix:')
    for i in range(6):
        for j in range(k):
            print(solution_matrix[i][j],end=' ')
        print()

    print('Stop criterion:',stop_criterion)
    print('Iterations:',iterations)
    print('Best Cost:',best_cost )              