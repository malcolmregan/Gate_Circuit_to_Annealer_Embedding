



import sys
import time
import threading
from converter.qiskit._qiskiterror import QISKitError
if ('ipykernel' in sys.modules) and ('spyder' not in sys.modules):
    _NOTEBOOK_ENV = True
    from IPython.display import display                              # pylint: disable=import-error
    import ipywidgets as widgets                                     # pylint: disable=import-error
    from converter.qiskitskit.tools.jupyter.jupyter_magics import _html_checker    # pylint: disable=C0412


def _text_checker(job, interval):
    pass







def job_monitor(job, interval=2, monitor_async=False):
    pass



