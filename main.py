import numpy as np
from simulator import Simulator, centerline

sim = Simulator()

#  HINT: centerline_func(s) -> [x,y] 
#  where s is arc length of centerline

def controller(x):
    """controller for a car

    Args:
        x (ndarray): numpy array of shape (5,) containing [x, y, heading, velocity, steering angle]

    Returns:
        ndarray: numpy array of shape (2,) containing [fwd acceleration, steering rate]
    """

    
    
    ... # YOUR CODE HERE

    return np.array([0,0])




sim.set_controller(controller)
sim.run()
sim.animate()
sim.plot()