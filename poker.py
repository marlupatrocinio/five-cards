import random

def criarBaralho():
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    naipes = ['♠', '♥', '♦', '♣']
    baralho = []
    for naipe in naipes:
        for valor in valores:
            baralho.append(valor + naipe)
    return baralho

def embaralharBaralho(baralho):
    random.shuffle(baralho)
    return baralho

# Crie o baralho
baralho = criarBaralho()
# Embaralhe o baralho
baralhoEmbaralhado = embaralharBaralho(baralho)

def distribuirCartas(baralho):
    return [baralho.pop() for _ in range(5)]

def valorCarta(carta):
    valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return valores[carta[:-1]]

def naipeCarta(carta):
    return carta[-1]

def avaliarMao(mao):
    valores = [valorCarta(carta) for carta in mao]
    naipes = [naipeCarta(carta) for carta in mao]
    valores_contagem = {}
    naipes_contagem = {}

    for valor in valores:
        valores_contagem[valor] = valores_contagem.get(valor, 0) + 1

    for naipe in naipes:
        naipes_contagem[naipe] = naipes_contagem.get(naipe, 0) + 1

    # Organiza os valores para verificar sequência
    valores_ordenados = sorted(set(valores))
    is_sequencia = len(valores_ordenados) == 5 and valores_ordenados[-1] - valores_ordenados[0] == 4
    is_flush = max(naipes_contagem.values()) == 5

    # Verifica Royal Flush e Straight Flush
    if is_sequencia and is_flush:
        if valores_ordenados[0] == 10:
            return "Royal Flush", mao

        return "Straight Flush", mao


    # Verifica Quadra e Full House
    if 4 in valores_contagem.values():
        return "Quadra", mao
    
    if 3 in valores_contagem.values() and 2 in valores_contagem.values():
        return "Full House", mao


    # Verifica Flush e Sequência
    if is_flush:
        return "Flush", mao

    if is_sequencia:
        return "Sequencia", mao


    # Verifica Trinca, Dois Pares e Par
    if 3 in valores_contagem.values():
        return "Trinca", mao

    if list(valores_contagem.values()).count(2) == 2:
        return "Dois Pares", mao

    if 2 in valores_contagem.values():
        return "Par", mao


    return "Carta Alta", mao

baralho = criarBaralho()
print("Baralho Criado:", baralho)

# Embaralhe o baralho
baralhoEmbaralhado = embaralharBaralho(baralho)
print("Baralho Embaralhado:", baralhoEmbaralhado)

# Distribua as cartas
mao = distribuirCartas(baralhoEmbaralhado)
print("Mão Distribuída:", mao)

# Avalie a mão
avaliacao = avaliarMao(mao)
print("Avaliação da Mão:", avaliacao)
