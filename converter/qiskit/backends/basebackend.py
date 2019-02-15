


import warnings
from abc import ABC, abstractmethod

from converter.qiskit._qiskiterror import QISKitError
import converter.qiskit 


class BaseBackend(ABC):
    pass

    def __init__(self, configuration, provider=None):
        pass




    def run(self, qobj):
        pass

    def configuration(self):
        pass

    def calibration(self):
        pass

    def parameters(self):
        pass

    def properties(self):
        pass

    def status(self):
        pass

    def name(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


