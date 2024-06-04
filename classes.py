from dataclasses import dataclass

@dataclass(frozen=True)
class Material:
    material_type: str

@dataclass(frozen=True)
class Category:
    name: str

@dataclass(frozen=True)
class Furniture:
    condition: str
    material: Material
    category: Category = None

class RestorationOrder:
    def __init__(self, cost, order_date):
        self.cost = cost
        self.order_date = order_date

    def __eq__(self, other):
        if isinstance(other, RestorationOrder):
            return self.cost == other.cost and self.order_date == other.order_date
        return False

class Workshop:
    def __init__(self, load):
        self.load = load

    def __eq__(self, other):
        if isinstance(other, Workshop):
            return self.load == other.load
        return False

class Client:
    def __init__(self, registration_data):
        self.registration_data = registration_data

    def __eq__(self, other):
        if isinstance(other, Client):
            return self.registration_data == other.registration_data
        return False