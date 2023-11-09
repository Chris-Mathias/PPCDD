import pandas as pd

prodtxt = open("/media/chris/SSD/Documentos/Python/PPCDD/Aula 08.31/produtos.txt", "r") # substitua o caminho pelo desejado

vendatxt = open("/media/chris/SSD/Documentos/Python/PPCDD/Aula 08.31/venda.txt", "w") # substitua o caminho pelo desejado

prod = (str(prodtxt.read()).split("\n"))

produtos = []
codigo = []

for x in prod:
    s = x.split(",")
    s[0] = int(s[0])
    s[2] = float(s[2])
    produtos.append(s)
    codigo.append(s[0])

venda = []
novaVenda = ""
novoProduto = ""

vendatxt.write("\n    Venda Finalizada\n\n")

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

vendatxt.write(str(pd.DataFrame(venda, columns = ["Código", "Produto", "Valor Unitário", "Quantidade", "Valor Total"])))

print("\nValor total da venda: %.2f\n" % (valor))

valortxt = "%.2f" % (valor)

vendatxt.write("\n\n    Valor total da venda: ")
vendatxt.write(valortxt)
