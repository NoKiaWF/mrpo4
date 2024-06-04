from use_case import FurnitureService, ClientService
from xml_repository import XMLRepository
from classes import Furniture, Material, Category, Client

# Инициализация репозитория
repository = XMLRepository('data.xml')

# Инициализация служб
furniture_service = FurnitureService(repository)
client_service = ClientService(repository)

# Пример использования служб
material = Material(material_type="wood")
category = Category(name="antique")
furniture = Furniture(condition="good", material=material, category=category)

if furniture_service.add_furniture(furniture):
    print("Furniture added successfully!")
else:
    print("Failed to add furniture.")

client = Client(registration_data="2024-01-01")
if client_service.register_client(client):
    print("Client registered successfully!")
else:
    print("Client is already registered.")
