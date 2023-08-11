numPedidos = []
comida = []
calorias = []
quantPedidos = int(input())
nomeComida = input()
pratoCalorias = int(input())
numPedidos.append(quantPedidos)
comida.append(nomeComida)
calorias.append(pratoCalorias)
for i in range(1, quantPedidos + 1):
    print(f"Pedido {i}: {nomeComida} {pratoCalorias} calorias")

