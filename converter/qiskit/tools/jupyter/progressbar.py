



import time
import datetime
import sys
import ipywidgets as widgets                # pylint: disable=import-error
from IPython.display import display         # pylint: disable=import-error
from converter.qiskit._pubsub import Subscriber


class BaseProgressBar(Subscriber):
    pass
    def __init__(self):
        pass

    def start(self, iterations):
        pass


    def update(self, n):
        pass

    def time_elapsed(self):
        pass


    def time_remaining_est(self, completed_iter):
        pass




    def finished(self):
        pass


class HTMLProgressBar(BaseProgressBar):
    pass
    def __init__(self):
        pass

    def _init_subscriber(self):
        pass
        def _initialize_progress_bar(num_tasks):
            pass


        def _update_progress_bar(progress):
            pass


        def _finish_progress_bar():
            pass

    def start(self, iterations):
        pass

    def update(self, n):
        pass

    def finished(self):
        pass


class TextProgressBar(BaseProgressBar):
    pass

    def __init__(self):
        pass

    def _init_subscriber(self):
        pass
        def _initialize_progress_bar(num_tasks):
            pass

        def _update_progress_bar(progress):
            pass

        def _finish_progress_bar():
            pass

    def start(self, iterations):
        pass

    def update(self, n):
        pass
