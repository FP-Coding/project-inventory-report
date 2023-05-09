import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.importer_manager import importer_manager


def main():
    try:
        _, path, type = sys.argv
        importer = importer_manager(path)

        result = InventoryRefactor(importer).import_data(path, type)
        sys.stdout.write(result)
    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)
