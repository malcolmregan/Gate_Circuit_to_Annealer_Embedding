



import errno
import logging
import os
import subprocess
import tempfile
import warnings

from PIL import Image

from converter.qiskit.dagcircuit import DAGCircuit
from converter.qiskit.tools.visualization import _error
from converter.qiskit.tools.visualization import _latex
from converter.qiskit.tools.visualization import _matplotlib
from converter.qiskit.tools.visualization import _text
from converter.qiskit.tools.visualization import _utils
from converter.qiskit.transpiler import transpile_dag



def plot_circuit(circuit,
                 basis="id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,"
                       "cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap",
                 scale=0.7,
                 style=None):
    pass


def circuit_drawer(circuit,
                   basis=None,
                   scale=0.7,
                   filename=None,
                   style=None,
                   output=None,
                   interactive=False,
                   line_length=None,
                   plot_barriers=True,
                   reverse_bits=False):
    pass











def qx_color_scheme():
    pass




def _text_circuit_drawer(circuit, filename=None,
                         basis="id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,"
                               "cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap", line_length=None,
                         reversebits=False, plotbarriers=True):
    pass




def latex_circuit_drawer(circuit,
                         basis="id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,"
                               "cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap",
                         scale=0.7,
                         filename=None,
                         style=None):
    pass






def _latex_circuit_drawer(circuit,
                          basis="id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,"
                                "cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap",
                          scale=0.7,
                          filename=None,
                          style=None,
                          plot_barriers=True,
                          reverse_bits=False):
    pass







def generate_latex_source(circuit, filename=None,
                          basis="id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,"
                                "cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap",
                          scale=0.7, style=None):
    pass




def _generate_latex_source(circuit, filename=None,
                           basis="id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,"
                                 "cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap",
                           scale=0.7, style=None, reverse_bits=False,
                           plot_barriers=True):
    pass





def matplotlib_circuit_drawer(circuit,
                              basis='id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,'
                                    'cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap',
                              scale=0.7,
                              filename=None,
                              style=None):
    pass




def _matplotlib_circuit_drawer(circuit,
                               basis='id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,'
                                     'ry,rz,cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,'
                                     'cswap',
                               scale=0.7,
                               filename=None,
                               style=None,
                               plot_barriers=True,
                               reverse_bits=False):
    pass



