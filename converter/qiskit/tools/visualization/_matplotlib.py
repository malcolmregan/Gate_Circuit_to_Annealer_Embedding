



import collections
import fractions
import itertools
import json
import logging
import math

import numpy as np
from matplotlib import patches
from matplotlib import pyplot as plt

from converter.qiskit import dagcircuit
from converter.qiskit import transpiler
from converter.qiskit.tools.visualization import _error
from converter.qiskit.tools.visualization import _qcstyle






class Anchor:
    pass
    def __init__(self, reg_num, yind, fold):
        pass

    def plot_coord(self, index, gate_width):
        pass


    def is_locatable(self, index, gate_width):
        pass

    def set_index(self, index, gate_width):
        pass

    def get_index(self):
        pass


class MatplotlibDrawer:
    pass
    def __init__(self,
                 basis='id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,'
                       'cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap',
                 scale=1.0, style=None, plot_barriers=True,
                 reverse_bits=False):
        pass




    def parse_circuit(self, circuit):
        pass

    def _registers(self):
        pass

    def ast(self):
        pass

    def _gate(self, xy, fc=None, wide=False, text=None, subtext=None):
        pass




    def _subtext(self, xy, text):
        pass


    def _line(self, xy0, xy1, lc=None, ls=None):
        pass

    def _measure(self, qxy, cxy, cid):
        pass


    def _conds(self, xy, istrue=False):
        pass



    def _ctrl_qubit(self, xy):
        pass


    def _tgt_qubit(self, xy):
        pass


    def _swap(self, xy):
        pass


    def _barrier(self, config, anc):
        pass


    def _linefeed_mark(self, xy):
        pass


    def draw(self, filename=None, verbose=False):
        pass

    def _draw_regs(self):
        pass

    def _reverse_bits(self, target_dict):
        pass

    def _draw_regs_sub(self, n_fold, feedline_l=False, feedline_r=False):
        pass


    def _draw_ops(self, verbose=False):
        pass




    def param_parse(v, pimode=False):
        pass

    def format_pi(val):
        pass

    def format_numeric(val, tol=1e-5):
        pass

    def fraction(val, base=np.pi, n=100, tol=1e-5):
        pass
