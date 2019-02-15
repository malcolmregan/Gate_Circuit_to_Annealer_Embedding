




import math
import warnings

import numpy as np
import scipy.linalg as la
from scipy.stats import unitary_group


from converter.qiskit import QISKitError
from converter.qiskit.quantum_info import pauli_group
from converter.qiskit.quantum_info import state_fidelity as new_state_fidelity




def qft(circ, q, n):
    pass




def partial_trace(state, trace_systems, dimensions=None, reverse=True):
    pass








def __partial_trace_vec(vec, trace_systems, dimensions, reverse=True):
    pass







def __partial_trace_mat(mat, trace_systems, dimensions, reverse=True):
    pass







def vectorize(density_matrix, method='col'):
    pass




def devectorize(vectorized_mat, method='col'):
    pass





def choi_to_rauli(choi, order=1):
    pass






def chop(array, epsilon=1e-10):
    pass





def outer(vector1, vector2=None):
    pass







def random_unitary_matrix(length):
    pass



def random_density_matrix(length, rank=None, method='Hilbert-Schmidt'):
    pass




def __ginibre_matrix(nrow, ncol=None):
    pass




def __random_density_hs(N, rank=None):
    pass



def __random_density_bures(N, rank=None):
    pass





def state_fidelity(state1, state2):
    pass





def purity(state):
    pass



def concurrence(state):
    pass




def shannon_entropy(pvec, base=2):
    pass



        def logfn(x):
            pass
        def logfn(x):
            pass
        def logfn(x):
            pass



def entropy(state):
    pass





def mutual_information(state, d0, d1=None):
    pass




def entanglement_of_formation(state, d0, d1=None):
    pass







def __eof_qubit(rho):
    pass






def is_pos_def(x):
    pass
