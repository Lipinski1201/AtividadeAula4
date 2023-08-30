def calcular_posicao_final(comandos):
    posicao = 0
    
    for comando in comandos:
        if comando == "Direita":
            posicao += 1
        elif comando == "Esquerda":
            posicao -= 1
    
    return posicao

# Exemplos de uso
comandos1 = ["Direita", "Direita"]
print("Posição Inicial: 0, Posição Final:", calcular_posicao_final(comandos1))

comandos2 = ["Esquerda"]
print("Posição Inicial: 0, Posição Final:", calcular_posicao_final(comandos2))

comandos3 = ["Esquerda", "Direita", "Direita", "Direita", "Direita", "Esquerda"]
print("Posição Inicial: 0, Posição Final:", calcular_posicao_final(comandos3))