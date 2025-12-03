class Solution1:

# The first step in gradient descent is to calculate the derivative (gradient) of the function.
#  The derivative gives the slope of the function.
# Start with an initial guess. In this problem the initial guess is given as a parameter.
# At each step, the current value (or guess) is updated by subtracting the product of the derivative and the learning rate.
# This process is repeated (iterated) a variable number of times. 
# Upon each iteration we will move closer to the point where the derivative is zero, which is the minimum of the function.

# own summary

# we have to match the tain data with the predicted output
# for generating correct output prediction error/ loss have to be mininmum which is our derivative function
# hsc level calculus math derivative y=x^2 derivative fx=y1=2*x
# now to minimize it using tangent over parabola we will decrease/increase the x using minimizer= minimizer - learning_rate*derivative
# so that minimizer goes to near x=0 where error = 0 ;so the probable result is correct
    
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        minimizer = init
        while iterations>0:
            iterations-=1
            derivative = 2* minimizer
            minimizer= minimizer - learning_rate*derivative
        return round(minimizer,5)

    