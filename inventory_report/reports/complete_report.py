from typing import List, Dict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.utils.counter_business import CounterBusiness


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data: List[Dict]):
        quantities = CounterBusiness.counter_quantity_products_by_business(
            data
        )
        formated_quantities = ''
        for empresa, quantity in quantities.items():
            formated_quantities += f'- {empresa}: {quantity}\n'
        return (
            f'{SimpleReport.generate(data)}\n'
            f'Produtos estocados por empresa:\n'
            f'{formated_quantities}'
        )
