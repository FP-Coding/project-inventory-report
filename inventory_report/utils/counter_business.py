from typing import List, Dict
from collections import Counter


class CounterBusiness:
    @staticmethod
    def counter_business_with_more_products(data: List[Dict]):
        names_business = [product["nome_da_empresa"] for product in data]
        return Counter(names_business).most_common(1)[0][0]
