from typing import List
from business_rules import BusinessRules
from classes import Furniture, Material, Client
from repository import AbstractRepository

class FurnitureService:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def add_furniture(self, furniture: Furniture) -> bool:
        if not BusinessRules.is_condition_satisfactory(furniture.condition):
            return False
        if not BusinessRules.has_category(furniture):
            return False
        self.repository.add(furniture)
        return True

    def get_furniture(self, material_type: str) -> List[Furniture]:
        return self.repository.get_by_material(material_type)

class ClientService:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def register_client(self, client: Client) -> bool:
        if not BusinessRules.is_client_registered(client):
            self.repository.add(client)
            return True
        return False

    def get_clients(self) -> List[Client]:
        return self.repository.get_all()