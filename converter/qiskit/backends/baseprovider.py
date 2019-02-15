



from abc import ABC, abstractmethod
import logging




class BaseProvider(ABC):
    pass
    def __init__(self, *args, **kwargs):
        pass

    def available_backends(self, *args, **kwargs):
        pass



    def get_backend(self, name=None, **kwargs):
        pass





    def backends(self, name=None, **kwargs):
        pass



    def __eq__(self, other):
        pass

