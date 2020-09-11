# coding: utf-8
numeros_sorteador = [1,4,6,7,10,12,13,16,17,18,19,20,22,23,24]

def resultado_lista_inteiro(resultado):
    resultado = resultado.replace(' ', ',')
    resultado = resultado[1:].replace(',0', ',')
    resultado = list(map(int, resultado.split(",")))

    return resultado

def compara_resultado(resultado, x):
    resultado_ = set(resultado).intersection(x)
    acertos = len(resultado_)

    return acertos

ganhos = 0
jogo = 1
with open('jogos.txt', 'r') as fd:
        for x in fd:
            if x != '' and x != "\n":
                y = (resultado_lista_inteiro(x))
                acertos = compara_resultado(numeros_sorteador, y)

                print("Resultado do %d° jogo acertou %d" % (jogo,acertos))

                if acertos == 15:
                    print("GANHOU GANHOU GANHOU MIZERAVEL")
                    ganhos = ganhos + 1124060
                elif acertos == 14:
                    print("Eita! \n Foi quase essa mizera!")
                    ganhos = ganhos + 1500
                elif acertos == 13:
                    print('Pelo menos não perdi dinheiro nessa!! :(')
                    ganhos = ganhos + 25
                elif acertos == 12:
                    print("Talvez de de cobrir os gastos")
                    ganhos = ganhos + 10
                elif acertos == 11:
                    print("Pelo menos não fiquei sem ganhar nada!!")
                    ganhos = ganhos + 5

                jogo +=1
print("\n\nGanho total aproximado é de R$ %.2f" % ganhos, "Reais")
