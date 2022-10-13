#creer par henrique vera
#creer le 12 octobre
#wanna play a game...

import random
def numero():
    #on demande a la victime un nombre a chosir
    #on retourne le nombre aleatoire chosis
    num1 = int(input("vous devez choisir deux numeros, choissisez le premier"))
    num2 = int(input("vous devez choisir deux numeros, choissisez le deuxieme"))
    return random.randint(num1, num2)


playing = True
while playing:
    number_range = numero()
    winning = False
    number_try = 0
    while not winning:
        number_try += 1
#s'il na pas le bon chiffre il demande ces questions ci dissous
        entre_nmbr = int(input("choissisez un nombre entre ceux choissi tantot"))

        if entre_nmbr > number_range:
            print("votre nombre est trop grand, choissiser un plus petit")
        elif entre_nmbr < number_range:
            print("votre nombre est trop petit, choissisez un plus grand")
        else:
            print("vous avez fini en", number_try)
            winning = True

# on propose lidee de recommencer le jeu
    recommencer = input("est ce que vous voulez recommencer, oui ou non")
    if recommencer == "non":
        playing = False

#fin