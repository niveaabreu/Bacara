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
        ficha3=100
        print("   ")
        print(jogador3,",", "você tem 100 fichas!")

    else :
        print(" ")

    #Definindo número de baralhos
    print("   ")
    baralhos=int(input("Quantos baralhos utilizar? 1, 6 ou 8? "))
    if  baralhos!=1 or baralhos!=6 or baralhos!=8:
        print("jogador tente outra vez")
    else:
        print("Vamos")


    
    
    #Randomizando cartas
    import random
    from random import randint
    Às = 1
    Q = 0
    J = 0
    K = 0
    cartas = [Às,2,3,4,5,6,7,8,9,10,Q,J,K,Às,2,3,4,5,6,7,8,9,10,Q,J,K,Às,2,3,4,5,6,7,8,9,10,Q,J,K,Às,2,3,4,5,6,7,8,9,10,Q,J,K]
           
    if baralhos == 1:
        random.shuffle(cartas)
            
    elif baralhos == 6 :
        cartas = cartas*6
        random.shuffle(cartas)
            
    elif baralhos == 8 :
        cartas = cartas*6
        random.shuffle(cartas)

    print("   ")
    print("Embaralhando cartas...")
    print("   ")
    print("Vamos às apostas?!")
    print("   ")
    

    #Apostas dos jogadores
    if jogadores == 1:
        aposta_jog1 = int(input("Quanto quer apostar, {0}? ".format(jogador1)))
        while aposta_jog1>ficha1:
            print("Você não possui fichas suficientes. Seu saldo é de {0} fichas".format(ficha1))
            aposta_jog1 = int(input("Quanto quer apostar, {0}? ".format(jogador1)))
        pers_apost_jog1 = input("Em quem vai apostar? Digite 0 para jogador, 1 para banco ou 2 para empate: ")

    
    elif jogadores == 2: