from typing import List, Dict
from inventory_report.utils.manipulator_date import ManipulatorDate
from inventory_report.utils.counter_business import CounterBusiness


class SimpleReport:
    @staticmethod
    def generate(data: List[Dict]):
        old_manufacturing = ManipulatorDate.get_oldest_manufacturing_date(data)
        early_expiration = ManipulatorDate.get_earliest_expiration_date(data)
        name = CounterBusiness.counter_business_with_more_products(data)

        return (
            f'Data de fabricação mais antiga: {old_manufacturing}\n'
            f'Data de validade mais próxima: {early_expiration}\n'
            f'Empresa com mais produtos: {name}'
        )
