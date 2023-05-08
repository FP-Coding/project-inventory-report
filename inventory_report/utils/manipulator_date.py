from typing import List, Dict
from datetime import datetime


class ManipulatorDate:
    @staticmethod
    def get_oldest_manufacturing_date(data: List[Dict]):
        old_date = min(
            data,
            key=lambda product:
                product["data_de_fabricacao"]
        )
        return old_date["data_de_fabricacao"]

    @staticmethod
    def get_earliest_expiration_date(data: List[Dict]):
        TODAY = datetime.now().strftime("%Y-%m-%d")
        dates = [
                    product["data_de_validade"]
                    for product in data
                    if product["data_de_validade"] >= TODAY
                ]
        early_date = min(
            dates
        )
        return early_date
