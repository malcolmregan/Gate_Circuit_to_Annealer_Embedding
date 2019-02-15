


from converter.qiskit import Gate
from converter.qiskit import InstructionSet
from converter.qiskit import QuantumCircuit
from converter.qiskit import QuantumRegister
from converter.qiskit.extensions.standard import header  # pylint: disable=unused-import


class SGate(Gate):
    pass

    def __init__(self, qubit, circ=None):
        pass

    def reapply(self, circ):
        pass

    def inverse(self):
        pass


class SdgGate(Gate):
    pass

    def __init__(self, qubit, circ=None):
        pass

    def reapply(self, circ):
        pass

    def inverse(self):
        pass


def s(self, q):
    pass



def sdg(self, q):
    pass



