from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.importer_manager import importer_manager


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        method = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate,
        }
        importer = importer_manager(path)
        data = importer.import_data(path)
        return method[type](data)
