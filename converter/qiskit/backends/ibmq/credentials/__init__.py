

from collections import OrderedDict
import logging

from converter.qiskit import QISKitError
from .credentials import Credentials
from ._configrc import read_credentials_from_qiskitrc, store_credentials
from ._environ import read_credentials_from_environ
from ._qconfig import read_credentials_from_qconfig



def discover_credentials(qiskitrc_filename=None):
    pass








