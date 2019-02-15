



from collections import OrderedDict
import logging

from converter.qiskit._qiskiterror import QISKitError
from converter.qiskit.backends import BaseProvider
from converter.qiskit.backends.providerutils import resolve_backend_name, filter_backends

from .qasm_simulator import CliffordSimulator, QasmSimulator
from .qasm_simulator_py import QasmSimulatorPy
from .statevector_simulator import StatevectorSimulator
from .statevector_simulator_py import StatevectorSimulatorPy
from .unitary_simulator import UnitarySimulator





class AerProvider(BaseProvider):
    pass

    def __init__(self, *args, **kwargs):
        pass


    def get_backend(self, name=None, **kwargs):
        pass



    def backends(self, name=None, filters=None, **kwargs):
        pass



    def grouped_backend_names():
        pass

    def deprecated_backend_names():
        pass

    def _verify_aer_backends(self):
        pass


    def _get_backend_instance(self, backend_cls):
        pass




    def __str__(self):
        pass
