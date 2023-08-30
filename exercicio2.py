"""  Histórias de Usuário Modificadas:
História de Usuário para Trilho Infinito:

Como usuário, quero dar uma lista de comandos ao trem para movê-lo em um trilho numérico infinito.
O trem começa na posição 0.
Os comandos disponíveis são "Esquerda" e "Direita".
Quero saber a posição final do trem após executar os comandos.
História de Usuário para Trilho Finito:

Como usuário, quero dar uma lista de comandos ao trem para movê-lo em um trilho numérico finito, variando de -2 a +10.
O trem começa na posição 0 dentro desse intervalo.
Os comandos disponíveis são "Esquerda" e "Direita".
O trem nunca deve sair dos limites do trilho (entre -2 e +10).
Quero saber a posição final do trem após executar os comandos, considerando os limites do trilho. 
""" 

def calcular_posicao_final(comandos, trilho_infinito=False):
    posicao = 0
    
    for comando in comandos:
        if comando == "Direita":
            posicao += 1
        elif comando == "Esquerda":
            posicao -= 1
        
        if not trilho_infinito:
            posicao = max(-2, min(posicao, 10))
    
    return posicao

# Exemplos de uso para trilho infinito
comandos_infinito = ["Direita", "Esquerda", "Direita"]
print("Trilho Infinito - Posição Inicial: 0, Posição Final:", calcular_posicao_final(comandos_infinito, trilho_infinito=True))

# Exemplos de uso para trilho finito
comandos_finito = ["Direita", "Direita", "Direita", "Esquerda"]
print("Trilho Finito - Posição Inicial: 0, Posição Final:", calcular_posicao_final(comandos_finito))