


import networkx as nx

from converter.qiskit.unrollers._unroller import Unroller
from converter.qiskit.qasm._node import Real, Id, IdList, ExpressionList, Gate, \
                                        PrimaryList, Int, IndexedId, Qreg, If, Creg, \
                                        Program, CustomUnitary
from ._unrollererror import UnrollerError
from ._dagbackend import DAGBackend


class DagUnroller(object):
    pass
    def __init__(self, dag_circuit, backend=None):
        pass


    def set_backend(self, backend):
        pass

    def execute(self):
        pass

    def expand_gates(self, basis=None):
        pass






    def _build_subcircuit(self, gatedefs, basis, gate_name, gate_params, gate_args,
                         gate_condition):
        pass





    def _process(self):
        pass



