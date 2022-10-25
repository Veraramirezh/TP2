# creer par henrique vera
# creer le 12 octobre
# wanna play a game...

from random import randint

max = 1000
reponse = randint(1,max)

print("Jai choisi un nombre mystere entre 1 et ",max, " à toi de le deviner")
playing = True
# alors ici, si winning est false qui veut dire quona a pas eux le bon chiffre, le number trty est egale a 0 comme indiquer,
# mais lorsque lutilisateur essai de trouver le chiffre, alors on doit ajouter plus un a chaque essai(+=1)
while playing:

    winning = False
    Nb_essais = 0
    while not winning:
        Nb_essais += 1
        #s'il na pas le bon chiffre il demande ces questions ci dissous
        chifr = int(input("choissisez un nombre entre ceux choissi tantot"))
        if chifr > reponse:
            print("votre nombre est trop grand choissiser un plus petit")
        elif chifr < reponse:
            print("votre nombre est trop petit choissisez un plus grand")
        else:
            print("vous avez fini en", Nb_essais)
            winning = True
 # on propose lidee de recommencer le jeu
    restart = input("est ce que vous voulez recommencer, oui ou non")
    if restart == "non":
        print("d'accord au revoir")
        playing = False

#fin
