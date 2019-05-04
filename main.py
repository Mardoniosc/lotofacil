# coding: utf-8
from apostar_ou_nao import verifica_se_pode_marcar
numeros_sorteador = [1,4,6,7,10,12,13,16,17,18,19,20,22,23,24]
j1c1 = [1,3,4,5,6,7,8,12,13,14,18,19,20,23,24]
j2c1 = [2,3,5,6,7,9,10,11,12,13,14,15,19,21,24]
j3c1 = [2,4,5,6,7,9,12,13,14,18,20,21,22,23,24]
j1c2 = [1,2,5,6,9,10,12,13,14,15,19,20,21,24,25]
j2c2 = [1,2,3,5,7,12,13,14,16,18,19,20,21,22,23]
j3c2 = [2,4,6,7,9,10,11,12,13,14,17,19,20,21,25]
j1c3 = [1,3,4,5,6,7,9,12,13,15,17,19,20,21,22]
j2c3 = [1,3,4,5,6,7,8,10,12,14,18,19,20,21,23]
j3c3 = [2,3,5,6,7,8,11,13,14,15,16,19,20,21,22]

def resultado_lista_inteiro(resultado):
    resultado = resultado[18:]
    resultado = resultado.replace(' ', ',')
    resultado = resultado[1:].replace(',0', ',')
    resultado = list(map(int, resultado.split(",")))

    return resultado

def compara_resultado(resultado, x):
    resultado_ = set(resultado).intersection(x)
    acertos = len(resultado_)

    return acertos

jogos = [j1c1, j2c1, j3c1, j1c2, j2c2, j3c2, j1c3, j2c3, j3c3]

ganhos = 0
jogo = 1
for x in jogos:

    

    # print(verifica_se_pode_marcar(x))

    acertos = compara_resultado(numeros_sorteador,x)
    print("Resultado do %d° jogo acertou %d" % (jogo,acertos))

    if acertos == 15:
        print("GANHOU GANHOU GANHOU MIZERAVEL")
        ganhos = ganhos + 1124060
    elif acertos == 14:
        print("Eita! \n Foi quase essa mizera!")
        ganhos = ganhos + 1700
    elif acertos == 13:
        print('Pelo menos não perdi dinheiro nessa!! :(')
        ganhos = ganhos + 20
    elif acertos == 12:
        print("Talvez de de cobrir os gastos")
        ganhos = ganhos + 8
    elif acertos == 11:
        print("Pelo menos não fiquei sem ganhar nada!!")
        ganhos = ganhos + 4
    else:
        print("Caraca Não ganhei nada nessa parada!!")

    jogo +=1
print("\n\nGanho total aproximado é de R$ %.2f" % ganhos, "Reais")
