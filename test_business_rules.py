import unittest
from classes import Furniture, Material, Category, Client
from business_rules import BusinessRules

class TestBusinessRules(unittest.TestCase):

    def test_validate_min_cost(self):
        self.assertTrue(BusinessRules.validate_min_cost(150))
        self.assertFalse(BusinessRules.validate_min_cost(50))

    def test_validate_max_load(self):
        self.assertTrue(BusinessRules.validate_max_load(5))
        self.assertFalse(BusinessRules.validate_max_load(15))

    def test_is_material_available(self):
        materials = ["wood", "metal", "fabric"]
        self.assertTrue(BusinessRules.is_material_available("wood", materials))
        self.assertFalse(BusinessRules.is_material_available("glass", materials))

    def test_is_condition_satisfactory(self):
        self.assertTrue(BusinessRules.is_condition_satisfactory("good"))
        self.assertFalse(BusinessRules.is_condition_satisfactory("poor"))

    def test_is_client_registered(self):
        registered_client = Client(registration_data="2024-01-01")
        unregistered_client = Client(registration_data=None)
        self.assertTrue(BusinessRules.is_client_registered(registered_client))
        self.assertFalse(BusinessRules.is_client_registered(unregistered_client))

    def test_has_category(self):
        material = Material(material_type="wood")
        category = Category(name="antique")
        furniture_with_category = Furniture(condition="good", material=material, category=category)
        furniture_without_category = Furniture(condition="good", material=material)
        self.assertTrue(BusinessRules.has_category(furniture_with_category))
        self.assertFalse(BusinessRules.has_category(furniture_without_category))

if __name__ == '__main__':
    unittest.main()

#Запуск тестов python -m unittest test_business_rules.py
