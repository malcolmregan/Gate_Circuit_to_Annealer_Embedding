

import logging
import numpy as np
import scipy.sparse as sp
import scipy.sparse.csgraph as cs

from converter.qiskit.transpiler._transpilererror import TranspilerError
from converter.qiskit._qiskiterror import QISKitError
from converter.qiskit.dagcircuit import DAGCircuit
from converter.qiskit import _quantumcircuit
from converter.qiskit.unrollers import _dagunroller
from converter.qiskit.unrollers import _dagbackend
from converter.qiskit.unrollers import _jsonbackend
from converter.qiskit.mapper import (Coupling, optimize_1q_gates, coupling_list2dict, swap_mapper,
                                     cx_cancellation, direction_mapper,
                                     remove_last_measurements, return_last_measurements)
from converter.qiskit._pubsub import Publisher, Subscriber
from ._parallel import parallel_map




def transpile(circuits, backend, basis_gates=None, coupling_map=None, initial_layout=None,
              seed_mapper=None, hpc=None, pass_manager=None):
    pass












def _circuits_2_dags(circuits):
    pass




def _dags_2_dags(dags, basis_gates='u1,u2,u3,cx,id', coupling_map=None,
                 initial_layouts=None, seed_mapper=None, pass_manager=None):
    pass





    def _emmit_start(num_dags):
        pass

    def _emmit_done(progress):
        pass

    def _emmit_finish():
        pass



def _transpile_dags_parallel(dag_layout_tuple, basis_gates='u1,u2,u3,cx,id',
                            coupling_map=None, seed_mapper=None, pass_manager=None):
    pass



def transpile_dag(dag, basis_gates='u1,u2,u3,cx,id', coupling_map=None,
                 initial_layout=None, get_layout=False,
                 format='dag', seed_mapper=None, pass_manager=None):
    pass














def _best_subset(backend, n_qubits):
    pass









def _matches_coupling_map(dag, coupling_map):
    pass




def _pick_best_layout(dag, backend):
    pass



