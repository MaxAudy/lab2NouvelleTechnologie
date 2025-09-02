# Question 1
def division_euclidienne(dividende, diviseur):
    quotient = 0
    reste = dividende
    #quotient = dividende // diviseur
    #reste = dividende - (quotient * diviseur)
    #while (reste >= diviseur):
    #   reste -= diviseur
    #    quotient += 1

    if diviseur > 0:
        while reste >= diviseur:
            reste -= diviseur
            quotient += 1
        while reste < 0:
            reste += diviseur
            quotient -= 1
    else:  # si le diviseur est négatif
        while reste <= diviseur:
            reste -= diviseur
            quotient += 1
        while reste > 0:
            reste += diviseur
            quotient -= 1
    print("Quotient : " + str(quotient))
    print("Reste : " + str(reste))

division_euclidienne(100,23)
# Quotient : 4
# Reste : 8

division_euclidienne(-100,23)
# Quotient : -5
# Reste : 15





# Question2
def formater_duree(secondes):
    annees = divmod(secondes,60 * 60 * 24 * 365) 
    jours = divmod(annees[1],60 * 60 * 24)
    heures = divmod(jours[1],60 * 60)
    minutes = divmod(heures[1],60)
    secondes = minutes[1]    

    print((str(annees[0]) + " année" if annees[0] <= 1 else str(annees[0]) + " années") + " " +
           (str(jours[0]) + " jour" if jours[0] <= 1 else str(jours[0]) + " jours") + " " +
            (str(heures[0]) + " heure" if heures[0] <= 1 else str(heures[0]) + " heures") + " " +
             (str(minutes[0]) + " minute" if minutes[0] <= 1 else str(minutes[0]) + " minutes") + " " +
              (str(secondes) + " seconde" if secondes <= 1 else str(secondes) + " secondes")
        )


formater_duree(123381181)
# 3 années 333 jours 0 heure 33 minutes 1 seconde



def entier_vers_caractere(nombre):
    chiffres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return chiffres[nombre]

def caractere_vers_entier(c):
    if "0" <= c <= "9":
        return ord(c) - ord("0")
    elif "A" <= c <= "Z":
        return ord(c) - ord("A") + 10

def nb_chiffre_apres_virgule(nb):
    nb_apres_virgule = 0
    if "." in nb:
       nb_apres_virgule = len(nb.split(".")[1])
    else:
       nb_apres_virgule = 0

    return nb_apres_virgule

def nb_chiffre_avant_virgule(nb):
    nb = str(nb)  

    # Si le nombre est négatif, on enlève le "-"
    if nb.startswith("-"):
        nb = nb[1:]

    if "." in nb:
        return len(nb.split(".")[0])  # partie avant la virgule
    else:
        return len(nb)  # tout le nombre (pas de virgule)
    
def est_negatif(nb) :
    nb = str(nb)  
    if(nb.startswith("-")):
        return True
    else:
        return False


# Question 3
def conv_nombre_base_vers_decimal(nombre_en_base, base):
 
 nbChiffreApresVirgule = nb_chiffre_apres_virgule(nombre_en_base)
 nbChiffreAvantVirgule = nbChiffreAvantVirgule(nombre_en_base)
 est_negatif = est_negatif(nombre_en_base)
 result = str("")

 if(base >= 2): #Base 2 au plus et au plus 8 chiffres après la virgule

    if(est_negatif):  # Rendre le chiffre positif pour simplifier les calculs
     nombre_en_base *= -1

    
    while(quotienEtReste[0] != 0): #Convertir la partie avant la virgule
        quotienEtReste = (nbChiffreAvantVirgule,0)
        quotienEtReste = divmod(quotienEtReste[0],base)
        result += quotienEtReste[1]

    while(quotienEtReste[0] != 0 or i < 7):
        i = 0





    
    
    #rendre négatif si nécéssaire
    #Faire le calcule apres la virgule



def conv_decimal_vers_base(n, base):
    pass



# conv_nombre_base_vers_decimal("-1231.1201", 4)
# -109.390625

# conv_nombre_base_vers_decimal("A00.B", 12)
# 1440.91666666

# conv_decimal_vers_base(171.32, 8)
# "253.24365605"

# conv_decimal_vers_base(203.75, 20)
# "A3.F"
