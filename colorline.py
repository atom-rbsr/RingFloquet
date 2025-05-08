# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:07:52 2017

@author: Dai
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as mcoll

def make_segments(x, y):
    """
    Create list of line segments from x and y coordinates, in the correct format
    for LineCollection: an array of the form numlines x (points per line) x 2 (x
    and y) array
    """

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    return segments

def colorline(x, y, c=None, 
              cmap='Blues', ax=plt.gca(),
              norm=plt.Normalize(0.0, 1.0),
              linewidth=1.0, alpha=1.0):
    """
    http://nbviewer.ipython.org/github/dpsanders/matplotlib-examples/blob/master/colorline.ipynb
    http://matplotlib.org/examples/pylab_examples/multicolored_line.html
    Plot a colored line with coordinates x and y
    Optionally specify colors in the array c
    Optionally specify a colormap, a norm function and a line width
    """

    # Default colors equally spaced on [0,1]:
    if c is None:
        c = np.linspace(0.0, 1.0, 1*len(x))

    # Special case if a single number:
    # to check for numerical input -- this is a hack
    if not hasattr(c, "__iter__"):
        c = np.array([c])

    c = np.asarray(c)

    segments = make_segments(x, y)
    lc = mcoll.LineCollection(segments, array=c, cmap=cmap,
                              norm=norm,
                              linewidth=linewidth,
                              alpha=alpha)  
    ax.add_collection(lc)

    return lc