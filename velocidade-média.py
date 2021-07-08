#A expressão que calcula a velocidade média de um móvel é:  distancia percorrida/tempo em que a distancia foi percorrida
#nesse scrpit o objetivo é realizar essa operação de maneira automatizada, precisando apenas que o usuário 
#dê os valores que deseja utilizar na fórmula! 



distancia=int(input("Digite a distancia percorrida:"))
tempo=int(input("Digite em quantas horas a distância foi percorrida:"))
velocidade= distancia / tempo
print("A velocidade é igual a:")
print(velocidade)
