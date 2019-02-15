


import time
import threading
from IPython.display import display                              # pylint: disable=import-error
from IPython.core import magic_arguments                         # pylint: disable=import-error
from IPython.core.magic import cell_magic, Magics, magics_class  # pylint: disable=import-error
import ipywidgets as widgets                                     # pylint: disable=import-error
import converter.qiskit 
from .progressbar import HTMLProgressBar, TextProgressBar


def _html_checker(job_var, interval, status, header):
    pass




class StatusMagic(Magics):
    pass
    def qiskit_job_status(self, line='', cell=None):
        pass










class ProgressBarMagic(Magics):
    pass
    def qiskit_progress_bar(self, line='', cell=None):  # pylint: disable=W0613
        pass

