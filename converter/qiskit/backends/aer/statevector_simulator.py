



import logging
import uuid

from converter.qiskit.qobj import QobjInstruction
from .qasm_simulator import QasmSimulator
from ._simulatorerror import SimulatorError
from .aerjob import AerJob



class StatevectorSimulator(QasmSimulator):
    pass


    def __init__(self, configuration=None, provider=None):
        pass

    def run(self, qobj):
        pass

    def _run_job(self, job_id, qobj):
        pass

    def _validate(self, qobj):
        pass

