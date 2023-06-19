# Projeto Inventory Report

Projeto realizado durante módulo de Ciência da Computação do curso de desenvolvimento web da Trybe.

<details>
  <summary><strong>👨‍💻 O que foi feito</strong></summary></br>

Neste projeto implementei, utilizando a Programação Orientada a Objetos, um **gerador de relatórios** que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados. Utilizando alguns design paterns para resolver o problemas propostos como: **Strategy**, **Factory**, **Iterator**, **Decorator**.

  Esses dados de estoque poderão ser obtidos de diversas fontes:

- Através da importação de um arquivo `CSV`;
- Através da importação de um arquivo `JSON`;
- Através da importação de um arquivo `XML`.

Além disso, o relatório final possuirá duas versões: **simples** e **completa**.

Report simples:

```bash
Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com mais produtos: NOME DA EMPRESA
```

Report completo:

```bash
Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com mais produtos: NOME DA EMPRESA
Produtos estocados por empresa:
- Physicians Total Care, Inc.: QUANTIDADE
- Newton Laboratories, Inc.: QUANTIDADE
- Forces of Nature: QUANTIDADE
```

</details>
<details>
  <summary><strong>🛼 Como rodar o projeto</strong></summary></br>

**Localmente:**

- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `python3 -m pip install -r dev-requirements.txt`
- `pip install .`
- `inventory_report parametro_1 parametro_2`

Exemplo:

```bash
inventory_report inventory_report/data/inventory.csv simples
```

</details>

<details>
  <summary><strong>📄 Tecnologias utilizadas</strong></summary><br />
  
- `Python`
- `Pytest`

</details>
<details>
  <summary><strong>🚵 Habilidades</strong></summary><br />

- Desenvolvimento de Padrões de Projeto;
- Desenvolvimento sob o paradigma de Programação Orientada a Objetos.

</details>
