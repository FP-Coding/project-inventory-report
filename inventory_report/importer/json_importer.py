import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        with open(path) as file:
            try:
                if not path.endswith('.json'):
                    raise ValueError('Arquivo inválido')
                products = json.load(file)
                return products
            except FileNotFoundError:
                raise ValueError('Arquivo inválido')
