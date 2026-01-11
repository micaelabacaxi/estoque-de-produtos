dic_produtos = {
    "camisa": {"preco": 500, "quantidade": 100},
    "calca": {"preco": 199.99, "quantidade": 50},
    "tenis": {"preco": 300, "quantidade": 30},
    "blusao": {"preco": 400, "quantidade": 20},
    "meia": {"preco": 600, "quantidade": 15}       
}
imposto = 0.28

for produto in dic_produtos:
    preco = dic_produtos[produto]["preco"]
    preco_com_imposto = preco + (preco * imposto)
    print(f"O preco do {produto} com imposto e R${preco_com_imposto:.2f}")
 


 ########################################################################################

produto_buscado = input("qual produto voce esta procurando?  ")
produtos_buscados = [p.strip().lower() for p in produto_buscado.split(',')]


for produto in produtos_buscados:
    try:
        if produto in dic_produtos:
            preco = dic_produtos[produto]["preco"]
            print(f"produto {produto} disponivel para venda")
            quantidade = int(input(f"O preco do {produto} e R${preco:.2f} Gostaria de comprar quantas unidades?"))
            if quantidade <= 0:
                print("Quantidade invalida.")
            elif quantidade <= dic_produtos[produto_buscado]["quantidade"]:
                total = preco * quantidade
                dic_produtos[produto_buscado]["quantidade"] -= quantidade  # Atualiza estoque
                print(f"O total da compra e R${total:.2f}. Quantidade restante : {dic_produtos[produto_buscado]['quantidade']}")
            else:
                if quantidade > dic_produtos[produto_buscado]["quantidade"]:
                    print(f"desculpe, nao temos essa quantidade em estoque. Temos apenas {dic_produtos[produto_buscado]['quantidade']} unidades disponiveis.")
        else:
            print(f"desculpe, o produto {produto_buscado} nao esta disponivel em estoque.")
    except Exception as e:
        print(f"Ocorreu um erro ao verificar o produto: {e}")
            