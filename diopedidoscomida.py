quantidadePedidos = int(input())
n = 1
valorFinal = 0
valorTotal = 0
while n <= quantidadePedidos:
    nomePedido = input()
    valorPedido = float(input())
    valorFinal = valorPedido + valorFinal
    n = n + 1
cupomEscolhido = input()
if cupomEscolhido == "10%":
    valorTotal = valorFinal - (valorFinal / 10)
elif cupomEscolhido == "20%":
    valorTotal = valorFinal - ((valorFinal / 10)*2)
print(f"Valor total: {valorTotal:.2f}")