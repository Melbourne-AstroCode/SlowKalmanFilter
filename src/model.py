import numpy as np


class KalmanVDP():
    """ 
    The Kalman filter equations for the Van der Pol oscillator with process noise.
    Please see xx.ipynb for a detailed explanation
    """


    def __init__(self,dt):
        self.dt = dt
        self.n_states = 2 # the system has 2 hidden states (x,y)
        self.n_y = 1 # the system has one observation state z

    """
    The discrete measurement noise covariance matrix
    """
    def R_matrix(self,σm):
        scalar = σm**2
        return scalar * np.ones((self.n_y,self.n_y)) #todo fix ny nomenclature


    """
    The discrete process noise covariance matrix
    """
    def Q_matrix(self,x,μ,σp):
      
        F21 = -2.0*μ*x[0]*x[1]-1.0

        Q11 = 1 
        Q12 = self.dt*F21/2 
        Q21 = Q12 
        Q22 = self.dt**2*(F21**2) / 3 

        return self.dt*σp**2*np.array(([Q11,Q12],[Q21,Q22]))


    """
    The state evolution function \dot{x} = f(x)
    """
    def f(self,x,μ):
        dx = np.zeros_like(x)
        dx[0] = x[1]
        dx[1] = μ*(1-x[0]**2)*x[1] - x[0]

        return dx 

    """
    The Jacobian matrix of the state evolution function F = \partial f / \partial x 
    This is a matrix of dimension (2,2)
    """
    def F_jacobian(self,x,μ):
        return np.array(([0.0,1.0],[-2.0*μ*x[0]*x[1]-1.0,μ*(1-x[0]**2)]))


    """
    The measurement function z = h(x)
    """
    def h(self,x):
        return x[0]**2 * x[1] + x[1]


    """
    The Jacobian matrix of the measurement function H = \partial h / \partial x 
    This is a matrix of dimension (2,1)
    """
    def H_jacobian(self,x):
        return np.ndarray((1,2),buffer=np.array([2*x[0]*x[1],x[0]**2 + 1])) #y,x #todo fix this to be general








