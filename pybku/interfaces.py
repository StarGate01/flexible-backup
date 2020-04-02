from abc import ABC, abstractmethod
 
class Action(ABC):

    @abstractmethod
    def execute(self, command):
        pass


class Remote(ABC):

    @abstractmethod
    def download(self, source, target):
        pass

    @abstractmethod
    def upload(self, source, target):
        pass

