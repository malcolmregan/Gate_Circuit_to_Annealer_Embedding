



from functools import reduce

import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from scipy import linalg

from converter.qiskit.quantum_info import pauli_group, Pauli
from converter.qiskit.tools.visualization import VisualizationError
from converter.qiskit.tools.visualization._bloch import Bloch


class Arrow3D(FancyArrowPatch):
    pass

    def __init__(self, xs, ys, zs, *args, **kwargs):
        pass

    def draw(self, renderer):
        pass


def plot_hinton(rho, title='', filename=None):
    pass







def plot_bloch_vector(bloch, title="", filename=None):
    pass




def plot_state_city(rho, title="", filename=None):
    pass












def plot_state_paulivec(rho, title="", filename=None):
    pass






def n_choose_k(n, k):
    pass




def lex_index(n, k, lst):
    pass





def bit_string_index(s):
    pass


def phase_to_color_wheel(complex_number):
    pass



def plot_state_qsphere(rho, filename=None):
    pass




def plot_state(quantum_state, method='city', filename=None):
    pass







def plot_wigner_function(state, res=100, filename=None):
    pass














def plot_wigner_curve(wigner_data, xaxis=None, filename=None):
    pass




def plot_wigner_plaquette(wigner_data, max_wigner='local', filename=None):
    pass









def plot_wigner_data(wigner_data, phis=None, method=None, filename=None):
    pass


