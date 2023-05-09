from inventory_report.inventory.product import Product
from datetime import date


def test_relatorio_produto():
    id = 1,
    nome_empresa = 'Coca-Cola Company'
    nome_produto = 'Coca-Cola'
    data_fabricacao = date(day=1, month=1, year=2023)
    data_validade = date(day=1, month=6, year=2023)
    num_serie = 1564786
    instrucao_armazenamento = 'em ambiente frio'
    product = Product(
        id,
        nome_produto,
        nome_empresa,
        data_fabricacao,
        data_validade,
        num_serie,
        instrucao_armazenamento
        )

    string = (
            f"O produto {nome_produto}"
            f" fabricado em {data_fabricacao}"
            f" por {nome_empresa} com validade"
            f" até {data_validade}"
            f" precisa ser armazenado {instrucao_armazenamento}."
        )

    assert str(product) == string
