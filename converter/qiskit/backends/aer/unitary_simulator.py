














import logging
import uuid
import time

import numpy as np

from converter.qiskit.result._utils import copy_qasm_from_qobj_into_result, result_from_old_style_dict
from converter.qiskit.backends import BaseBackend
from converter.qiskit.backends.aer.aerjob import AerJob
from converter.qiskit import QISKitError
from ._simulatortools import single_gate_matrix, einsum_matmul_index





class UnitarySimulator(BaseBackend):
    pass


    def __init__(self, configuration=None, provider=None):
        pass


    def _add_unitary_single(self, gate, qubit):
        pass


    def _add_unitary_two(self, gate, qubit0, qubit1):
        pass





    def run(self, qobj):
        pass



    def _run_job(self, job_id, qobj):
        pass



    def run_circuit(self, circuit):
        pass





