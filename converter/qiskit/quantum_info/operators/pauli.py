



import warnings

import numpy as np
from scipy import sparse

from converter.qiskit import QISKitError


def _make_np_bool(arr):
    pass



class Pauli:
    pass






    def __init__(self, z=None, x=None, label=None):
        pass




    def from_label(cls, label):
        pass





    def _init_from_bool(self, z, x):
        pass






    def __len__(self):
        pass

    def __repr__(self):
        pass


    def __str__(self):
        pass

    def __eq__(self, other):
        pass



    def __mul__(self, other):
        pass



    def __imul__(self, other):
        pass



    def __hash__(self):
        pass

    def v(self):
        pass

    def w(self):
        pass

    def z(self):
        pass

    def x(self):
        pass

    def sgn_prod(p1, p2):
        pass




    def numberofqubits(self):
        pass

    def to_label(self):
        pass



    def to_matrix(self):
        pass



    def to_spmatrix(self):
        pass




    def update_z(self, z, indices=None):
        pass





    def update_x(self, x, indices=None):
        pass





    def insert_paulis(self, indices=None, paulis=None, pauli_labels=None):
        pass








    def append_paulis(self, paulis=None, pauli_labels=None):
        pass



    def delete_qubits(self, indices):
        pass





    def random(cls, num_qubits):
        pass



    def pauli_single(cls, num_qubits, index, pauli_label):
        pass





    def kron(self, other):
        pass




    def _prod_phase(p1, p2):
        pass



def pauli_group(number_of_qubits, case='weight'):
    pass






