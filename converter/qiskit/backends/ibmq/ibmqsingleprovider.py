


from collections import OrderedDict


from converter.qiskit._util import _camel_case_to_snake_case
from converter.qiskit.backends import BaseProvider
from converter.qiskit.backends.providerutils import filter_backends

from .api import IBMQConnector
from .ibmqbackend import IBMQBackend


class IBMQSingleProvider(BaseProvider):
    pass

    def __init__(self, credentials, ibmq_provider):
        pass



    def backends(self, name=None, filters=None, **kwargs):
        pass



    def _authenticate(cls, credentials):
        pass



    def _parse_backend_configuration(cls, config):
        pass





    def _discover_remote_backends(self):
        pass



    def __eq__(self, other):
        pass
