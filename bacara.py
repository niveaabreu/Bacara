#EP - Design de Software
#Dupla: Breno Alencar e Nívea Abreu
#Data:17/10/2020

#Favor instalar o módulo 'pygame' (pip install pygame) para maior imersão. Do contrário, favor remover as 5 linhas seguintes.

from pygame import mixer 
mixer.init()
mixer.music.load('bttbsv.mp3')
mixer.music.play()

#Todos os direitos reservados a George Thorogood pela música "Back To The Bone" utilizada neste jogo.


#Bacará

#Em caso do erro 'list index out of range', favor executá-lo novamente.

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
print("   ")
print("Para sua maior diversão, ainda será possível jogar mesmo sem fichas, para isso, bastar digitar 0 fichas!\nBom divertimento!")

#Fichas iniciais dos jogadores (mesmo que esses não participem)
ficha1=100
ficha2=100
ficha3=100
print("   ")

#Definindo outros jogadores (1ª regra avançada implementada)
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
        print("  ")

    elif jogadores == 3 :
        print("   ")
        jogador2=input("Qual o seu nome, jogador 2? ")
        print("   ")
        ficha2=100
        print(jogador2,",", "você tem 100 fichas!")
        print("  ")

        jogador3=input("Qual o seu nome, jogador 3? ")
        ficha3=100
        print("   ")
        print(jogador3,",", "você tem 100 fichas!")

    else :
        print(" ")

    #Definindo número de baralhos (2ª regra avançada implementada)
    
    baralhos=int(input("Digite o número de baralhos a serem utilizados (1, 6 ou 8): "))
    while (int(baralhos)!=1 and int(baralhos)!=6 and int(baralhos)!=8):
        print("Digite um dos valores válidos")
        baralhos=int(input("Digite o número de baralhos a serem utilizados (1, 6 ou 8): "))
        
    #Randomizando cartas
    import random
    from random import randint
    Às = 1
    Q = 0
    J = 0
    K = 0
    cartas = [Às,2,3,4,5,6,7,8,9,10,Q,J,K,Às,2,3,4,5,6,7,8,9,10,Q,J,K,Às,2,3,4,5,6,7,8,9,10,Q,J,K,Às,2,3,4,5,6,7,8,9,10,Q,J,K]

    #Multiplicando, caso necessário, a lista de cartas e embaralhando-as       
    if baralhos == 1:
        random.shuffle(cartas)
            
    elif baralhos == 6 :
        cartas = cartas*6
        random.shuffle(cartas)
            
    elif baralhos == 8 :
        cartas = cartas*8
        random.shuffle(cartas)

    print("   ")
    print("Embaralhando cartas...")
    print("   ")
    print("Vamos às apostas?!")
    print("   ")
    

    #Apostas dos jogadores
    #O loop inicia-se aqui.
    #As demais estruturas baseiam-se na simples repetição dos blocos e apenas adicionando ou removendo seções
    # de acordo com o número de fichas restantes de cada jogador.
    # Mais uma vez, caso não deseje apostar, apenas apostar 0 fichas. 
    
    while ficha1!=0 or ficha2!=0 or ficha3!=0:
        if ficha1!=0:
            if jogadores == 1:
                aposta_jog1 = int(input("Quanto quer apostar, {0}? ".format(jogador1)))
                while aposta_jog1>ficha1:
                    print("Você não possui fichas suficientes. Seu saldo é de {0} fichas".format(ficha1))
                    aposta_jog1 = int(input("Quanto quer apostar, {0}? ".format(jogador1)))
                pers_apost_jog1 = int(input("Em quem vai apostar? Digite 0 para jogador, 1 para banco ou 2 para empate: "))
                while int(pers_apost_jog1)!=0 and int(pers_apost_jog1) != 1 and int(pers_apost_jog1)!=2:
                    pers_apost_jog1 = int(input("Valor inválido. Em quem vai apostar? Digite 0 para jogador, 1 para banco ou 2 para empate: "))   

        
        if jogadores == 2:
            if ficha1!=0:
                aposta_jog1 = int(input("Quanto quer apostar, {0}? ".format(jogador1)))
                while aposta_jog1>ficha1:
                    print("Você não possui fichas suficientes. Seu saldo é de {0} fichas".format(ficha1))
                    aposta_jog1 = int(input("Quanto quer apostar, {0}? ".format(jogador1)))
                pers_apost_jog1 = int(input("Em quem vai apostar? Digite 0 para jogador, 1 para banco ou 2 para empate: "))
                while int(pers_apost_jog1)!=0 and int(pers_apost_jog1) != 1 and int(pers_apost_jog1)!=2:
                    pers_apost_jog1 = int(input("Valor inválido. Em quem vai apostar? Digite 0 para jogador, 1 para banco ou 2 para empate: "))
            
            else:
                print("Sem mais fichas, ", jogador1)
            
            if ficha2!=0:    
                aposta_jog2 = int(input("Quanto quer apostar, {0}? ".format(jogador2)))
                while aposta_jog2>ficha2:
                    print("Você não possui fichas suficientes. Seu saldo é de {0} fichas".format(ficha2))
                    aposta_jog2 = int(input("Quanto quer apostar, {0}? ".format(jogador2)))
                pers_apost_jog2 = int(input("Em quem vai apostar? Digite 0 para jogador, 1 para banco ou 2 para empate: "))
                while int(pers_apost_jog2)!=0 and int(pers_apost_jog2) != 1 and int(pers_apost_jog2)!=2:
                    pers_apost_jog2 = int(input("Valor inválido. Em quem vai apostar? Digite 0 para jogador, 1 para banco ou 2 para empate: "))

            else:
                print("Sem mais fichas, ", jogador2)

        if jogadores == 3:
            if ficha1!=0:
                aposta_jog1 = int(input("Quanto quer apostar, {0}? ".format(jogador1)))
                while aposta_jog1>ficha1:
                    print("Você não possui fichas suficientes. Seu saldo é de {0} fichas".format(ficha1))
                    aposta_jog1 = int(input("Quanto quer apostar, {0}? ".format(jogador1)))
                pers_apost_jog1 = int(input("Em quem vai apostar? Digite 0 para jogador, 1 para banco ou 2 para empate: "))
                while int(pers_apost_jog1)!=0 and int(pers_apost_jog1) != 1 and int(pers_apost_jog1)!=2:
                    pers_apost_jog1 = int(input("Valor inválido. Em quem vai apostar? Digite 0 para jogador, 1 para banco ou 2 para empate: "))

            else:
                print("Sem mais fichas, ", jogador1)
            
            print ("  ")
            
            if ficha2!=0:
                aposta_jog2 = int(input("Quanto quer apostar, {0}? ".format(jogador2)))
                while aposta_jog2>ficha2:
                    print("Você não possui fichas suficientes. Seu saldo é de {0} fichas".format(ficha2))
                    aposta_jog2 = int(input("Quanto quer apostar, {0}? ".format(jogador2)))
                pers_apost_jog2 = int(input("Em quem vai apostar? Digite 0 para jogador, 1 para banco ou 2 para empate: "))
                while int(pers_apost_jog2)!=0 and int(pers_apost_jog2) != 1 and int(pers_apost_jog2)!=2:
                    pers_apost_jog2 = int(input("Valor inválido. Em quem vai apostar? Digite 0 para jogador, 1 para banco ou 2 para empate: "))

            else:
                print("Sem mais fichas, ", jogador2)    
            print ("  ")
            
            if ficha3!=0:
                aposta_jog3 = int(input("Quanto quer apostar, {0}? ".format(jogador3)))
                while aposta_jog3>ficha3:
                    print("Você não possui fichas suficientes. Seu saldo é de {0} fichas".format(ficha3))
                    aposta_jog3 = int(input("Quanto quer apostar, {0}? ".format(jogador3)))
                pers_apost_jog3 = int(input("Em quem vai apostar? Digite 0 para jogador, 1 para banco ou 2 para empate: "))
                while int(pers_apost_jog3)!=0 and int(pers_apost_jog3) != 1 and int(pers_apost_jog3)!=2:
                    pers_apost_jog3 = int(input("Valor inválido. Em quem vai apostar? Digite 0 para jogador, 1 para banco ou 2 para empate: "))

            else:
                print("Sem mais fichas, ", jogador3)
        else :
            print ("  ")

        #Distribuindo cartas para os jogadores
        #A contrução desta parte pode variar entre formas de jogar. Neste caso, o jogador tem sua carta sorteada
        # e, logo em seguida, a segunda carta é sorteada sem a presença da primeira.
        # Após isso, a primeira carta é reinserida ao baralho e o sorteio acontece para os outros jogadores (caso existam). 
        # Outras formas de sorteio podem ser contempladas.
        #Para melhor acompanhamento do sorteio, optamos por dar um tempo entre a apresentação de carta sorteada.
        #Optamos por sortear cartas diferentes para jogadores diferentes.
        #A seção novamente foi construida com repetições.
        import time
        time.sleep(0.3)
        print ("  ")
        c1=randint(0,len(cartas))
        if jogadores == 1 :
            if ficha1!=0:
                cartas1_1 = cartas [c1]
                print ("Primeira carta de {0}: ".format(jogador1),cartas1_1)
                del cartas [c1]
                c2=randint(0,len(cartas))
                cartas1_2 = cartas [c2]
                time.sleep(0.7)
                print("Segunda carta de {0}: ".format(jogador1), cartas1_2)
                cartas.append(cartas[c1])         
                random.shuffle(cartas)
                print("  ")    
        
        elif jogadores == 2:
            if ficha1!=0:
                cartas1_1 = cartas [c1]
                time.sleep(0.7)
                print ("Primeira carta de {0}: ".format(jogador1),cartas1_1)
                del cartas [c1]
                c2=randint(0,len(cartas))
                cartas1_2 = cartas [c2]
                time.sleep(0.7)
                print("Segunda carta de {0}: ".format(jogador1), cartas1_2)
                cartas.append(cartas[c1])         
                random.shuffle(cartas)
                print("  ")

            if ficha2!=0:
                c3=randint(0,len(cartas))
                cartas2_1=cartas[c3]
                time.sleep(0.7)
                print ("Primeira carta de {0}: ".format(jogador2),cartas2_1)
                del cartas[c3]
                c4=randint(0,len(cartas))
                cartas2_2=cartas[c4]
                time.sleep(0.7)
                print("Segunda carta de {0}: ".format(jogador2), cartas2_2)
                cartas.append(cartas[c3])
                random.shuffle(cartas)
                print("  ")
        
        
        elif jogadores ==3:
            if ficha1!=0:
                cartas1_1= cartas [c1]
                time.sleep(0.7)
                print ("Primeira carta de {0}: ".format(jogador1),cartas1_1)
                del cartas [c1]
                c2=randint(0,len(cartas))
                cartas1_2=cartas[c2]
                time.sleep(0.7)
                print("Segunda carta de {0}: ".format(jogador1), cartas1_2)
                cartas.append(cartas[c1])
                random.shuffle(cartas)
                print("  ")

            if ficha2!=0:
                c3=randint(0,len(cartas))
                cartas2_1=cartas[c3]
                time.sleep(0.7)
                print ("Primeira carta de {0}: ".format(jogador2),cartas2_1)
                del cartas[c3]
                c4=randint(0,len(cartas))
                cartas2_2=cartas[c4]
                time.sleep(0.7)
                print("Segunda carta de {0}: ".format(jogador2), cartas2_2)
                cartas.append(cartas[c3])
                random.shuffle(cartas)
                print("  ")

            if ficha3!=0:
                c5=randint(0,len(cartas))
                cartas3_1=cartas[c5]
                time.sleep(0.7)
                print ("Primeira carta de {0}: ".format(jogador3),cartas3_1)
                del cartas[c5]
                c6=randint(0,len(cartas))
                cartas3_2=cartas[c6]
                time.sleep(0.7)
                print("Segunda carta de {0}: ".format(jogador3), cartas3_2)
                cartas.append(cartas[c5])
                random.shuffle(cartas)
                print("  ")
        else:
            print("  ")
        
        #Distribuição das cartas do banco (independe da carta dos jogadores neste jogo)
        print("  ")
        cb = randint(0,len(cartas))
        cartasb1 = cartas[cb]
        time.sleep(0.7)
        print("Primeira carta do banco: ", cartasb1)
        del cartas[cb]
        cb2 = randint(0,len(cartas))
        cartasb2 = cartas[cb2]
        time.sleep(0.7)
        print("Segunda carta do banco: ", cartasb2)
        cartas.append(cartas[cb])
        random.shuffle(cartas)
        print("  ")

        #soma das cartas e em caso de valores maiores que 10 ou 20, contabilizamos apenas a unidade
        if jogadores == 1:
            if ficha1!=0:
                soma1=cartas1_1+cartas1_2
                if soma1>=10 :
                    soma1= soma1-10
                if soma1>=20:
                    soma1=soma1-20
                time.sleep(0.7)
                print ("Soma de {0}: ".format(jogador1), soma1)
            
        elif jogadores == 2:
            if ficha1!=0:
                soma1=cartas1_1+cartas1_2
                if soma1>=10 :
                    soma1= soma1-10
                if soma1>=20:
                    soma1=soma1-20
                time.sleep(0.7)
                print ("Soma de {0}: ".format(jogador1), soma1)

            if ficha2!=0:
                soma2 = cartas2_1 + cartas2_2
                if soma2>=10:
                    soma2=soma2-10
                if soma2>=20:
                    soma2=soma2-20
                time.sleep(0.7)
                print ("Soma de {0}: ".format(jogador2), soma2)
            
        
        elif jogadores == 3:
            if ficha1!=0:
                soma1=cartas1_1+cartas1_2
                if soma1>=10 :
                    soma1= soma1-10
                if soma1>=20:
                    soma1=soma1-20
                time.sleep(0.7)
                print ("Soma de {0}: ".format(jogador1), soma1)

            if ficha2!=0:
                soma2=cartas2_1+cartas2_2
                if soma2>=10:
                    soma2=soma2-10
                if soma2>=20:
                    somab2=soma2-20
                time.sleep(0.7)
                print ("Soma de {0}: ".format(jogador2), soma2)
            
            if ficha3!=0:
                soma3=cartas3_1+cartas3_2
                if soma3>=10:
                    soma3=soma3-10
                if soma3>=20:
                    soma3=soma3-20
                time.sleep(0.7)
                print ("Soma de {0}: ".format(jogador3), soma3)
        
        #Soma banco
        somab=cartasb1+cartasb2
        if somab>=10:
            somab=somab-10
        if somab>=20:
            somab=somab-20
        time.sleep(0.7)
        print ("Soma do banco: ", somab)
        print("  ")

        #Regras de distribuição da terceira carta (jogador e banco)
        if ficha1!=0:
            if soma1<=5:
                time.sleep(0.7)
                print("{0}, você tem direito a mais uma carta!".format(jogador1))
                print("  ")
                c7=randint(0,len(cartas))
                cartas1_3= cartas [c7]
                time.sleep(0.7)
                print("Terceira carta de {0}: ".format(jogador1), cartas1_3)
                soma1=soma1+cartas1_3
                if soma1>=10:
                    soma1=soma1-10
                if soma1>=20:
                    soma1=soma1-20
                time.sleep(0.7)
                print("Soma final de {0}: ".format(jogador1),soma1)
                print("  ")
        
        if ficha2!=0:
            if jogadores==2:
                if soma2<=5:
                    time.sleep(0.7)
                    print("{0}, você tem direito a mais uma carta!".format(jogador2))
                    print("  ")
                    c8=randint(0,len(cartas))
                    cartas2_3= cartas [c8]
                    time.sleep(0.7)
                    print("Terceira carta de {0}: ".format(jogador2), cartas2_3)
                    soma2=soma2+cartas2_3
                    if soma2>=10:
                        soma2=soma2-10
                    if soma2>=20:
                        soma2=soma2-20
                    time.sleep(0.7)
                    print("Soma final de {0}: ".format(jogador2),soma2)
        
        if jogadores==3:
            if ficha2!=0:
                if soma2<=5:
                    time.sleep(0.7)
                    print("{0}, você tem direito a mais uma carta!".format(jogador2))
                    print("  ")
                    c8=randint(0,len(cartas))
                    cartas2_3= cartas [c8]
                    time.sleep(0.7)
                    print("Terceira carta de {0}: ".format(jogador2), cartas2_3)
                    soma2=soma2+cartas2_3
                    if soma2>=10:
                        soma2=soma2-10
                    if soma2>=20:
                        soma2=soma2-20
                    time.sleep(0.7)
                    print("Soma final de {0}: ".format(jogador2),soma2)
                    print("  ")

            if ficha3!=0:
                if soma3<=5:
                    time.sleep(0.7)
                    print("{0}, você tem direito a mais uma carta!".format(jogador3))
                    print("  ")
                    c9=randint(0,len(cartas))
                    cartas3_3= cartas [c9]
                    time.sleep(0.7)
                    print("Terceira carta de {0}: ".format(jogador3), cartas3_3)
                    soma3=soma3+cartas3_3
                    if soma3>=10:
                        soma3=soma3-10
                    if soma3>=20:
                        soma3=soma3-20
                    time.sleep(0.7)
                    print("Soma final de {0}: ".format(jogador3),soma3)
                    print("  ")
            
        
        
        if somab<=5:
            time.sleep(0.5)
            print("O banco tem direito a mais uma carta!")
            print("  ")
            c10=randint(0,len(cartas))
            cartasb_3= cartas [c10]
            time.sleep(0.5)
            print("Terceira carta do banco : ",cartasb_3)
            somab=somab+cartasb_3
            if somab>=10:
                somab=somab-10
            if somab>=20:
                somab=somab-20
            time.sleep(0.5)
            print("Soma final do banco: ",somab)
        
        #Comparando valores das cartas
        #Cada porcentagem de comissão já está inserida em cada possibilidade de resultado. Ver "fichax=..." (3ª regra avançada implementada)
        #As taxas de comissão não foram anunciadas como variáveis globais para dificultar possíveis alterações.
        #Ao término da linha 878, o jogo retorna para a linha 122 e segue ou não.
        print("  ")
        #Para 1 jogador
        if jogadores == 1:
            if ficha1!=0:
                if soma1<somab :
                    if pers_apost_jog1 == 0:
                        ficha1=ficha1-aposta_jog1
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))
                    
                    elif pers_apost_jog1 == 1:
                        if baralhos == 1:
                            ficha1=int(ficha1+0.95*aposta_jog1-(1.01/100)*0.95*aposta_jog1)
                            print("{0}, você venceu! Fichas: {1}".format(jogador1,ficha1))
                        if baralhos == 6 :
                            ficha1=int(ficha1+0.95*aposta_jog1-(1.06/100)*0.95*aposta_jog1)
                            print("{0}, você venceu! Fichas: {1}".format(jogador1,ficha1))
                        if baralhos == 8:
                            ficha1=int(ficha1+0.95*aposta_jog1-(1.06/100)*0.95*aposta_jog1)
                            print("{0}, você venceu! Fichas: {1}".format(jogador1,ficha1))
                        

                    if pers_apost_jog1 == 2:
                        ficha1=ficha1-aposta_jog1
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}" .format(jogador1,ficha1))

                if soma1==somab:
                    if pers_apost_jog1 == 0:
                        ficha1=ficha1-aposta_jog1
                        print("Empate! {0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1, ficha1))

                    elif pers_apost_jog1 == 1:
                        ficha1=ficha1-aposta_jog1
                        print("Empate! {0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))

                    elif pers_apost_jog1 == 2:
                        if baralhos == 1:
                            ficha1=int(ficha1+8*aposta_jog1-(15.75/100)*8*aposta_jog1)
                            print("Empate! {0}, você venceu! Fichas: {1}".format(jogador1,ficha1))

                        elif baralhos == 6:
                            ficha1=int(ficha1+8*aposta_jog1-(14.44/100)*8*aposta_jog1)
                            print("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))
                        
                        elif baralhos == 8:
                            ficha1=int(ficha1+8*aposta_jog1-(14.36/100)*8*aposta_jog1)
                            print("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))

                if soma1> somab:
                    if pers_apost_jog1==0:
                        if baralhos == 1:
                            ficha1=int(ficha1+aposta_jog1-(1.29/100)*aposta_jog1)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))

                        if baralhos == 6:
                            ficha1=int(ficha1+aposta_jog1-(1.24/100)*aposta_jog1)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))

                        if baralhos == 8:
                            ficha1=int(ficha1+aposta_jog1-(1.24/100)*aposta_jog1)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))
                        
                    
                    elif pers_apost_jog1 == 1:
                        ficha1=ficha1-aposta_jog1
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))

                    elif pers_apost_jog1 == 2:
                        ficha1=ficha1-aposta_jog1
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))
        
        #Para 2 jogadores
        if jogadores == 2:
            if ficha1!=0:
                if soma1<somab :
                    if pers_apost_jog1 == 0:
                        ficha1=ficha1-aposta_jog1
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))
                    
                    if pers_apost_jog1 == 1:
                        if baralhos == 1:
                            ficha1=int(ficha1+0.95*aposta_jog1-(1.01/100)*0.95*aposta_jog1)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))

                        if baralhos == 6:
                            ficha1=int(ficha1+0.95*aposta_jog1-(1.06/100)*0.95*aposta_jog1)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))

                        if baralhos == 8:
                            ficha1=int(ficha1+0.95*aposta_jog1-(1.06/100)*0.95*aposta_jog1)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))
                
                    if pers_apost_jog1 == 2 :
                        ficha1=ficha1-aposta_jog1
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))

                if soma1==somab:
                    if pers_apost_jog1 == 0:
                        ficha1=ficha1-aposta_jog1
                        print("Empate! {0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))

                    if pers_apost_jog1 == 1:
                        ficha1=ficha1-aposta_jog1
                        print("Empate! {0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))

                    if pers_apost_jog1 == 2:
                        if baralhos == 1:
                            ficha1=int(ficha1+8*aposta_jog1-(15.75/100)*8*aposta_jog1)
                            print ("Empate! {0}, você venceu! Fichas: {1}".format(jogador1, ficha1))

                        if baralhos == 6:
                            ficha1=int(ficha1+8*aposta_jog1-(14.44/100)*8*aposta_jog1)
                            print ("Empate! {0}, você venceu! Fichas: {1}".format(jogador1, ficha1))
                        
                        if baralhos == 8:
                            ficha1=int(ficha1+8*aposta_jog1-(14.36/100)*8*aposta_jog1)
                            print ("Empate! {0}, você venceu! Fichas: {1}".format(jogador1, ficha1))

                if soma1> somab:
                    if pers_apost_jog1==0:
                        if baralhos == 1:
                            ficha1=int(ficha1+aposta_jog1-(1.29/100)*aposta_jog1)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))

                        if baralhos == 6:
                            ficha1=int(ficha1+aposta_jog1-(1.24/100)*aposta_jog1)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))

                        if baralhos == 8:
                            ficha1=int(ficha1+aposta_jog1-(1.24/100)*aposta_jog1)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))
                    
                    if pers_apost_jog1 == 1:
                        ficha1=ficha1-aposta_jog1
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))

                if pers_apost_jog1 == 2:
                    ficha1=ficha1-aposta_jog1
                    print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))
            
            if ficha2!=0:
                if soma2<somab :
                    if pers_apost_jog2 == 0:
                        ficha2=ficha2-aposta_jog2
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador2,ficha2))
                    if pers_apost_jog2 == 1:
                        if baralhos == 1:
                            ficha2=int(ficha2+0.95*aposta_jog2-(1.01/100)*0.95*aposta_jog2)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador2, ficha2))
                        if baralhos == 6:
                            ficha2=ficha2+0.95*aposta_jog2-(1.06/100)*0.95*aposta_jog2
                            print ("{0}, você venceu! Fichas: {1}".format(jogador2, ficha2))
                        if baralhos == 8:
                            ficha2=int(ficha2+0.95*aposta_jog2-(1.06/100)*0.95*aposta_jog2)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador2, ficha2))
                
                    if pers_apost_jog2 == 2:
                        ficha2=ficha2-aposta_jog2
                        print("{0}, você perdeu a aposta! Fichas restantes:{1}".format(jogador2, ficha2))
                
                if soma2==somab:
                    if pers_apost_jog2 == 0:
                        ficha2=ficha2-aposta_jog2
                        print("{0}, você perdeu a aposta! Fichas restantes: ".format(jogador2), ficha2)

                    if pers_apost_jog2 == 1:
                        ficha2=ficha2-aposta_jog2
                        print("{0}, você perdeu a aposta! Fichas restantes: ".format(jogador2),ficha2)

                    if pers_apost_jog2 == 2:
                        if baralhos == 1:
                            ficha2=int(ficha2+8*aposta_jog2-(15.75/100)*8*aposta_jog2)
                            print("{0}, você, venceu! Fichas: {1}".format(jogador2,ficha2))

                        if baralhos == 6:
                            ficha2=int(ficha2+8*aposta_jog2-(14.44/100)*8*aposta_jog2)
                            print("{0}, você venceu! Fichas: ".format(jogador2), ficha2)
                        
                        if baralhos == 8:
                            ficha2=int(ficha2+8*aposta_jog2-(14.36/100)*8*aposta_jog2)
                            print("{0}, você venceu! Fichas: ".format(jogador2), ficha2)

                if soma2> somab:
                    if pers_apost_jog2==0:
                        if baralhos == 1:
                            ficha2=int(ficha2+aposta_jog2-(1.29/100)*aposta_jog2)
                            print("{0}, você venceu! Fichas: ".format(jogador2),ficha2)

                        if baralhos == 6:
                            ficha2=int(ficha2+aposta_jog2-(1.24/100)*aposta_jog2)
                            print("{0}, você venceu! Fichas: ".format(jogador2),ficha2)

                        if baralhos == 8:
                            ficha2=int(ficha2+aposta_jog2-(1.24/100)*aposta_jog2)
                            print("{0}, você venceu! Fichas: ".format(jogador2),ficha2)
                    
                    if pers_apost_jog2 == 1:
                        ficha2=ficha2-aposta_jog2
                        print("{0}, você perdeu a aposta! Fichas: ".format(jogador2),ficha2)

                    if pers_apost_jog2 == 2:
                        ficha2=ficha2-aposta_jog2
                        print("{0}, você perdeu a aposta! Fichas: ".format(jogador2),ficha2)
        
        #Para 3 jogadores       
        if jogadores == 3:
            if ficha1!=0:
                if soma1<somab :
                    if pers_apost_jog1 == 0:
                        ficha1=ficha1-aposta_jog1
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))
                    if pers_apost_jog1 == 1:
                        if baralhos == 1:
                            ficha1=int(ficha1+0.95*aposta_jog1-(1.01/100)*0.95*aposta_jog1)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))

                        if baralhos == 6:
                            ficha1=int(ficha1+0.95*aposta_jog1-(1.06/100)*0.95*aposta_jog1)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))

                        if baralhos == 8:
                            ficha1=int(ficha1+0.95*aposta_jog1-(1.06/100)*0.95*aposta_jog1)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))
                
                    if pers_apost_jog1 == 2 :
                        ficha1=ficha1-aposta_jog1
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))

                if soma1==somab:
                    if pers_apost_jog1 == 0:
                        ficha1=ficha1-aposta_jog1
                        print("Empate! {0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))

                    if pers_apost_jog1 == 1:
                        ficha1=ficha1-aposta_jog1
                        print("Empate! {0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))

                    if pers_apost_jog1 == 2:
                        if baralhos == 1:
                            ficha1=int(ficha1+8*aposta_jog1-(15.75/100)*8*aposta_jog1)
                            print ("Empate! {0}, você venceu! Fichas: {1}".format(jogador1, ficha1))

                        if baralhos == 6:
                            ficha1=int(ficha1+8*aposta_jog1-(14.44/100)*8*aposta_jog1)
                            print ("Empate! {0}, você venceu! Fichas: {1}".format(jogador1, ficha1))
                        
                        if baralhos == 8:
                            ficha1=int(ficha1+8*aposta_jog1-(14.36/100)*8*aposta_jog1)
                            print ("Empate! {0}, você venceu! Fichas: {1}".format(jogador1, ficha1))

                if soma1> somab:
                    if pers_apost_jog1==0:
                        if baralhos == 1:
                            ficha1=int(ficha1+aposta_jog1-(1.29/100)*aposta_jog1)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))

                        if baralhos == 6:
                            ficha1=int(ficha1+aposta_jog1-(1.24/100)*aposta_jog1)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))

                        if baralhos == 8:
                            ficha1=int(ficha1+aposta_jog1-(1.24/100)*aposta_jog1)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador1, ficha1))
                    
                    if pers_apost_jog1 == 1:
                        ficha1=ficha1-aposta_jog1
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))

                    if pers_apost_jog1 == 2:
                        ficha1=ficha1-aposta_jog1
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador1,ficha1))
            
            if ficha2!=0:
                if soma2<somab :
                    if pers_apost_jog2 == 0:
                        ficha2=ficha2-aposta_jog2
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador2,ficha2))
                    if pers_apost_jog2 == 1:
                        if baralhos == 1:
                            ficha2=int(ficha2+0.95*aposta_jog2-(1.01/100)*0.95*aposta_jog2)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador2, ficha2))
                        if baralhos == 6:
                            ficha2=ficha2+0.95*aposta_jog2-(1.06/100)*0.95*aposta_jog2
                            print ("{0}, você venceu! Fichas: {1}".format(jogador2, ficha2))
                        if baralhos == 8:
                            ficha2=int(ficha2+0.95*aposta_jog2-(1.06/100)*0.95*aposta_jog2)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador2, ficha2))
                
                    if pers_apost_jog2 == 2:
                        ficha2=ficha2-aposta_jog2
                        print("{0}, você perdeu a aposta! Fichas restantes:{1}".format(jogador2, ficha2))

                if soma2==somab:
                    if pers_apost_jog2 == 0:
                        ficha2=ficha2-aposta_jog2
                        print("{0}, você perdeu a aposta! Fichas restantes: ".format(jogador2), ficha2)

                    if pers_apost_jog2 == 1:
                        ficha2=ficha2-aposta_jog2
                        print("{0}, você perdeu a aposta! Fichas restantes: ".format(jogador2),ficha2)

                    if pers_apost_jog2 == 2:
                        if baralhos == 1:
                            ficha2=int(ficha2+8*aposta_jog2-(15.75/100)*8*aposta_jog2)
                            print("{0}, você, venceu! Fichas: {1}".format(jogador2,ficha2))

                        if baralhos == 6:
                            ficha2=int(ficha2+8*aposta_jog2-(14.44/100)*8*aposta_jog2)
                            print("{0}, você venceu! Fichas: ".format(jogador2), ficha2)
                        
                        if baralhos == 8:
                            ficha2=int(ficha2+8*aposta_jog2-(14.36/100)*8*aposta_jog2)
                            print("{0}, você venceu! Fichas: ".format(jogador2), ficha2)

                if soma2> somab:
                    if pers_apost_jog2==0:
                        if baralhos == 1:
                            ficha2=int(ficha2+aposta_jog2-(1.29/100)*aposta_jog2)
                            print("{0}, você venceu! Fichas: ".format(jogador2),ficha2)

                        if baralhos == 6:
                            ficha2=int(ficha2+aposta_jog2-(1.24/100)*aposta_jog2)
                            print("{0}, você venceu! Fichas: ".format(jogador2),ficha2)

                        if baralhos == 8:
                            ficha2=int(ficha2+aposta_jog2-(1.24/100)*aposta_jog2)
                            print("{0}, você venceu! Fichas: ".format(jogador2),ficha2)
                    
                    if pers_apost_jog2 == 1:
                        ficha2=ficha2-aposta_jog2
                        print("{0}, você perdeu a aposta! Fichas: ".format(jogador2),ficha2)

                    if pers_apost_jog2 == 2:
                        ficha2=ficha2-aposta_jog2
                        print("{0}, você perdeu a aposta! Fichas: ".format(jogador2),ficha2)

            if ficha3!=0:
                if soma3<somab :
                    if pers_apost_jog3 == 0:
                        ficha3=ficha3-aposta_jog3
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador3,ficha3))
                    
                    if pers_apost_jog3 == 1:
                        if baralhos == 3:
                            ficha3=int(ficha3+0.95*aposta_jog3-(1.01/100)*0.95*aposta_jog3)
                            print("{0}, você venceu! Fichas: {1}".format(jogador3,ficha3))
                        if baralhos == 6 :
                            ficha3=int(ficha3+0.95*aposta_jog3-(1.06/100)*0.95*aposta_jog3)
                            print("{0}, você venceu! Fichas: {1}".format(jogador3,ficha3))
                        if baralhos == 8:
                            ficha3=int(ficha3+0.95*aposta_jog3-(1.06/100)*0.95*aposta_jog3)
                            print("{0}, você venceu! Fichas: {1}".format(jogador3,ficha3))
                        

                    if pers_apost_jog3 == 2:
                        ficha3=ficha3-aposta_jog3
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}" .format(jogador3,ficha3))

                if soma3==somab:
                    if pers_apost_jog3 == 0:
                        ficha3=ficha3-aposta_jog3
                        print("Empate! {0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador3, ficha3))

                    if pers_apost_jog3 == 1:
                        ficha3=ficha3-aposta_jog3
                        print("Empate! {0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador3,ficha3))

                    if pers_apost_jog3 == 2:
                        if baralhos == 1:
                            ficha3=int(ficha3+8*aposta_jog3-(15.75/100)*8*aposta_jog3)
                            print("Empate! {0}, você venceu! Fichas: {1}".format(jogador3,ficha3))

                        if baralhos == 6:
                            ficha3=int(ficha3+8*aposta_jog3-(14.44/100)*8*aposta_jog3)
                            print("Empate! {0}, você venceu! Fichas: {1}".format(jogador3, ficha3))
                        
                        if baralhos == 8:
                            ficha3=int(ficha3+8*aposta_jog3-(14.36/100)*8*aposta_jog3)
                            print("Empate! {0}, você venceu! Fichas: {1}".format(jogador3, ficha3))

                if soma3> somab:
                    if pers_apost_jog3==0:
                        if baralhos == 1:
                            ficha3=int(ficha3+aposta_jog3-(1.29/100)*aposta_jog3)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador3, ficha3))

                        if baralhos == 6:
                            ficha3=int(ficha3+aposta_jog3-(1.24/100)*aposta_jog3)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador3, ficha3))

                        if baralhos == 8:
                            ficha3=int(ficha3+aposta_jog3-(1.24/100)*aposta_jog3)
                            print ("{0}, você venceu! Fichas: {1}".format(jogador3, ficha3)) 
                    
                    if pers_apost_jog3 == 1:
                        ficha3=ficha3-aposta_jog3
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador3,ficha3))

                    if pers_apost_jog3 == 2:
                        ficha3=ficha3-aposta_jog3
                        print("{0}, você perdeu a aposta! Fichas restantes: {1}".format(jogador3,ficha3))
    

    

 
    






       







