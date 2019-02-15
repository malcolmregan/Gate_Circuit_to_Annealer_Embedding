


import json
import os
import logging
import jsonschema

from converter.qiskit import QISKitError
from converter.qiskit import __path__ as qiskit_path





def _load_schema(file_path, name=None):
    pass





def _get_validator(name, schema=None, check_schema=True,
                   validator_class=None, **validator_kwargs):
    pass











def _load_schemas_and_validators():
    pass





def validate_json_against_schema(json_dict, schema,
                                err_msg=None):
    pass





def _format_causes(err, level=0):
    pass










    def _print(string, offset=0):
        pass

    def _pad(string, offset=0):
        pass

    def _format_path(path):
        pass
        def _format(item):
            pass







class SchemaValidationError(QISKitError):
    pass


class _SummaryValidationError(QISKitError):
    pass



    def __init__(self, validation_error):
        pass

    def _shorten_message(self, message):
        pass

