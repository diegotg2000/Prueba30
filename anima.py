import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import imageio

vec=np.loadtxt('datos.txt',usecols=0)

Z=np.zeros(shape=(201,101))

    
for i in range(201):
    Z[i,:]=vec[i*101:(i+1)*101]


def plot_for_offset(i):
    # Data for plotting
    x = np.arange(101)/101
    s = Z[i]

    fig, ax = plt.subplots(figsize=(5,5))
    ax.plot(x, s)
    ax.grid()
    ax.set(xlabel='X', ylabel='U',
           title='Tiempo: '+'{0:.2f}'.format(2*i/201))

    # IMPORTANT ANIMATION CODE HERE
    # Used to keep the limits constant
    ax.set_ylim(-0.05, 0.05)

    # Used to return the plot as an image rray
    fig.canvas.draw()       # draw the canvas, cache the renderer
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    return image

kwargs_write = {'fps':20, 'quantizer':'nq'}
imageio.mimsave('./powers.gif', [plot_for_offset(i) for i in range(201)], fps=20)