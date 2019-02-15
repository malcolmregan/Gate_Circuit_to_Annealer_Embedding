

from converter.qiskit._quantumregister import QuantumRegister
from converter.qiskit._classicalregister import ClassicalRegister
from ._unrollererror import UnrollerError


class Unroller(object):
    pass

    def __init__(self, ast, backend=None, precision=15, filename=None):
        pass

    def _process_bit_id(self, node):
        pass


    def _process_custom_unitary(self, node):
        pass

    def _process_gate(self, node, opaque=False):
        pass


    def _process_cnot(self, node):
        pass

    def _process_measure(self, node):
        pass

    def _process_if(self, node):
        pass

    def _process_children(self, node):
        pass

    def _process_node(self, node):
        pass
























    def set_backend(self, backend):
        pass

    def execute(self):
        pass
