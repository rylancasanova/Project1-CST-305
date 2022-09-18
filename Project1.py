# Zach Pedersen and Rylan Casanova
# Project 1: Visualizing ODE with SciPy

# Importing required extensions
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
# import warnings
np.warnings.filterwarnings("ignore")

# define the model
def model(x, t, k):  # Initial function to return dx/dt
   dxdt: Any = k / t
   return dxdt

# Set Parameters
x0 = 9
t = np.linspace(1, 40)
# Solves the ODE
k = 9
x1 = odeint(model, x0, t, args=(k,))
k = 18
x2 = odeint(model, x0, t, args=(k,))
k = 27
x3 = odeint(model, x0, t, args=(k,))
k = 36
x4 = odeint(model, x0, t, args=(k,))
# Plots results
plt.plot(t, x1, 'r', linewidth=2, label='k=9')
plt.plot(t, x2, 'g', linewidth=2, label='k=18')
plt.plot(t, x3, 'r--', linewidth=2, label='k=27')
plt.plot(t, x4, 'g--', linewidth=2, label='k=36')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.legend()
plt.show()
