dic_produtos = { "cafe": {"preco": 500, "quantidade": 100},
    "pao": {"preco": 200, "quantidade": 50},
    "leite": {"preco": 300, "quantidade": 30},
    "ovos": {"preco": 400, "quantidade": 20},
    "manteiga": {"preco": 600, "quantidade": 15},
    "queijo": {"preco": 800, "quantidade": 10},
    "presunto": {"preco": 700, "quantidade": 25}}


produto_buscado = input("qual produto voce esta procurando?  ")
produto_buscado = produto_buscado.lower().split(',')
for produto_buscado in dic_produtos
    preco = dic_produto
    if produto_buscado in dic_produtos:
        print(f"produto {produto_buscado} disponivel para venda")
        preco = dic_produtos[produto_buscado]
        quantidade = int(input(f"O preco do {produto_buscado} e R${preco:.2f} Gostaria de comprar quantas unidades?"))
        if quantidade <= dic_produtos[produto_buscado]["quantidade"]:
            total = preco * quantidade
            print(f"o total da compra e R${total:.2f}")
        if quantidade > dic_produtos[produto_buscado]["quantidade"]: 
            print(f"desculpe, nao temos essa quantidade em estoque. Temos apenas {dic_produtos[produto_buscado]['quantidade']} unidades disponiveis.")    
    else:
        print(f"desculpe, o produto {produto_buscado} nao esta disponivel em estoque.")
except KeyError:
    print(f"desculpe, o produto {produto_buscado} nao esta disponivel em estoque.")
except ValueError:

    print("quantidade invalida, por favor insira um numero inteiro.")   
