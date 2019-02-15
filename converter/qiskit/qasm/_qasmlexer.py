



import os

import ply.lex as lex
from sympy import Number

from . import _node as node
from ._qasmerror import QasmError



class QasmLexer(object):
    pass


    def __mklexer__(self, filename):
        pass


    def __init__(self, filename):
        pass

    def input(self, data):
        pass

    def token(self):
        pass

    def pop(self):
        pass

    def push(self, filename):
        pass


    def t_REAL(self, t):
        pass

    def t_NNINTEGER(self, t):
        pass

    def t_ASSIGN(self, t):
        pass

    def t_MATCHES(self, t):
        pass

    def t_STRING(self, t):
        pass

    def t_INCLUDE(self, t):
        pass




    def t_FORMAT(self, t):
        pass

    def t_COMMENT(self, t):
        pass

    def t_CX(self, t):
        pass

    def t_U(self, t):
        pass

    def t_ID(self, t):
        pass


    def t_newline(self, t):
        pass

    def t_eof(self, t):
        pass


    def t_error(self, t):
        pass
