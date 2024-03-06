import numpy
from zad1.Values import *


class SGDsolver:

    def __init__(self):
        self.starting_point_x = 0
        self.starting_point_y = 0
        self.wk = 0

    def changeradstartingpoints(self):
        values = numpy.random.uniform(-1,1,(1,2))
        self.starting_point_x = values[0,0]
        self.starting_point_y = values[0,1]

    def print_self_values(self):
        print(f"{self.starting_point_x},{self.starting_point_y},{self.wk}")

    def GD_minimum(self,steps,length_of_step):
      
        counter_of_steps = 0
        w_k = numpy.array([self.starting_point_x,self.starting_point_y])
        gradient_vector = numpy.array([Values.derivative_of_x(self.starting_point_x,self.starting_point_y),Values.derivative_of_y(self.starting_point_x,self.starting_point_y)])
        w_k_1 = numpy.array([0,0])
        w_k_1 = w_k - length_of_step * gradient_vector

        while counter_of_steps < steps - 1:

            x = w_k_1[0]
            y = w_k_1[1]
            w_k = w_k_1

            gradient_vector[0] = Values.derivative_of_x(x,y)
            gradient_vector[1] = Values.derivative_of_y(x,y)

            w_k_1 = w_k - length_of_step * gradient_vector

            counter_of_steps = counter_of_steps + 1

        return w_k_1
    
    def GD_maximum(self,steps,length_of_step):
      
        counter_of_steps = 0
        w_k = numpy.array([self.starting_point_x,self.starting_point_y])
        gradient_vector = numpy.array([Values.derivative_of_x(self.starting_point_x,self.starting_point_y),Values.derivative_of_y(self.starting_point_x,self.starting_point_y)])
        w_k_2 = numpy.array([0,0])
        w_k_2 = w_k + length_of_step * gradient_vector

        while counter_of_steps < steps - 1:

            x = w_k_2[0]
            y = w_k_2[1]
            w_k = w_k_2

            gradient_vector[0] = Values.derivative_of_x(x,y)
            gradient_vector[1] = Values.derivative_of_y(x,y)

            w_k_2 = w_k + length_of_step * gradient_vector
            

            counter_of_steps = counter_of_steps + 1

        return w_k_2
    
    def RealSGDMaximum(self,steps,length_of_step,number_of_gradient):
        if number_of_gradient > steps:
            return TypeError("Numbers of gradient cannot be bigger than number of steps")
        else:
            counter_of_steps = 0
            values = numpy.random.randint(steps,size=(1,number_of_gradient))
            w_k = numpy.array([self.starting_point_x,self.starting_point_y])
            gradient_vector = numpy.array([Values.derivative_of_x(self.starting_point_x,self.starting_point_y),Values.derivative_of_y(self.starting_point_x,self.starting_point_y)])
            w_k_3 = numpy.array([0,0])
            w_k_3 = w_k + length_of_step * gradient_vector


            while counter_of_steps < steps - 1:
                if counter_of_steps in values:
                    x = w_k_3[0]
                    y = w_k_3[1]
                    w_k = w_k_3

                    gradient_vector[0] = Values.derivative_of_x(x,y)
                    gradient_vector[1] = Values.derivative_of_y(x,y)

                    w_k_3 = w_k + length_of_step * gradient_vector
                    

                    counter_of_steps = counter_of_steps + 1
                else:
                    w_k = w_k_3
                    w_k_3 = w_k + length_of_step * gradient_vector
                    counter_of_steps = counter_of_steps + 1
                     
        return w_k_3
    
    def RealSGDMinimum(self,steps,length_of_step,number_of_gradient):
        if number_of_gradient > steps:
            return TypeError("Numbers of gradient cannot be bigger than number of steps")
        else:
            counter_of_steps = 0
            values = numpy.random.randint(steps,size=(1,number_of_gradient))
            w_k = numpy.array([self.starting_point_x,self.starting_point_y])
            gradient_vector = numpy.array([Values.derivative_of_x(self.starting_point_x,self.starting_point_y),Values.derivative_of_y(self.starting_point_x,self.starting_point_y)])
            w_k_4 = numpy.array([0,0])
            w_k_4 = w_k - length_of_step * gradient_vector


            while counter_of_steps < steps -1:
                if counter_of_steps in values:
                    x = w_k_4[0]
                    y = w_k_4[1]
                    w_k = w_k_4

                    gradient_vector[0] = Values.derivative_of_x(x,y)
                    gradient_vector[1] = Values.derivative_of_y(x,y)

                    w_k_4 = w_k - length_of_step * gradient_vector
                    

                    counter_of_steps = counter_of_steps + 1
                else:
                    w_k = w_k_4
                    w_k_4 = w_k - length_of_step * gradient_vector
                    counter_of_steps = counter_of_steps + 1
                     
        return w_k_4


    

def main():
    sgd = SGDsolver()
    sgd.changeradstartingpoints()
    print("\n")
    print(f"{sgd.starting_point_x} - starting x ")
    print(f"{sgd.starting_point_y}  - starting y\n")
    
    w_k_1 = sgd.GD_minimum(10000,0.0001)
    x = w_k_1[0]
    y= w_k_1[1]
    print(f"{x} - minimum x ")
    print(f"{y} - minimum y")
    minimum = Values.functionoftwo(x,y)
    print(f"{minimum} - minimum \n")
    
    
    w_k_2 = sgd.GD_maximum(10000,0.0001)
    x = w_k_2[0]
    y= w_k_2[1]
     
    print(f"{x} - maximum x ")
    print(f"{y} - maximum y")
    maximum = Values.functionoftwo(x,y)
    print(f"{maximum} - maximum \n")


    w_k_4 = sgd.RealSGDMinimum(10000,0.0001,20)
    x = w_k_4[0]
    y= w_k_4[1]
    print(f"{x} - minimum real x ")
    print(f"{y} - minimum real y ")
    realminimum= Values.functionoftwo(x,y)
    print(f"{realminimum} - realminimum \n")
    

    w_k_3 = sgd.RealSGDMaximum(10000,0.0001,20)
    x = w_k_3[0]
    y= w_k_3[1]
    print(f"{x} - maximum real x ")
    print(f"{y} - maximum real y ")
    realmaximum= Values.functionoftwo(x,y)
    print(f"{realmaximum} - realmaximum \n")

    
    

if __name__ == "__main__":
    main()