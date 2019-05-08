import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

vec=np.loadtxt('datos.txt',usecols=0)

Z=np.zeros(shape=(201,101))

    
for i in range(201):
    Z[i,:]=vec[i*101:(i+1)*101]

U0=Z[0,:]
U1=Z[60,:]
U2=Z[140,:]
Uf=Z[-1,:]



X=np.array(range(101))/101
plt.plot(X, U0, label='tiempo inicial')
plt.plot(X, U1, label='tiempo 1')
plt.plot(X, U2, label='tiempo 2')
plt.plot(X, Uf, label='tiempo final')
plt.xlabel('Desplazamiento [metros]')
plt.ylabel('U')
plt.legend()
plt.savefig('graficas.png')

