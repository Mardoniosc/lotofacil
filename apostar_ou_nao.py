# coding: utf-8

def resultado_lista_inteiro(resultado):
    resultado = resultado[18:]
    resultado = resultado.replace(' ', ',')
    resultado = resultado[1:].replace(',0', ',')
    resultado = list(map(int, resultado.split(",")))

    return resultado

def compara_resultado(resultado, y):
    resultado_ = set(resultado).intersection(y)
    acertos = len(resultado_)

    return acertos

def verifica_se_pode_marcar(jogo):

    with open('resultados_lotofacil.txt', 'r') as fd:

        for x in fd:
            if x != '' and x != "\n":
                y = (resultado_lista_inteiro(x))
                acerto = compara_resultado(y,jogo)
                if acerto == 15:
                    return True
                else:
                    return False