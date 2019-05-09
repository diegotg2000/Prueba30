import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import imageio

vec=np.loadtxt('datos.txt',usecols=0)

Z=np.zeros(shape=(401,201))

    
for i in range(401):
    Z[i,:]=vec[i*201:(i+1)*201]


def plot_for_offset(i):
    # Data for plotting
    x = np.arange(201)/201
    s = Z[i]

    fig, ax = plt.subplots(figsize=(5,5))
    ax.plot(x, s)
    ax.grid()
    ax.set(xlabel='X', ylabel='U',
           title='Tiempo: '+'{0:.2f}'.format(2*i/401))

    # IMPORTANT ANIMATION CODE HERE
    # Used to keep the limits constant
    ax.set_ylim(-0.05, 0.05)

    # Used to return the plot as an image rray
    fig.canvas.draw()       # draw the canvas, cache the renderer
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    return image

kwargs_write = {'fps':20, 'quantizer':'nq'}
imageio.mimsave('./movie.gif', [plot_for_offset(i) for i in range(401)], fps=20)