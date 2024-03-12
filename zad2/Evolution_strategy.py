import numpy as np
from Values import *


'''
This class is used to solve the problem of finding the minimum or maximum of a function using the Evolution Strategy method.
The Evolution Strategy method is a heuristic optimization method that is used to find the minimum or maximum of a function.
The Evolution Strategy method is based on the idea of evolution, where the best individuals are selected and used to create new individuals.
'''


class Evolution_Strategy_Solver:

    def __init__(self):
        self.starting_point_x = 0
        self.starting_point_y = 0

    def changeradstartingpoints(self):
        values = np.random.uniform(-1,1,(1,2))
        self.starting_point_x = values[0,0]
        self.starting_point_y = values[0,1]

    def print_self_values(self):
        print(f"{self.starting_point_x},{self.starting_point_y}")

    '''
    n_iter - total iterations
    bounds - range beetween points
    mu - number of parents
    lam - number of children
    step_size - maximum step_size
    '''

    def E_S(n_iter,bounds,mu,lam):
        best = []
        best_eval = 0
        if lam >= mu:
            n_children = int(lam/mu)
            var = mu
        else:
            n_children = 1
            var = lam
        population = []
        scores = []
 

        for i in range(mu):
            Value = None
            candidate = [0,0]
            gaussian_noise1 = np.random.normal(0,0.1,size=2)
            while Value is None or Values.check_in_bounds(candidate,bounds):
                Value = 1
                candidate[0] = bounds[0] +  np.random.rand(1,1) * (bounds[1] - bounds[0]) + gaussian_noise1[0]
                candidate[1] = bounds[0] +  np.random.rand(1,1) * (bounds[1] - bounds[0]) + gaussian_noise1[1]
            population.append(candidate)

        for m in range(n_iter):
            for l in range(len(population)):
                x = population[l][0]
                y = population[l][1]
                scores.append(Values.functionoftwo(x,y))

            # Sorting values to the lowest

            ranks = Values.custom_rank(scores)
            new_population = []
            selected = [ j for j , h in enumerate(ranks) if h < mu] 

            # Implementing the elemination of the worst individuals
            for s in range(len(selected)):
                new_population.append(population[selected[s]])
            population = new_population
            scores = []
            for l in range(len(population)):
                x = population[l][0]
                y = population[l][1]
                scores.append(Values.functionoftwo(x,y))
            children = []

            for k in range(len(selected)):
                if scores[k] < best_eval:
                    best = population[k]
                    best_eval = scores[k]
                    print(f'loop {m+1}, iteration {k}, Best: f({best}) = {best_eval}\n')
                for c in range(n_children):
                    Value1 = None
                    child = [0,0]
                    gaussian_noise2 = np.random.normal(0,1,size=2)
                    while Value1 is None or Values.check_in_bounds(child,bounds):
                        Value1 = 1
                        a = np.random.rand()
                        values_list = np.array(np.random.choice(var, 2))
                        parent1 = population[values_list[0]]
                        parent2 = population[values_list[1]]
                        child[0] = a * parent1[0] + (1-a) * parent2[0] + gaussian_noise2[0]
                        child[1] = a * parent1[1] + (1-a) * parent2[1] + gaussian_noise2[1]
                    children.append(child)
            # lambda + u - children and parents
            if m == n_iter -1 :
                population = population
            else:
                population = population + children
            children = []
            scores = []
         
           
        length = len(population)
        return best,best_eval,length
    

    def E_M(n_iter,bounds,mu,lam):
        best = []
        best_eval = 0
        n_children = int(lam/mu)
        population = []
        scores = []
        var = mu
        new_population = []
      
 

        for i in range(lam):
            Value = None
            candidate = [0,0]
            gaussian_noise1 = np.random.normal(0,0.1,size=2)
            while Value is None or Values.check_in_bounds(candidate,bounds):
                Value = 1
                candidate[0] = bounds[0] +  np.random.rand(1,1) * (bounds[1] - bounds[0]) + gaussian_noise1[0]
                candidate[1] = bounds[0] +  np.random.rand(1,1) * (bounds[1] - bounds[0]) + gaussian_noise1[1]
            population.append(candidate)

        for m in range(n_iter):
            for l in range(len(population)):
                x = population[l][0]
                y = population[l][1]
                scores.append(Values.functionoftwo(x,y))

            # Sorting values to the lowest

            ranks = Values.custom_rank(scores)
         
            selected = []
            if mu ==  1:
                selected = [np.argmax(scores)]
            if mu == lam and len(population) == lam:
                for j,h in enumerate(ranks):
                    if  h < mu and len(selected) < mu:
                        selected.append(j)
            else:
                for j,h in enumerate(ranks):
                    if not h < mu and len(selected) < mu:
                        selected.append(j)
                    else:
                        if len(selected) == mu and j > min(selected) and h < ranks[min(selected)]:
                            selected.remove(min(selected))
                            selected.append(j)

            new_population = []
            # Implementing the elemination of the worst individuals
            
            for s in range(len(selected)):
                new_population.append(population[selected[s]])
            population = new_population
            scores = []
            for l in range(len(population)):
                x = population[l][0]
                y = population[l][1]
                scores.append(Values.functionoftwo(x,y))
            children = []

            for k in range(len(scores)):
                if scores[k] < best_eval:
                    best = population[k]
                    best_eval = scores[k]
                    print(f'loop {m+1}, iteration {k}, Best: f({best}) = {best_eval}\n')
                for c in range(n_children):
                    Value1 = None
                    child = [0,0]
                    gaussian_noise2 = np.random.normal(0,1,size=2)
                    while Value1 is None or Values.check_in_bounds(child,bounds):
                        Value1 = 1
                        a = np.random.rand()
                        values_list = np.array(np.random.choice(var, 2))
                        parent1 = population[values_list[0]]
                        parent2 = population[values_list[1]]
                        child[0] = a * parent1[0] + (1-a) * parent2[0] + gaussian_noise2[0]
                        child[1] = a * parent1[1] + (1-a) * parent2[1] + gaussian_noise2[1]
                    children.append(child)
            # lambda + u - children and parents
            if m == n_iter -1 :
                population = population
            else:
                population = population + children
            children = []
            scores = []
         
        length = len(population)
        return best,best_eval,length
    
    
    
def main():

    best1,score1,lenght= Evolution_Strategy_Solver.E_S(20,[-5,5],128,512)    
    best2,score2,lenght= Evolution_Strategy_Solver.E_M(20,[-5,5],128,512)
    print(f"Best found value: {best1},{score1},{lenght}\n")
    print(f"Best found value: {best2},{score2},{lenght}\n")
  
    
    

if __name__ == "__main__":
    main()