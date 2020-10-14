#EP - Design Software
#Dupla: Breno Alencar e Nívea Abreu
#Data:

#Bacará

print("            ")
print("Bacará V0.01")
print("                                          ___")
print(" ____                                    /__/")
print("| __ )    __ _    ___    __ _   _ __    __ _ ") 
print("|  _ \   / _` |  / __|  / _` | | '__|  / _` |")
print("| |_) | | (_| | | (__  | (_| | | |    | (_| |")
print("|____/   \__,_|  \___|  \__,_| |_|     \__,_|")

#Recolhendo dados dos jogadores
print("   ")
print("Bem-vindo(a) ao Bacará!")
print("   ")

#Dados jogador 1
jogador1=input("Qual o seu nome? ")
print("   ")
print(jogador1,",", "você tem 100 fichas!")
#Fichas iniciais
ficha1=100
print("   ")

#Definindo outros jogadores
jogadores=int(input("Quantos jogadores na partida? Máximo de 3 jogadores. "))

if jogadores == 0:
    print("   ")
    print ("Até logo!")
else :
    while jogadores <= 0 or jogadores > 3:
        print("Digite 1, 2 ou 3 jogadores")
        jogadores=int(input("Quantos jogadores na partida? Máximo de 3 jogadores : "))

    if jogadores == 2 :
        print("   ")
        jogador2=input("Qual o seu nome, jogador 2? ")
        print("   ")
        ficha2=100
        print(jogador2,",", "você tem 100 fichas!")

    elif jogadores == 3 :
        print("   ")
        jogador2=input("Qual o seu nome, jogador 2? ")
        print("   ")
        ficha2=100
        print(jogador2,",", "você tem 100 fichas!")

        jogador3=input("Qual o seu nome, jogador 3? ")