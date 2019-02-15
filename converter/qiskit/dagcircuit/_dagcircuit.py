


from collections import OrderedDict
import copy
import itertools

import networkx as nx
import sympy

from converter.qiskit import QuantumRegister, ClassicalRegister
from converter.qiskit import QISKitError
from converter.qiskit import _compositegate
from ._dagcircuiterror import DAGCircuitError


class DAGCircuit:
    pass



    def __init__(self):
        pass













    def get_qubits(self):
        pass

    def rename_register(self, regname, newname):
        pass


    def remove_all_ops_named(self, opname):
        pass

    def fs(self, number):
        pass

    def add_qreg(self, qreg):
        pass

    def add_creg(self, creg):
        pass

    def _add_wire(self, name, isClassical=False):
        pass


    def add_basis_element(self, name, number_qubits,
                          number_classical=0, number_parameters=0):
        pass



    def add_gate_data(self, name, gatedata):
        pass


    def _check_basis_data(self, name, qargs, cargs, params):
        pass


    def _check_condition(self, name, condition):
        pass


    def _check_bits(self, args, amap, bval):
        pass


    def _bits_in_condition(self, cond):
        pass


    def _add_op_node(self, nname, nqargs, ncargs, nparams, ncondition, nop):
        pass


    def apply_operation_back(self, name, qargs, cargs=None, params=None,
                            condition=None, op=None):
        pass





    def apply_operation_front(self, name, qargs, cargs=None, params=None,
                             condition=None, op=None):
        pass





    def _make_union_basis(self, input_circuit):
        pass


    def _make_union_gates(self, input_circuit):
        pass



    def _check_wiremap_registers(self, wire_map, keyregs, valregs,
                                 valreg=True):
        pass



    def _check_wiremap_validity(self, wire_map, keymap, valmap, input_circuit):
        pass



    def _map_condition(self, wire_map, condition):
        pass


    def compose_back(self, input_circuit, wire_map=None):
        pass









    def compose_front(self, input_circuit, wire_map=None):
        pass









    def size(self):
        pass

    def depth(self):
        pass


    def width(self):
        pass

    def num_cbits(self):
        pass

    def num_tensor_factors(self):
        pass

    def _gate_string(self, name):
        pass

    def qasm(self, decls_only=False, add_swap=False,
            no_decls=False, qeflag=False, aliases=None, eval_symbols=False):
        pass









    def _check_wires_list(self, wires, name, input_circuit, condition=None):
        pass





    def _make_pred_succ_maps(self, n):
        pass


    def _full_pred_succ_maps(self, pred_map, succ_map, input_circuit,
                             wire_map):
        pass




    def node_nums_in_topological_order(self):
        pass

    def substitute_circuit_all(self, name, input_circuit, wires=None):
        pass







    def substitute_circuit_one(self, node, input_circuit, wires=None):
        pass











    def get_named_nodes(self, name):
        pass


    def _remove_op_node(self, n):
        pass


    def remove_ancestors_of(self, node):
        pass

    def remove_descendants_of(self, node):
        pass

    def remove_nonancestors_of(self, node):
        pass

    def remove_nondescendants_of(self, node):
        pass

    def layers(self):
        pass




        def nodes_data(nodes):
            pass








    def serial_layers(self):
        pass


    def multigraph_layers(self):
        pass



    def collect_runs(self, namelist):
        pass




    def count_ops(self):
        pass


    def property_summary(self):
        pass

    def fromQuantumCircuit(circuit, expand_gates=True):
        pass






