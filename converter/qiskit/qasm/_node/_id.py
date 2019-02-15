

from ._node import Node
from ._nodeexception import NodeException


class Id(Node):
    pass


    def __init__(self, id, line, file):
        pass

    def to_string(self, indent):
        pass

    def qasm(self, prec=15):
        pass

    def latex(self, prec=15, nested_scope=None):
        pass

    def sym(self, nested_scope=None):
        pass

    def real(self, nested_scope=None):
        pass
