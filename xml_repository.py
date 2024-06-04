import xml.etree.ElementTree as ET
from typing import List
from classes import Furniture, Material, Client, Category
from repository import AbstractRepository

class XMLRepository(AbstractRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path
        try:
            self.tree = ET.parse(self.file_path)
            self.root = self.tree.getroot()
        except FileNotFoundError:
            self.root = ET.Element("root")
            self.tree = ET.ElementTree(self.root)
            self.tree.write(self.file_path)

    def add(self, item):
        if isinstance(item, Furniture):
            self._add_furniture(item)
        elif isinstance(item, Client):
            self._add_client(item)
        self.tree.write(self.file_path)

    def _add_furniture(self, furniture: Furniture):
        furniture_elem = ET.Element('Furniture')
        condition_elem = ET.SubElement(furniture_elem, 'Condition')
        condition_elem.text = furniture.condition
        material_elem = ET.SubElement(furniture_elem, 'Material')
        material_elem.text = furniture.material.material_type
        if furniture.category:
            category_elem = ET.SubElement(furniture_elem, 'Category')
            category_elem.text = furniture.category.name
        self.root.append(furniture_elem)

    def _add_client(self, client: Client):
        client_elem = ET.Element('Client')
        reg_data_elem = ET.SubElement(client_elem, 'RegistrationData')
        reg_data_elem.text = client.registration_data
        self.root.append(client_elem)

    def get_all(self):
        return [self._element_to_client(client_elem) for client_elem in self.root.findall('Client')]

    def get_by_material(self, material_type: str) -> List[Furniture]:
        return [self._element_to_furniture(furniture_elem)
                for furniture_elem in self.root.findall(f"./Furniture[Material='{material_type}']")]

    def _element_to_furniture(self, elem):
        condition = elem.find('Condition').text
        material = Material(material_type=elem.find('Material').text)
        category_elem = elem.find('Category')
        category = Category(name=category_elem.text) if category_elem is not None else None
        return Furniture(condition=condition, material=material, category=category)

    def _element_to_client(self, elem):
        registration_data = elem.find('RegistrationData').text
        return Client(registration_data=registration_data)
