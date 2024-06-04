from typing import List
from classes import Furniture, Material, Category, Client

class BusinessRules:
    MIN_COST = 100
    MAX_LOAD = 10

    @staticmethod
    def validate_min_cost(cost: float) -> bool:
        return cost >= BusinessRules.MIN_COST

    @staticmethod
    def validate_max_load(current_load: int) -> bool:
        return current_load < BusinessRules.MAX_LOAD

    @staticmethod
    def is_material_available(material: str, available_materials: List[str]) -> bool:
        return material in available_materials

    @staticmethod
    def is_condition_satisfactory(condition: str) -> bool:
        satisfactory_conditions = ["good", "excellent"]
        return condition in satisfactory_conditions

    @staticmethod
    def is_client_registered(client: Client) -> bool:
        return client.registration_data is not None

    @staticmethod
    def has_category(furniture: Furniture) -> bool:
        return furniture.category is not None
