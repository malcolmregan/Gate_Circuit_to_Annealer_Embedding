

import os
import shutil
import tempfile

import ply.yacc as yacc
import sympy

from . import _node as node
from ._qasmerror import QasmError
from ._qasmlexer import QasmLexer


class QasmParser(object):
    pass


    def __init__(self, filename):
        pass

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

    def update_symtab(self, obj):
        pass


    def verify_declared_bit(self, obj):
        pass


    def verify_bit_list(self, obj):
        pass

    def verify_exp_list(self, obj):
        pass


    def verify_as_gate(self, obj, bitlist, arglist=None):
        pass



    def verify_reg(self, obj, object_type):
        pass




    def verify_reg_list(self, obj, object_type):
        pass

    def id_tuple_list(self, id_node):
        pass

    def verify_distinct(self, list_of_nodes):
        pass


    def pop_scope(self):
        pass

    def push_scope(self):
        pass


    def p_main(self, program):
        pass

    def p_program_0(self, program):
        pass

    def p_program_1(self, program):
        pass

    def p_statement(self, program):
        pass

    def p_format(self, program):
        pass

    def p_format_0(self, program):
        pass

    def p_id(self, program):
        pass

    def p_id_e(self, program):
        pass

    def p_indexed_id(self, program):
        pass

    def p_primary(self, program):
        pass

    def p_id_list_0(self, program):
        pass

    def p_id_list_1(self, program):
        pass

    def p_gate_id_list_0(self, program):
        pass

    def p_gate_id_list_1(self, program):
        pass

    def p_bit_list_0(self, program):
        pass

    def p_bit_list_1(self, program):
        pass

    def p_primary_list_0(self, program):
        pass

    def p_primary_list_1(self, program):
        pass

    def p_decl(self, program):
        pass

    def p_qreg_decl(self, program):
        pass

    def p_qreg_decl_e(self, program):
        pass

    def p_creg_decl(self, program):
        pass

    def p_creg_decl_e(self, program):
        pass

    def p_gate_decl_0(self, program):
        pass

    def p_gate_decl_1(self, program):
        pass

    def p_gate_decl_2(self, program):
        pass

    def p_gate_scope(self, program):
        pass

    def p_gate_body_0(self, program):
        pass

    def p_gate_body_1(self, program):
        pass

    def p_gate_op_list_0(self, program):
        pass

    def p_gate_op_list_1(self, program):
        pass

    def p_unitary_op_0(self, program):
        pass

    def p_unitary_op_1(self, program):
        pass

    def p_unitary_op_2(self, program):
        pass

    def p_unitary_op_3(self, program):
        pass

    def p_unitary_op_4(self, program):
        pass

    def p_gate_op_0(self, program):
        pass

    def p_gate_op_0e1(self, p):
        pass

    def p_gate_op_0e2(self, program):
        pass

    def p_gate_op_1(self, program):
        pass

    def p_gate_op_1e1(self, program):
        pass

    def p_gate_op_1e2(self, program):
        pass

    def p_gate_op_2(self, program):
        pass

    def p_gate_op_2e(self, program):
        pass

    def p_gate_op_3(self, program):
        pass

    def p_gate_op_4(self, program):
        pass

    def p_gate_op_4e0(self, program):
        pass

    def p_gate_op_4e1(self, program):
        pass

    def p_gate_op_5(self, program):
        pass

    def p_gate_op_5e(self, program):
        pass

    def p_opaque_0(self, program):
        pass

    def p_opaque_1(self, program):
        pass

    def p_opaque_2(self, program):
        pass

    def p_opaque_1e(self, program):
        pass

    def p_measure(self, program):
        pass

    def p_measure_e(self, program):
        pass

    def p_barrier(self, program):
        pass

    def p_reset(self, program):
        pass

    def p_if(self, program):
        pass



    def p_quantum_op(self, program):
        pass

    def p_unary_0(self, program):
        pass

    def p_unary_1(self, program):
        pass

    def p_unary_2(self, program):
        pass

    def p_unary_3(self, program):
        pass

    def p_unary_4(self, program):
        pass

    def p_unary_6(self, program):
        pass


    def p_expression_1(self, program):
        pass

    def p_expression_0(self, program):
        pass

    def p_expression_2(self, program):
        pass

    def p_exp_list_0(self, program):
        pass

    def p_exp_list_1(self, program):
        pass

    def p_ignore(self, program):
        pass

    def p_error(self, program):
        pass


    def find_column(self, input_, token):
        pass


    def get_tokens(self):
        pass



    def parse_debug(self, val):
        pass

    def parse(self, data):
        pass

    def print_tree(self):
        pass

    def run(self, data):
        pass

