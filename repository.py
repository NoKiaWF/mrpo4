from abc import ABC, abstractmethod
from typing import List

class AbstractRepository(ABC):
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_material(self, material_type: str) -> List:
        pass
