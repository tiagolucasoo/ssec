# SSEC - Sistema de Sugestão Estratégica de Compras
- Um sistema desktop desenvolvido para realizar análises de vendas e sugerir compras/reposições de estoque. O objetivo é auxiliar pequenos negócios a manterem o estoque em níveis ideais, de forma simples e direta.


## 📝 Criação do Projeto
- Desenvolvido inicialmente como trabalho semestral para a disciplina de `Construção de Aplicações em Ambiente Visual`, o projeto consistia na criação de um sistema com padrão MVC e persistência de dados.

- Com interface moderna feita em `CustomTkinter`, a aplicação permite o cadastro de produtos, categorias e vendas (manualmente ou por importação em lote), possibilitando cálculos automatizados de reposição com base em filtros e desempenho de vendas.

- O objetivo nesta primeira versão é atuar como um **módulo auxiliar**, podendo ser integrado a sistemas existentes, desde que utilizem os mesmos códigos de produto.


## ✨ Funcionalidades
- **Cadastro de Categorias**: Inserção simples apenas com o nome da categoria.
- **Cadastro de Produtos**: Inclui Código, Código de Barras, Descrição, Marca, Categoria (via ComboBox), Custo, Venda e Curva ABC.
- **Cadastro de Vendas**: Informações por produto, com quantidade vendida e período (em dias).
- **Importação em Lote**: Permite a importação de arquivos `.txt` com dados de produtos ou vendas, acelerando a entrada de dados.
- **Sugestão de Compras**:
  - Filtragem por Categoria, Curva ABC e Período
  - Quantidade sugerida de cada item
  - Valor total de custo e venda
  - Margem de lucro individual
- **Banco de Dados**: Utiliza `SQLite3`, tornando o sistema portátil e sem dependência de servidores externos.

## 🛠️ Tecnologias Utilizadas
-   Python
-   CustomTkinter
-   SQLite 3

## 📂 Estrutura do Projeto
-   `main.py`
-   `banco.db`
-   `readme.md`<br><br>
-  `📂 CONTROLLER`
-   -   `controller.py`
-  `📂 MODEL`
-   -   `model.py`
-  `📂 VIEW`
-   -   `cad_categorias.py`
-   -   `cad_produtos.py`
-   -   `cad_vendas.py`
-   -   `imp_produtos.py`
-   -   `imp_vendas.py`
-   -   `pag_inicial.py`
-   -   `sugestao_compras.py`

## 🔒 Alterações e Exclusões
- Nesta versão inicial, o SSEC **não permite alterações ou exclusões de dados diretamente pela interface** (Embora isso seja possível diretamente no BD). Essa decisão visa garantir a integridade das informações cadastradas após as validações, mantendo o foco principal na análise e sugestão com base em dados consistentes.
- O controle total de dados será implementado nas próximas versões, juntamente com o módulo de estoque — que reforçará a funcionalidade de sugestões com variavéis como estoque atual, estoque mínimo e similares.

## 🔮 Próximos Passos
- Implementar módulo de controle de estoque
- Desenvolver uma versão web com Flask (Jinja2, HTML, CSS, JS)
- Evoluir para um ERP simplificado:
  - Geração automática de código de produtos
  - Integração de módulos adicionais (estoque, financeiro, etc.)