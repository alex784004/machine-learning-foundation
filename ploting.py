import numpy as np
import matplotlib.pyplot as plt
plt.figure(1)
x=np.arange(0,10.1,0.1)
y=x*x
plt.plot(x,y)
plt.show()

z=np.arange(-10,10.1,0.2)
y=(x-z)*(x-z)*(x-z)
plt.plot(x,y,z)
plt.show()
