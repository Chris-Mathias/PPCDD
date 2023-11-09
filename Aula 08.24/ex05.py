import pandas as pd

produtos = [[101, "Arroz", 20.99],
            [102, "Feijão", 11.99],
            [103, "Sal", 1.99],
            [104, "Açúcar", 16.99],
            [105, "Farinha", 19.99]]
codigo = [101, 102, 103, 104, 105]
venda = []
novaVenda = ""
novoProduto = ""

while novaVenda != "n":

    print("\nProdutos disponíveis:\n")
    print(pd.DataFrame(produtos, columns = ["Código", "Produto", "Valor"]))    

    while novoProduto != "n":

        produto = int(input("\nInsira o código de um produto: "))
        while produto not in codigo:
            print("Produto inválido")
            produto = int(input("Insira o código de um produto: "))
        
        quantidade = int(input("Insira a quantidade: "))
        idx = codigo.index(produto)

        venda.append([produto, produtos[idx][1], produtos[idx][2], quantidade, (produtos[idx][2])*quantidade])

        novoProduto = input("Produto inserido na venda, deseja continuar: (S/n) ").lower()

    valor = 0

    for i in venda:
        valor += i[4]

    print("\nVenda finalizada\n")
    
    print(pd.DataFrame(venda, columns = ["Código", "Produto", "Valor Unitário", "Quantidade", "Valor Total"]))

    print("\nValor total da compra: %.2f\n" % (valor))

    venda = []
    novoProduto = ""

    novaVenda = input("Venda finalizada, deseja continuar? (S/n) ").lower()
