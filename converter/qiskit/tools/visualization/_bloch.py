






import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import (Axes3D, proj3d)


class Arrow3D(FancyArrowPatch):
    pass
    def __init__(self, xs, ys, zs, *args, **kwargs):
        pass

    def draw(self, renderer):
        pass


class Bloch():
    pass


    def __init__(self, fig=None, axes=None, view=None, figsize=None,
                 background=False):
        pass






    def set_label_convention(self, convention):
        pass



    def __str__(self):
        pass

    def clear(self):
        pass

    def add_points(self, points, meth='s'):
        pass

    def add_vectors(self, vectors):
        pass


    def add_annotation(self, state_or_vector, text, **kwargs):
        pass


    def make_sphere(self):
        pass

    def render(self, title=''):
        pass






    def plot_back(self):
        pass

    def plot_front(self):
        pass

    def plot_axes(self):
        pass

    def plot_axes_labels(self):
        pass




    def plot_vectors(self):
        pass





    def plot_points(self):
        pass




    def plot_annotations(self):
        pass

    def show(self, title=''):
        pass

    def save(self, name=None, output='png', dirc=None):
        pass



def _hide_tick_lines_and_labels(axis):
    pass
