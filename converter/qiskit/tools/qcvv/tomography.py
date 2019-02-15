







import logging
from functools import reduce
from itertools import product
from re import match

import numpy as np

from converter.qiskit import QuantumCircuit
from converter.qiskit import QISKitError
from converter.qiskit.tools.qi.qi import vectorize, devectorize, outer




class TomographyBasis(dict):
    pass


            def BX_prep_fun(circuit, qreg, op):
                pass
            def BX_prep_fun(circuit, qreg, op):
                pass



    def prep_gate(self, circuit, qreg, op):
        pass


    def meas_gate(self, circuit, qreg, op):
        pass



def tomography_basis(basis, prep_fun=None, meas_fun=None):
    pass







def __pauli_prep_gates(circuit, qreg, op):
    pass



def __pauli_meas_gates(circuit, qreg, op):
    pass






def __sic_prep_gates(circuit, qreg, op):
    pass








def tomography_set(qubits,
    pass













def state_tomography_set(qubits, meas_basis='Pauli'):
    pass







def process_tomography_set(qubits, meas_basis='Pauli', prep_basis='SIC'):
    pass






def tomography_circuit_names(tomo_set, name=''):
    pass







def create_tomography_circuits(circuit, qreg, creg, tomoset):
    pass













def tomography_data(results, name, tomoset):
    pass






def marginal_counts(counts, meas_qubits):
    pass









def count_keys(n):
    pass






def fit_tomography_data(tomo_data, method='wizard', options=None):
    pass







def __get_option(opt, options):
    pass




def __leastsq_fit(tomo_data, weights=None, trace=None, beta=None):
    pass









def __projector(op_list, basis):
    pass


def __tomo_linear_inv(freqs, ops, weights=None, trace=None):
    pass









def __wizard(rho, epsilon=None):
    pass







def build_wigner_circuits(circuit, phis, thetas, qubits,
    pass







def wigner_data(q_result, meas_qubits, labels, shots=None):
    pass









