import os
import pkgutil
import __main__ as main

from . import _util

from ._qiskiterror import QISKitError
from ._classicalregister import ClassicalRegister
from ._quantumregister import QuantumRegister
from ._quantumcircuit import QuantumCircuit
from ._gate import Gate
from ._compositegate import CompositeGate
from ._instruction import Instruction
from ._instructionset import InstructionSet
from ._reset import Reset
from ._measure import Measure
from ._schema_validation import (validate_json_against_schema,SchemaValidationError)
from .result import Result
from ._pubsub import Publisher, Subscriber

import converter.qiskit .extensions.standard
import converter.qiskit .extensions.quantum_initializer

#from converter.qiskit.backends.ibmq import IBMQ
#from converter.qiskit.backends.aer import Aer  # pylint: disable=invalid-name

# to be placed *before* the wrapper imports or any non-import code.

from .wrapper._wrapper import (load_qasm_string, load_qasm_file, qobj_to_circuits)
from .tools._compiler import (compile, execute)

#import converter.qiskit wrapper, to make it available when doing "import qiskit".
from . import wrapper
from . import tools

