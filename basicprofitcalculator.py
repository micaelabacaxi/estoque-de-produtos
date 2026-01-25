dic_produtos = {"camisa" : {"preco": 500, "quantidade": 100, "preco_venda": 750, "imposto": 0.28},
    "calca": {"preco": 199.99, "quantidade": 100, "preco_venda": 299.99, "imposto": 0.28},
    "tenis": {"preco": 300, "quantidade": 50, "preco_venda": 450, "imposto": 0.28},
    "blusao": {"preco": 400, "quantidade": 30, "preco_venda": 600, "imposto": 0.32},
    "meia": {"preco": 600, "quantidade": 20, "preco_venda": 900, "imposto": 0.14},
    "bone": {"preco": 150, "quantidade": 80, "preco_venda": 225, "imposto": 0.10},
    "botas": {"preco": 300, "quantidade": 40, "preco_venda": 450, "imposto": 0.35}
} 
 
produtos = dic_produtos.keys()  # ✅ "produtos"

def calcular_lucro_por_produto(produtos):
    for produto in produtos:
        dados = dic_produtos[produto]
        preco = dados["preco"]
        preco_venda = dados["preco_venda"]
        imposto = dados["imposto"]
        base_de_preco = preco - (preco * imposto)
        lucro_total = preco_venda - base_de_preco
        print(f"O lucro do produto {produto} e R${lucro_total:.2f}")

def adicionar_produto():
    nome = input("Nome do produto: ")
    
    
    preco = float(input("Preço: "))
    

    quantidade = int(input("Quantidade: "))

    preco_venda = float(input("Preço de venda: "))

    imposto = float(input("Imposto (em decimal, ex: 0.28 para 28%): "))
    dic_produtos[nome] = {
        "preco": preco,
        "quantidade": quantidade,
        "preco_venda": preco_venda,
        "imposto": imposto
    }

    print(f"Produto {nome} adicionado com sucesso.")

adicionar_produto()
calcular_lucro_por_produto(produtos)