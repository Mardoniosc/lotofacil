# coding: utf-8
numeros_sorteador = [2,3,4,5,6,9,10,12,14,15,17,19,22,23,25]

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


                if acertos == 15:
                    print("Resultado do %d° jogo acertou %d" % (jogo,acertos))    
                    ganhos = ganhos + 1124060
                elif acertos == 14:
                    print("Resultado do %d° jogo acertou %d" % (jogo,acertos))
                    ganhos = ganhos + 1500
                elif acertos == 13:
                    print("Resultado do %d° jogo acertou %d" % (jogo,acertos))
                    ganhos = ganhos + 25
                elif acertos == 12:
                    print("Resultado do %d° jogo acertou %d" % (jogo,acertos))
                    ganhos = ganhos + 10
                elif acertos == 11:
                    print("Resultado do %d° jogo acertou %d" % (jogo,acertos))
                    ganhos = ganhos + 5

                jogo +=1
print("\n\nGanho total aproximado é de R$ %.2f" % ganhos, "Reais")
