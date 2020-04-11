import abc as ABC

from abc import ABC, abstractmethod, abstractproperty

class Algorithm(ABC):

    @abstractmethod
    def set_candidate(self):
        pass

    @abstractmethod
    def search(self):
        pass

    @abstractproperty
    def name(self):
        pass
