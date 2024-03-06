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

