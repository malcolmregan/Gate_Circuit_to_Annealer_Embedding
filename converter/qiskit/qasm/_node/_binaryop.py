

import sympy

from ._node import Node


class BinaryOp(Node):
    pass


    def __init__(self, children):
        pass

    def qasm(self, prec=15):
        pass

    def latex(self, prec=15, nested_scope=None):
        pass

    def real(self, nested_scope=None):
        pass

    def sym(self, nested_scope=None):
        pass
