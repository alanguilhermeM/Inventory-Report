from typing import Dict, Type, List
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json
import csv


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        raise NotImplementedError


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, "r") as file:
            data = json.load(file)
            self.products = [Product(**product) for product in data]

        return self.products


class CsvImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, "r") as file:
            reader = csv.DictReader(file)
            self.products = [Product(**product) for product in reader]

        return self.products


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
