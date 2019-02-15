


import warnings
from concurrent import futures
import logging
import sys
import functools

from converter.qiskit.backends import BaseJob, JobStatus, JobError
from converter.qiskit.qobj import validate_qobj_against_schema



def requires_submit(func):
    pass


    def _wrapper(self, *args, **kwargs):
        pass


class AerJob(BaseJob):
    pass



    def __init__(self, backend, job_id, fn, qobj):
        pass

    def submit(self):
        pass




    def result(self, timeout=None):
        pass





    def cancel(self):
        pass

    def status(self):
        pass




    def backend_name(self):
        pass


    def backend(self):
        pass
