


import warnings
import logging

from converter.qiskit import QISKitError
from converter.qiskit._util import _camel_case_to_snake_case
from converter.qiskit.backends import BaseBackend
from converter.qiskit.backends import JobStatus

from .api import ApiError
from .ibmqjob import IBMQJob, IBMQJobPreQobj



class IBMQBackend(BaseBackend):
    pass

    def __init__(self, configuration, provider, credentials, api):
        pass



    def run(self, qobj):
        pass



    def calibration(self):
        pass








    def parameters(self):
        pass







    def properties(self):
        pass




    def status(self):
        pass



    def jobs(self, limit=50, skip=0, status=None, db_filter=None):
        pass










    def retrieve_job(self, job_id):
        pass




    def __repr__(self):
        pass


class IBMQBackendError(QISKitError):
    pass


class IBMQBackendValueError(IBMQBackendError, ValueError):
    pass


def _job_class_from_job_response(job_response):
    pass


def _job_class_from_backend_support(backend):
    pass


def _dict_merge(dct, merge_dct):
    pass


