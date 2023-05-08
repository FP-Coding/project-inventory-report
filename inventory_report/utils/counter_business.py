from typing import List, Dict
from collections import Counter


class CounterBusiness:
    @classmethod
    def counter_business_with_more_products(cls, data: List[Dict]):
        names_business = [product["nome_da_empresa"] for product in data]
        return Counter(names_business).most_common(1)[0][0]

    @classmethod
    def counter_quantity_products_by_business(cls, data: List[Dict]):
        names_business = [product["nome_da_empresa"] for product in data]
        return Counter(names_business)
