



from abc import ABC, abstractmethod


class BaseJob(ABC):
    pass

    def __init__(self, backend, job_id):
        pass


    def job_id(self):
        pass

    def backend(self):
        pass

    def submit(self):
        pass

    def result(self):
        pass

    def cancel(self):
        pass

    def status(self):
        pass
