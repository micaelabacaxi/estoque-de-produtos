Coleção de ferramentas em Python para gestão de produtos, cálculo de lucros e análise financeira.

---

## 📁 Projetos

### 1. **Calculadora Financeira de Produtos** 
**Arquivo:** `calculadorafinanceira.py`

#### 🎯 O que faz?
Permite adicionar produtos e calcular automaticamente:
- **Preço de venda** baseado em custo + margem + imposto
- **Análise de lucro** por produto
- **Simulação de cenários** com diferentes margens e impostos

#### 💻 Como usar?
```bash
python calculadorafinanceira.py
```

#### 📋 Funcionalidades:
- ✅ Adicionar novos produtos dinamicamente
- ✅ Calcular preço com fórmula: `Custo × (1 + Margem%) × (1 + Imposto%)`
- ✅ Listar todos os produtos
- ✅ Analisar lucro unitário e percentual
- ✅ Simular diferentes cenários de preço
- ✅ Dados persistem em arquivo JSON

#### 📊 Exemplo de uso:
```
Digite o nome do produto: Camiseta
Digite o preço de custo: 50
Digite a margem de lucro (%): 30
Digite o imposto (%): 28

✓ Preço de venda calculado: R$ 83,20
```

---

### 2. **Gestor de Estoque e Vendas**
**Arquivo:** `Estoque.py`

#### 🎯 O que faz?
Gerencia o estoque de produtos com:
- **Busca de produtos** por nome
- **Vendas** com atualização automática de estoque
- **Validação de quantidade** disponível
- **Cálculo de total** da venda

#### 💻 Como usar?
```bash
python Estoque.py
```

#### 📋 Funcionalidades:
- ✅ Buscar produtos por nome
- ✅ Verificar preço e disponibilidade
- ✅ Realizar vendas com validação
- ✅ Atualizar quantidade em estoque
- ✅ Tratamento de erros (quantidade insuficiente, produto não encontrado)

#### 📊 Exemplo de uso:
```
Qual produto está procurando? camisa
✓ Produto camisa disponível para venda
Quantas unidades deseja comprar? 2

O total da compra é R$ 150.00
Quantidade restante: 98
```

---

### 3. **Cálculo de Impostos e Vendas**
**Arquivo:** `impostoeVendas.py`

#### 🎯 O que faz?
Calcula o impacto de impostos nas vendas:
- **Aplicar impostos** aos produtos
- **Registrar vendas** com desconto de estoque
- **Exibir preços finais** com impostos

#### 💻 Como usar?
```bash
python impostoeVendas.py
```

#### 📋 Funcionalidades:
- ✅ Mostrar preços com imposto automático
- ✅ Buscar e vender produtos
- ✅ Validar estoque
- ✅ Atualizar quantidade de produtos

---

### 4. **Calculadora IA** (Em desenvolvimento)
**Arquivo:** `IA.py`

Projeto futuro para integração com inteligência artificial.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Dicionários** para armazenamento de dados
- **JSON** para persistência (em alguns projetos)
- **Manipulação de strings** e entrada de usuário

---

## 📊 Comparação de Projetos

| Projeto | Foco | Funcionalidade | Complexidade |
|---------|------|----------------|--------------|
| Calculadora Financeira | Preços e Lucros | Simulação de cenários | Média |
| Gestor de Estoque | Vendas | Controle de estoque | Média |
| Impostos e Vendas | Fiscalidade | Cálculo de impostos | Baixa |

---

## 🚀 Como Começar

### Pré-requisitos
- Python 3.7 ou superior
- Editor de texto (VS Code, PyCharm, etc.)

### Instalação
```bash
# Clone ou baixe o repositório
cd NovoProjeto/PROJETOS

# Execute o projeto desejado
python calculadorafinanceira.py
```

---

## 📈 Próximas Melhorias Sugeridas

### Curto Prazo
- [ ] Adicionar validação de entrada (valores negativos, duplicatas)
- [ ] Interface gráfica simples com tkinter
- [ ] Exportar relatórios em PDF

### Médio Prazo
- [ ] Integrar banco de dados (SQLite)
- [ ] Dashboard com gráficos (matplotlib, plotly)
- [ ] Sistema de usuários com login

### Longo Prazo
- [ ] API REST com Flask/Django
- [ ] Integração com IA para previsões
- [ ] Aplicativo mobile

---

## 📝 Estrutura de Dados

### Formato de Produto (Dicionário)
```python
{
    "camisa": {
        "preco": 500,           # Preço de custo
        "quantidade": 100,      # Quantidade em estoque
        "preco_venda": 750,     # Preço final ao cliente
        "imposto": 0.28         # Imposto aplicado (28%)
    }
}
```

---

## 💡 Dicas de Uso

1. **Para testes rápidos:** Use os dados pré-carregados nos dicionários
2. **Para aprender:** Analise a estrutura de cada função
3. **Para expandir:** Adicione novas funções seguindo o padrão existente

---

## 📚 Conceitos Python Aplicados

- ✅ Dicionários aninhados
- ✅ Funções com parâmetros
- ✅ Loops (for, while)
- ✅ Condicionais (if/elif/else)
- ✅ Tratamento de exceções (try/except)
- ✅ Formatação de strings (f-strings)
- ✅ Input/Output de usuário

---

## 👨‍💻 Autor

Desenvolvido para aprendizado de Python e conceitos de programação.

---

## 📞 Suporte

Para dúvidas sobre os projetos:
1. Verifique os comentários no código
2. Execute os exemplos passo a passo
3. Teste com dados diferentes

---
