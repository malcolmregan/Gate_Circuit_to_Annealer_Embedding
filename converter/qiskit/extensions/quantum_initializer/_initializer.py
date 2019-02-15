


import math
import numpy as np
import scipy

from converter.qiskit import CompositeGate
from converter.qiskit import Gate
from converter.qiskit import QISKitError
from converter.qiskit import QuantumCircuit
from converter.qiskit.extensions.standard.cx import CnotGate
from converter.qiskit.extensions.standard.ry import RYGate
from converter.qiskit.extensions.standard.rz import RZGate



class InitializeGate(CompositeGate):
    pass





    def __init__(self, param, qargs, circ=None):
        pass







    def nth_qubit_from_least_sig_qubit(self, nth):
        pass

    def reapply(self, circ):
        pass

    def gates_to_uncompute(self):
        pass



    def _rotations_to_disentangle(local_param):
        pass







    def _bloch_angles(pair_of_complex):
        pass


    def _multiplex(self, bottom_gate, bottom_qubit_index, list_of_angles):
        pass










    def chop_num(numb):
        pass




def reverse(self):
    pass






def optimize_gates(self):
    pass




def remove_zero_rotations(self):
    pass






def number_atomic_gates(self):
    pass




def remove_double_cnots_once(self):
    pass











def first_atomic_gate_host(self):
    pass





def last_atomic_gate_host(self):
    pass





def initialize(self, params, qubits):
    pass



