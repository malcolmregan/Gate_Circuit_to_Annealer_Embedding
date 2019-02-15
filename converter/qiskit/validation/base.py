




    class PersonSchema(BaseSchema):
        pass

    class Person(BaseModel):
        pass

from functools import partial, wraps
from types import SimpleNamespace

from marshmallow import ValidationError
from marshmallow import Schema, post_dump, post_load, fields
from marshmallow.utils import is_collection

from .fields import BasePolyField


class BaseSchema(Schema):
    pass





    def dump_additional_data(self, valid_data, original_data):
        pass





    def load_additional_data(self, valid_data, original_data):
        pass





    def make_model(self, data):
        pass


class _SchemaBinder:
    pass

    def __init__(self, schema_cls):
        pass

    def __call__(self, model_cls):
        pass






    def _create_shallow_schema(self, schema_cls):
        pass





    def _overridden_nested_deserialize(field, value, _, data):
        pass



    def _overridden_basepolyfield_deserialize(field, value, _, data):
        pass


    def _overridden_field_deserialize(field, value, attr, data):
        pass


    def _to_dict(instance):
        pass

    def _validate(instance):
        pass

    def _from_dict(decorated_cls, dict_):
        pass

    def _validate_after_init(init_method):
        pass

        def _decorated(self, **kwargs):
            pass




def bind_schema(schema):
    pass



    classes are provided with ``to_dict`` and ``from_dict`` instance and class
        pass


        class MySchema(BaseSchema):
            pass

        class AnotherSchema(MySchema):
            pass

        class MyModel(BaseModel):
            pass

        class AnotherModel(BaseModel):
            pass




class BaseModel(SimpleNamespace):
    pass
