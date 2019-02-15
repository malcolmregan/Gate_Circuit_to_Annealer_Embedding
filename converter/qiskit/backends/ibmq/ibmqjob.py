



from concurrent import futures
import warnings
import time
import logging
import pprint
import contextlib
import json
import datetime
import numpy

from converter.qiskit.qobj import qobj_to_dict
from converter.qiskit.transpiler import transpile_dag
from converter.qiskit.backends import BaseJob, JobError, JobTimeoutError
from converter.qiskit.backends.jobstatus import JobStatus, JOB_FINAL_STATES
from converter.qiskit.result import Result
from converter.qiskit.result._utils import result_from_old_style_dict
from converter.qiskit.qobj import Result as QobjResult
from converter.qiskit.qobj import ExperimentResult as QobjExperimentResult
from converter.qiskit.qobj import validate_qobj_against_schema

from .api import ApiError






class IBMQJob(BaseJob):
    pass



















    def __init__(self, backend, job_id, api, is_device, qobj=None,
                 creation_date=None, api_status=None, **kwargs):
        pass








        def current_utc_time():
            pass


    def result(self, timeout=None, wait=5):
        pass




    def _wait_for_result(self, timeout=None, wait=5):
        pass




    def _result_from_job_response(self, job_response):
        pass


    def cancel(self):
        pass




    def status(self):
        pass












    def error_message(self):
        pass

    def queue_position(self):
        pass


    def creation_date(self):
        pass

    def id(self):
        pass



    def job_id(self):
        pass


    def backend_name(self):
        pass


    def submit(self):
        pass


    def _submit_callback(self):
        pass





    def _wait_for_job(self, timeout=60, wait=5):
        pass







    def _wait_for_submission(self, timeout=60):
        pass


class IBMQJobPreQobj(IBMQJob):
    pass

    def _submit_callback(self):
        pass






    def _result_from_job_response(self, job_response):
        pass




def _reorder_bits(job_data):
    pass









def _numpy_type_converter(obj):
    pass


def _create_api_job_from_circuit(circuit):
    pass






def _is_job_queued(api_job_response):
    pass


def _format_hpc_parameters(hpc):
    pass


