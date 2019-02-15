



import logging
import copy
from collections import OrderedDict

import numpy

from converter.qiskit import QISKitError, QuantumCircuit




class ExperimentResult(object):
    pass

    def __init__(self, qobj_result_experiment):
        pass


    def counts(self):
        pass

    def snapshots(self):
        pass

    def statevector(self):
        pass

    def unitary(self):
        pass


class Result(object):
    pass

    def __init__(self, qobj_result, experiment_names=None):
        pass


    def __str__(self):
        pass


    def __getitem__(self, i):
        pass

    def __len__(self):
        pass

    def __iadd__(self, other):
        pass




    def __add__(self, other):
        pass


    def _is_error(self):
        pass

    def get_status(self):
        pass

    def circuit_statuses(self):
        pass


    def get_circuit_status(self, icircuit):
        pass


    def get_job_id(self):
        pass


    def get_ran_qasm(self, name):
        pass



    def get_data(self, circuit=None):
        pass












    def _get_experiment(self, key=None):
        pass






    def get_counts(self, circuit=None):
        pass





    def get_statevector(self, circuit=None):
        pass





    def get_unitary(self, circuit=None):
        pass





    def get_snapshots(self, circuit=None):
        pass





    def get_snapshot(self, slot=None, circuit=None):
        pass






    def get_names(self):
        pass


    def average_data(self, name, observable):
        pass




    def get_qubitpol_vs_xval(self, nqubits, xvals_dict=None):
        pass








def _status_or_success(obj):
    pass
