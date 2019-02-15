


from ._transpilererror import TranspilerAccessError


class FencedObject():
    pass

    def __init__(self, instance, attributes_to_fence):
        pass

    def __getattribute__(self, name):
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def _check_if_fenced(self, name):
        pass




class FencedPropertySet(FencedObject):
    pass
    def __init__(self, property_set_instance):
        pass


class FencedDAGCircuit(FencedObject):
    pass
    def __init__(self, dag_circuit_instance):
        pass
