






import logging
import uuid

from converter.qiskit.backends.aer.aerjob import AerJob
from converter.qiskit.backends.aer._simulatorerror import SimulatorError
from converter.qiskit.qobj import QobjInstruction
from .qasm_simulator_py import QasmSimulatorPy



class StatevectorSimulatorPy(QasmSimulatorPy):
    pass


    def __init__(self, configuration=None, provider=None):
        pass

    def run(self, qobj):
        pass



    def _run_job(self, job_id, qobj):
        pass

    def _validate(self, qobj):
        pass

