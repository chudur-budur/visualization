"""scatter.py -- A customized scatter plotting module. 

    This module provides a customized scatter plotting functions for
    high-dimensional Pareto-optimal fronts. It also provides different
    relevant parameters, tools and utilities.

    Copyright (C) 2016
    Computational Optimization and Innovation (COIN) Laboratory
    Department of Computer Science and Engineering
    Michigan State University
    428 S. Shaw Lane, Engineering Building
    East Lansing, MI 48824-1226, USA

.. moduleauthor:: AKM Khaled Talukder <talukde1@msu.edu>

"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mc


__all__ = ["plot", "camera_angles"]


# Some good camera angles for scatter plots.
camera_angles = {
    'dtlz2': {'3d': (60,20), '4d':(-60,30), '8d': (22,21)}, \
    'dtlz2-nbi': {'3d': (60,20), '4d':(-60,30), '8d': (-60,30)}, \
    'debmdk': {'3d': (-30,15), '4d': (-20,32), '8d': (-60,30)}, \
    'debmdk-nbi': {'3d': (-60,30), '4d': (-60,30), '8d': (-60,30)}, \
    'debmdk-all': {'3d': (-60,30), '4d': (-60,30), '8d': (-60,30)}, \
    'debmdk-all-nbi': {'3d': (-60,30), '4d': (-60,30), '8d': (-60,30)}, \
    'dtlz8': {'3d': (-60,30), '4d': (-60,30), '6d': (-60,30), '8d': (-60,30)}, \
    'dtlz8-nbi': {'3d': (-60,30), '4d': (-60,30), '6d': (-60,30), '8d': (-60,30)}, \
    'c2dtlz2': {'3d': (45,15), '4d': (-20,40), '5d': (-25,30), '8d': (-25,30)}, \
    'c2dtlz2-nbi': {'3d': (45,15), '4d': (-20,40), '5d': (-25,30), '8d': (-25,30)}, \
    'cdebmdk': {'3d': (20,15), '4d': (-60,30), '8d': (-60,30)}, \
    'cdebmdk-nbi': {'3d': (20,15), '4d': (-60,30), '8d': (-60,30)}, \
    'c0dtlz2': {'3d': (20,25), '4d': (-60,30), '8d': (-60,30)}, \
    'c0dtlz2-nbi': {'3d': (20,25), '4d': (-60,30), '8d': (-60,30)}, \
    'crash-nbi': {'3d': (30,25)}, 'crash-c1-nbi': {'3d': (30,25)}, 'crash-c2-nbi': {'3d': (30,25)}, \
    'gaa': {'10d': (-60,30)}, \
    'gaa-nbi': {'10d': (-60,30)}
}


def plot(A, plt, s=1, c=mc.TABLEAU_COLORS['tab:blue'], **kwargs):
    r"""A scatter plot function.

    This uses `matplotlib.axes.Axes.scatter` function to do a scatter plot.

    Parameters
    ----------
    A : ndarray 
        `n` number of `m` dim. points to be plotted.
    plt : A `matplotlib.pyplot` object
        It needs to be passed.
    s : int or 1-D array_like, optional
        Point size, or an array of point sizes. Default 1 when optional.
    c : A `matplotlib.colors` object, str or an array RGBA color values.
        Colors to be used. Default `mc.TABLEAU_COLORS['tab:blue']` when optional.

    Other Parameters
    ----------------
    label_prefix : str, optional
        The axis-label-prefix to be used, default `r"$f_{:d}$"` when optional.
    label_fontsize : str or int, optional
        The fontsize for the axes labels. Default `'large'` when optional.
    axes : tuple of int, optional
        The list of columns of `A` to be plotted. Default `(0, 1, 2)` when optional.
    euler : tuple (i.e. a pair) of int, optional
        The azmiuth and elevation angle. Default `(-60,30)` when optional.
    xbound : tuple (i.e. a pair) of int, optional 
        The bounds on the X-axis. Default `None` when optional.
    ybound : tuple (i.e. a pair) of int, optional 
        The bounds on the Y-axis. Default `None` when optional.
    zbound : tuple (i.e. a pair) of int, optional 
        The bounds on the Z-axis. Default `None` when optional.
    title : str, optional
        The plot title. Default `None` when optional.

    Returns
    -------
    (fig, ax) : tuple of `matplotlib.pyplot.figure` and `matplotlib.axes.Axes`
        A tuple of `matplotlib.pyplot.figure` and `matplotlib.axes.Axes` 
        (or `mpl_toolkits.mplot3d.axes.Axes`) objects.
    """
    # all other parameters
    # by default label_prefix is $f_n$
    label_prefix = kwargs['label_prefix'] if (kwargs is not None and 'label_prefix' in kwargs) \
                            else r"$f_{:d}$"
    # default label font size is 'large'
    label_fontsize = kwargs['label_fontsize'] if (kwargs is not None and 'label_fontsize' in kwargs) \
                            else 'large'
    # plot first 3 axes by default
    axes = kwargs['axes'] if (kwargs is not None and 'axes' in kwargs) else (0, 1, 2)
    # azimuth is -60 and elevation is 30 by default
    euler = kwargs['euler'] if (kwargs is not None and 'euler' in kwargs) else (-60, 30)
    # by default, take the entire range
    xbound = kwargs['xbound'] if (kwargs is not None and 'xbound' in kwargs) else None
    ybound = kwargs['ybound'] if (kwargs is not None and 'ybound' in kwargs) else None
    zbound = kwargs['zbound'] if (kwargs is not None and 'zbound' in kwargs) else None
    # by default, no title
    title = kwargs['title'] if (kwargs is not None and 'title' in kwargs) else None

    if plt is not None:
        fig = plt.figure()
        if title is not None:
            fig.suptitle(title)
        if A.shape[1] < 3:
            ax = fig.gca()
            ax.scatter(A[:,axes[0]], A[:,axes[1]], s = s, c = c)
            ax.set_xbound(ax.get_xbound() if xbound is None else xbound)
            ax.set_ybound(ax.get_ybound() if ybound is None else ybound)
            ax.set_xlabel(label_prefix.format(axes[0] + 1), fontsize=label_fontsize)
            ax.set_ylabel(label_prefix.format(axes[1] + 1), fontsize=label_fontsize)
        else:
            ax = Axes3D(fig)
            ax.scatter(A[:,axes[0]], A[:,axes[1]], A[:,axes[2]], s=s, c=c) 
            ax.set_xbound(ax.get_xbound() if xbound is None else xbound)
            ax.set_ybound(ax.get_ybound() if ybound is None else ybound)
            ax.set_zbound(ax.get_zbound() if zbound is None else zbound)
            ax.set_xlabel(label_prefix.format(axes[0] + 1), fontsize=label_fontsize)
            ax.set_ylabel(label_prefix.format(axes[1] + 1), fontsize=label_fontsize)
            ax.set_zlabel(label_prefix.format(axes[2] + 1), fontsize=label_fontsize)
            ax.xaxis.set_rotate_label(False)
            ax.yaxis.set_rotate_label(False)
            ax.zaxis.set_rotate_label(False)
            ax.view_init(euler[1], euler[0])
        return (fig, ax)
    else:
        raise TypeError("A valid `matplotlib.pyplot` object must be provided.")