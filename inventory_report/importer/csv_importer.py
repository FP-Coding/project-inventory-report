import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        with open(path) as file:
            try:
                if not path.endswith('.csv'):
                    raise ValueError('Arquivo inválido')
                products = list(csv.DictReader(file))
                return products
            except FileNotFoundError:
                raise ValueError('Arquivo inválido')
