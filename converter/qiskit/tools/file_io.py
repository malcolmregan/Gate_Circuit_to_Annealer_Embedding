


import copy
import datetime
import json
import os

import numpy
from sympy import Basic

from converter.qiskit.result._utils import result_from_old_style_dict
from converter.qiskit._qiskiterror import QISKitError
from converter.qiskit.backends import BaseBackend


def convert_qobj_to_json(in_item):
    pass






def convert_json_to_qobj(in_item):
    pass







def file_datestr(folder, fileroot):
    pass






def load_result_from_file(filename):
    pass










class ResultEncoder(json.JSONEncoder):
    pass
    def default(self, o):
        pass



def save_result_to_file(resultobj, filename, metadata=None):
    pass










def _old_style_dict_from_result(result):
    pass


