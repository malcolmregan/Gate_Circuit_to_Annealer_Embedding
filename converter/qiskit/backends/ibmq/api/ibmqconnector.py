


import json
import logging
import re
import time

import requests
from requests_ntlm import HttpNtlmAuth



def get_job_url(config, hub, group, project):
    pass


def get_backend_stats_url(config, hub, backend_type):
    pass


def get_backend_url(config, hub, group, project):
    pass


class _Credentials(object):
    pass

    def __init__(self, token, config=None, verify=True, proxy_urls=None,
                 ntlm_credentials=None):
        pass

        if not verify:
            import requests.packages.urllib3 as urllib3


    def obtain_token(self, config=None):
        pass






    def get_token(self):
        pass

    def get_user_id(self):
        pass

    def get_config(self):
        pass

    def set_token(self, access_token):
        pass

    def set_user_id(self, user_id):
        pass


class _Request(object):
    pass
    def __init__(self, token, config=None, verify=True, retries=5,
                timeout_interval=1.0):
        pass






    def check_token(self, respond):
        pass

    def post(self, path, params='', data=None):
        pass



    def put(self, path, params='', data=None):
        pass

    def get(self, path, params='', with_token=True):
        pass

    def _response_good(self, respond):
        pass





    def _parse_response(self, respond):
        pass






class IBMQConnector(object):
    pass

    def __init__(self, token=None, config=None, verify=True):
        pass



    def _check_backend(self, backend, endpoint):
        pass


    def check_credentials(self):
        pass

    def run_job(self, job, backend='simulator', shots=1,
               access_token=None, user_id=None):
        pass













    def get_job(self, id_job, hub=None, group=None, project=None,
                access_token=None, user_id=None):
        pass






    def get_jobs(self, limit=10, skip=0, backend=None, only_completed=False,
                filter=None, hub=None, group=None, project=None,
                access_token=None, user_id=None):
        pass




    def get_status_job(self, id_job, hub=None, group=None, project=None,
                      access_token=None, user_id=None):
        pass





    def get_status_jobs(self, limit=10, skip=0, backend=None, filter=None,
                        hub=None, group=None, project=None, access_token=None,
                        user_id=None):
        pass







    def cancel_job(self, id_job, hub=None, group=None, project=None,
                   access_token=None, user_id=None):
        pass





    def backend_status(self, backend='ibmqx4', access_token=None, user_id=None):
        pass





    def backend_calibration(self, backend='ibmqx4', hub=None, access_token=None, user_id=None):
        pass






    def backend_parameters(self, backend='ibmqx4', hub=None, access_token=None, user_id=None):
        pass






    def available_backends(self, hub=None, group=None, project=None,
                           access_token=None, user_id=None):
        pass



    def api_version(self):
        pass


class ApiError(Exception):
    pass
    def __init__(self, usr_msg=None, dev_msg=None):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass


class BadBackendError(ApiError):
    pass
    def __init__(self, backend):
        pass


class CredentialsError(ApiError):
    pass


class RegisterSizeError(ApiError):
    pass
