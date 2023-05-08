from datetime import date
from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 1,
    nome_empresa = 'Coca-Cola Company'
    nome_produto = 'Coca-Cola'
    data_fabricacao = date(day=1, month=1, year=2023)
    data_validade = date(day=1, month=6, year=2023)
    num_serie = 1564786
    instrucao_armazenamento = 'Precisa ser armazenado em ambiente frio'
    product = Product(
        id,
        nome_produto,
        nome_empresa,
        data_fabricacao,
        data_validade,
        num_serie,
        instrucao_armazenamento
        )
    assert product.id == id
    assert product.nome_do_produto == nome_produto
    assert product.nome_da_empresa == nome_empresa
    assert product.data_de_fabricacao == str(data_fabricacao)
    assert product.data_de_validade == str(data_validade)
    assert product.numero_de_serie == num_serie
    assert product.instrucoes_de_armazenamento == instrucao_armazenamento
