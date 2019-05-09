import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

vec=np.loadtxt('datos.txt',usecols=0)

Z=np.zeros(shape=(401,201))

    
for i in range(401):
    Z[i,:]=vec[i*201:(i+1)*201]

U0=Z[0,:]
Uf=Z[-1,:]



X=np.array(range(201))/201
plt.plot(X, U0, label='tiempo inicial')
plt.plot(X, Uf, label='tiempo final')
plt.xlabel('Desplazamiento [metros]')
plt.ylabel('U')
plt.legend()
plt.grid()
plt.savefig('graficas.png')

