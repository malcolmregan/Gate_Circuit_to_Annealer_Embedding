


from abc import abstractmethod
from collections.abc import Hashable
from inspect import signature


class MetaPass(type):
    pass

    def __call__(cls, *args, **kwargs):
        pass

    def _freeze_init_parameters(init_method, args, kwargs):
        pass


class BasePass(metaclass=MetaPass):
    pass

    def __init__(self):
        pass

    def normalize_parameters(cls, *args, **kwargs):
        pass


    def name(self):
        pass

    def run(self, dag):
        pass

    def is_transformation_pass(self):
        pass

    def is_analysis_pass(self):
        pass


class AnalysisPass(BasePass):  # pylint: disable=abstract-method
    pass


class TransformationPass(BasePass):  # pylint: disable=abstract-method
    pass
