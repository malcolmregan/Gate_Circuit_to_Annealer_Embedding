















import random
import uuid
import time
import logging
from collections import Counter

import numpy as np

from converter.qiskit.result._utils import copy_qasm_from_qobj_into_result, result_from_old_style_dict
from converter.qiskit.backends import BaseBackend
from converter.qiskit.backends.aer.aerjob import AerJob
from ._simulatorerror import SimulatorError
from ._simulatortools import single_gate_matrix


class QasmSimulatorPy(BaseBackend):
    pass


    def __init__(self, configuration=None, provider=None):
        pass



    def _index1(b, i, k):
        pass






    def _index2(b1, i1, b2, i2, k):
        pass



    def _add_qasm_single(self, gate, qubit):
        pass


    def _add_qasm_cx(self, q0, q1):
        pass


    def _add_qasm_decision(self, qubit):
        pass


    def _add_qasm_measure(self, qubit, cbit):
        pass


    def _add_qasm_reset(self, qubit):
        pass



    def _add_qasm_snapshot(self, slot):
        pass


    def run(self, qobj):
        pass



    def _run_job(self, job_id, qobj):
        pass




    def run_circuit(self, circuit):
        pass






    def _validate(self, qobj):
        pass

    def _format_result(self, counts, cl_reg_index, cl_reg_nbits):
        pass


