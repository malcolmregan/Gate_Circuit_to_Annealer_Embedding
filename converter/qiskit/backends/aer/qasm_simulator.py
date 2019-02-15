



import uuid
import json
import logging
import os
import subprocess
from subprocess import PIPE
import platform

import numpy as np

from converter.qiskit.result._utils import copy_qasm_from_qobj_into_result, result_from_old_style_dict
from converter.qiskit.backends import BaseBackend
from converter.qiskit.backends.aer.aerjob import AerJob
from converter.qiskit.qobj import Qobj
from converter.qiskit.qobj import qobj_to_dict





class QasmSimulator(BaseBackend):
    pass


    def __init__(self, configuration=None, provider=None):
        pass



    def run(self, qobj):
        pass

    def _run_job(self, job_id, qobj):
        pass


    def _validate(self, qobj):
        pass


class CliffordSimulator(BaseBackend):
    pass


    def __init__(self, configuration=None, provider=None):
        pass



    def run(self, qobj):
        pass



    def _run_job(self, job_id, qobj):
        pass



    def _validate(self):
        pass


class QASMSimulatorEncoder(json.JSONEncoder):
    pass



    def default(self, obj):
        pass


class QASMSimulatorDecoder(json.JSONDecoder):
    pass

    def __init__(self, *args, **kwargs):
        pass

    def object_hook(self, obj):
        pass



def run(qobj, executable):
    pass





def cx_error_matrix(cal_error, zz_error):
    pass











def x90_error_matrix(cal_error, detuning_error):
    pass









def _generate_coherent_error_matrix(config):
    pass



