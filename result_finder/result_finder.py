from abc import ABC, abstractmethod

"""
For Every type of result, create new object that should inherit from ResultFinder Interface
"""


class ResultFinder(ABC):
    def __init__(self, db):
        self.db = db

    @abstractmethod
    def prepare_result(self): pass

    @abstractmethod
    def get_result(self): pass
