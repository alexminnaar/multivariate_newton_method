import numpy as np
import numdifftools as nd

class multivariate_newton(object):

    def __init__(self,func,start_point,step_size=0.8,num_iter=100,tol=0.000001):
        '''
        func: function to be optimized. Takes a vector argument as input and returns
              a scalar output
        step_size: step size in newton method update step
        num_iter: number of iterations for newton method to run
        tol: tolerance to determine convergence
        '''
        self.func=func
        self.start_point=np.array(start_point)
        self.num_iter=num_iter
        self.step_size=step_size
        self.tol=tol


    def newton_method(self):
        '''
        perform multivariate newton method for function with vector input
        and scalar output
        '''
        x_t=self.start_point
        #Get an approximation to hessian of function
        H=nd.Hessian(self.func)
        #Get an approximation of Gradient of function
        g=nd.Gradient(self.func)

        for i in range(self.num_iter):
            x_tplus1=x_t-self.step_size*np.dot(np.linalg.inv(H(x_t)),g(x_t))
            #check for convergence
            if abs(max(x_tplus1-x_t))<self.tol:
                break
            x_t=x_tplus1

        self.crit_point=x_tplus1
        self.max_min=self.func(x_t)

        return self

    def critical_point(self):
        '''
        print critical point found in newton_method function. newton_method function
        must be called first.
        '''
        print self.crit_point

