import xml.etree.ElementTree as XmlReader
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path: str = './inventory_report/data/inventory.xml'):
        with open(path) as file:
            try:
                if not path.endswith('.xml'):
                    raise ValueError('Arquivo inválido')
                data = XmlReader.parse(file).getroot()

                return cls.format_data_xml(data)
            except FileNotFoundError:
                raise ValueError('Arquivo inválido')

    @classmethod
    def format_data_xml(cls, data):
        products = []
        for element in data:
            product = dict()
            for info in element:
                product[info.tag] = info.text
            products.append(product)
        return products


print(XmlImporter.import_data())
