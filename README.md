##How it works
Given a function that takes a vector input and returns a scalar, Newton's method for optimization is used to find the critical point.  Numdifftools is used to get approximations for the Hessian and gradient of the given function.  Here is an example.

  def f(x):
    return 12*x[0]**2+x[1]-12*x[0]*x[1]
  
  #initial guess  
  y=[-2,7]
  newt=multivariate_newton(f,y)
  newt.newton_method()
  newt.critical_point()



##Dependencies
Numpy and Numdifftools
