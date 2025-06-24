# Checklist – Sistema de Sugestão Estratégica de Compras (SSEC)
- Projeto em criação (Ainda não finalizado) | Assim que finalizado (Julho) este será postado no meu LinkedIn e terá aqui o readme alterado descrevendo as funcionalidades

## Etapa 1 – Estrutura Inicial
- [X] Criar estrutura de pastas (`models`, `views`, `controllers`, `db`, `utils`)
- [X] Criar banco SQLite com tabelas: `produtos`, `categorias`, `vendas`
- [X] Criar script inicial para conexão com o banco

## Etapa 2 – Tela Principal e Menu
- [X] Criar tela principal com menu (Tkinter ou CustomTkinter)
- [X] Criar botões de acesso para cada funcionalidade
- [ ] Cria Menu

## Etapa 3 – Cadastro de Categorias
- [X] Criar formulário de cadastro de categoria
- [X] Implementar função `adicionar_categoria` no banco
- [X] Listar categorias cadastradas (opcional: atualizar/deletar)

## Etapa 4 – Cadastro de Produtos
- [X] Criar tela com campos: código, descrição, marca, categoria, custo, venda
- [ ] Implementar função `adicionar_produto` no banco
- [X] Combobox para seleção de categoria

## Etapa 5 – Importação Manual de Vendas
- [X] Criar formulário para digitar: código, quantidade, período
- [ ] Validar e salvar os dados na tabela `vendas`

## Etapa 6 – Importação de Vendas por Lote (.txt)
- [ ] Criar tela para upload/seleção do arquivo `.txt`
- [ ] Ler arquivo linha a linha, validar e salvar dados
- [ ] Mensagem de sucesso ou erro

## Etapa 7 – Importação de Produtos por Lote (.txt)
- [ ] Criar tela para importar produtos via arquivo `.txt`
- [ ] Ler dados no formato: `código,descrição,marca,categoria,custo,preço`
- [ ] Validar e inserir no banco

### Exemplo de conteúdo do arquivo `.txt`:
```txt
1010,Energético Furioso,Furioso,Categorias Bebidas,3.00,5.00
1011,Água Mineral 500ml,Crystal,Categorias Bebidas,1.20,2.50
1012,Cerveja Gelada,Lager,Categorias Bebidas,2.50,4.00
