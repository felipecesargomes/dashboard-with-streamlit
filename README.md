# Dashboard de Vendas com Streamlit

Dashboard interativo para análise e visualização de dados de vendas, desenvolvido com Streamlit e Plotly.

## 📋 Descrição

Projeto educacional de um dashboard que exibe:
- Visualização de dataset completo de vendas
- Análise de receita por período
- Desempenho de vendedores

## 🗂️ Estrutura do Projeto

```
dashboard-with-streamlit/
├── app.py              # Aplicação Streamlit principal
├── dataset.py          # Carregamento e processamento de dados
├── utils.py            # Funções utilitárias (formatação de números)
├── data/
│   └── vendas.json     # Dados fictícios de vendas
├── .venv/              # Ambiente virtual Python
├── .gitignore          # Configuração Git
└── README.md           # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- **Streamlit** - Framework para criar dashboards web
- **Pandas** - Manipulação e análise de dados
- **Plotly** - Visualizações interativas
- **Python 3.x** - Linguagem de programação

## 📊 Dados

O arquivo `data/vendas.json` contém dados fictícios de vendas com as seguintes informações:
- ID da venda
- Data da compra (formato DD/MM/YYYY)
- Produto
- Quantidade
- Preço unitário
- Total da venda
- Vendedor
- Região

Exemplo:
```json
{
  "id": 1,
  "data_compra": "15/01/2024",
  "produto": "Notebook Dell",
  "quantidade": 2,
  "preco_unitario": 3500.00,
  "total": 7000.00,
  "vendedor": "João Silva",
  "regiao": "Sul"
}
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- pip

### Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd dashboard-with-streamlit
```

2. Crie um ambiente virtual:
```bash
python -m venv .venv
```

3. Ative o ambiente virtual:
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. Instale as dependências:
```bash
pip install streamlit pandas plotly
```

### Executar o Dashboard

```bash
streamlit run app.py
```

A aplicação abrirá no navegador em `http://localhost:8501`

## 📑 Funcionalidades

### Aba 1: Dataset
Exibe a tabela completa com todos os registros de vendas em formato interativo.

### Aba 2: Receita
Mostra métricas importantes:
- Receita Total (formatada com conversão para milhões/mil quando necessário)
- Quantidade de Vendas

### Aba 3: Vendedores
(A implementar) Rankings e desempenho dos vendedores por região.

## 📝 Arquivos Principais

### `app.py`
Arquivo principal da aplicação Streamlit que configura:
- Título e layout do dashboard
- Abas de navegação
- Componentes de visualização

### `dataset.py`
Script que:
- Lê dados do arquivo JSON
- Converte para DataFrame Pandas
- Processa coluna de data com formato correto (DD/MM/YYYY)

### `utils.py`
Contém funções utilitárias:
- `format_number()` - Formata números com prefixo (R$) e conversão automática para mil/milhões

## 🔧 Configuração

O dashboard utiliza layout `wide` para melhor aproveitamento da tela.

## 📈 Próximas Melhorias

- [ ] Implementar gráficos de receita por período
- [ ] Adicionar filtros interativos por período e região
- [ ] Criar rankings de vendedores na aba 3
- [ ] Adicionar mais métricas (ticket médio, produto mais vendido, etc)
- [ ] Criar visualizações com Plotly (gráficos de linha, barras, pizza)
- [ ] Exportar relatórios em PDF

## 📄 Licença

Projeto educacional sem licença específica.

## 👤 Autor

Felipe César
