# A expressão que calcula a velocidade média de um móvel é: distancia percorrida/tempo em que a distancia foi percorrida
# nesse scrpit o objetivo é realizar essa operação de maneira automatizada, precisando apenas que o usuário
# dê os valores que deseja utilizar na fórmula!


def calcular(distancia, tempo):
    return distancia / tempo


if __name__ == '__main__':
    velocidade = calcular(
        int(input("Digite a distancia percorrida: ")),
        int(input("Digite em quantas horas a distância foi percorrida: "))
    )

    print(F"A velocidade média é de {velocidade} km/h")
