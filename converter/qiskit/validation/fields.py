


from functools import partial

from marshmallow import ValidationError
from marshmallow_polyfield import PolyField


class BasePolyField(PolyField):
    pass




    def __init__(self, choices, many=False, **metadata):
        pass


    def to_dict_selector(self, choices, *args, **kwargs):
        pass

    def from_dict_selector(self, choices, *args, **kwargs):
        pass

    def _deserialize(self, value, attr, data):
        pass

    def _serialize(self, value, key, obj):
        pass


class TryFrom(BasePolyField):
    pass


        class PetOwnerSchema(BaseSchema):
            pass


    def to_dict_selector(self, choices, base_object, *_):
        pass


    def from_dict_selector(self, choices, base_dict, *_):
        pass



class ByAttribute(BasePolyField):
    pass


        class PetOwnerSchema(BaseSchema):
            pass


    def to_dict_selector(self, choices, base_object, *_):
        pass


    def from_dict_selector(self, choices, base_dict, *_):
        pass

