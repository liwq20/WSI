import math 

class Values:

    def functionoftwo(x,y):
        e = math.e
        return 9*x*y/e**(x**2 + 1/2*x + y**2)
    
    def derivative_of_x(x,y):
        e = math.e
        return -9/2*(4*y*x**2 + x*y - 2*y) / e**(x**2 + x/2 + y**2)
    
    def derivative_of_y(x,y):
        e = math.e
        return -9*x *(2 *y**2 - 1) / e**(x**2 + x/2 + y**2)
    
    def check_in_bounds(point,bounds):

        for d in range(len(bounds)):
            if point[d] < bounds[d] or point[d] > bounds[d]:
                return False
        return True
    
    def custom_rank(scores):
    # Step 1: Sort the scores and get the indices
        sorted_indices = sorted(range(len(scores)), key=lambda i: scores[i])
        
        # Step 2: Create an array to hold the ranks
        ranks = [0] * len(scores)
        
        # Step 3: Assign ranks based on sorted indices
        for rank, index in enumerate(sorted_indices):
            ranks[index] = rank
    
        return ranks
    