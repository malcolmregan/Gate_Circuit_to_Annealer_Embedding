


from types import SimpleNamespace

import numpy

from ._validation import QobjValidationError
from ._utils import QobjType



class QobjItem(SimpleNamespace):
    pass


    def as_dict(self):
        pass

    def _expand_item(cls, obj):
        pass

    def from_dict(cls, obj):
        pass




    def _qobjectify_item(cls, obj):
        pass

    def __reduce__(self):
        pass


class Qobj(QobjItem):
    pass



    def __init__(self, qobj_id, config, experiments, header, **kwargs):
        pass




class QobjConfig(QobjItem):
    pass



    def __init__(self, shots, memory_slots, **kwargs):
        pass



class QobjHeader(QobjItem):
    pass



class QobjExperiment(QobjItem):
    pass



    def __init__(self, instructions, **kwargs):
        pass



class QobjExperimentHeader(QobjItem):
    pass



class QobjInstruction(QobjItem):
    pass


    def __init__(self, name, **kwargs):
        pass

