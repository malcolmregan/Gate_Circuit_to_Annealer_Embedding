

from functools import partial
from collections import OrderedDict
from converter.qiskit.dagcircuit import DAGCircuit
from ._propertyset import PropertySet
from ._basepasses import BasePass
from ._fencedobjs import FencedPropertySet, FencedDAGCircuit
from ._transpilererror import TranspilerError


class PassManager():
    pass

    def __init__(self, ignore_requires=None, ignore_preserves=None, max_iteration=None):
        pass





    def _join_options(self, passset_options):
        pass


    def add_passes(self, passes, ignore_requires=None, ignore_preserves=None, max_iteration=None,
                    **flow_controller_conditions):
        pass







    def run_passes(self, dag):
        pass



    def _do_pass(self, pass_, dag, options):
        pass






    def _update_valid_passes(self, pass_, ignore_preserves):
        pass


class FlowController():
    pass


    def __init__(self, passes, options, **partial_controller):
        pass

    def __iter__(self):
        pass

    def add_flow_controller(cls, name, controller):
        pass

    def remove_flow_controller(cls, name):
        pass

    def controller_factory(cls, passes, options, **partial_controller):
        pass





class FlowControllerLinear(FlowController):
    pass

    def __init__(self, passes, options):  # pylint: disable=super-init-not-called
        pass


class DoWhileController(FlowController):
    pass

    def __init__(self, passes, options, do_while=None,
                **partial_controller):
        pass

    def __iter__(self):
        pass




class ConditionalController(FlowController):
    pass

    def __init__(self, passes, options, condition=None,
                **partial_controller):
        pass

    def __iter__(self):
        pass


