from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def importer_manager(path: str):
    importer = None
    key = {
        "csv": CsvImporter,
        "json": JsonImporter,
        "xml": XmlImporter,
    }
    if path.endswith(".csv"):
        importer = key["csv"]
    elif path.endswith(".json"):
        importer = key["json"]
    else:
        importer = key["xml"]

    return importer
