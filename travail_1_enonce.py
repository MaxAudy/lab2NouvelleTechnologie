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


def tronquer_8_decimales_sans_arrondir(x: float) -> str:
    s = f"{x:.20f}"            # conversion en chaîne avec beaucoup de décimales
    if "." not in s:
        return s
    avant, apres = s.split(".", 1)
    apres = apres[:8]          # garder max 8
    apres = apres.rstrip("0")  # enlever les zéros de fin inutiles
    return avant if apres == "" else avant + "." + apres



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
    s = str(nb)
    return len(s.split(".", 1)[1]) if "." in s else 0
    
def est_negatif(nb) :
    nb = str(nb)  
    if(nb.startswith("-")):
        return True
    else:
        return False


# Question 3
def conv_nombre_base_vers_decimal(nombre_en_base, base):
    if not (2 <= base <= 36):
        raise ValueError("La base doit être entre 2 et 36.")

    # Vérifier le signe
    negatif = nombre_en_base.startswith("-")
    if negatif:
        nombre_en_base = nombre_en_base[1:]

    # Séparer partie entière et fractionnaire
    if "." in nombre_en_base:
        partie_entiere, partie_frac = nombre_en_base.split(".")
    else:
        partie_entiere, partie_frac = nombre_en_base, ""

    # Conversion partie entière
    valeur = 0
    for c in partie_entiere:
        valeur = valeur * base + caractere_vers_entier(c)

    # Conversion partie fractionnaire
    puissance = base
    for c in partie_frac:
        valeur += caractere_vers_entier(c) / puissance
        puissance *= base

    return "-" + tronquer_8_decimales_sans_arrondir(valeur) if negatif else tronquer_8_decimales_sans_arrondir(valeur)


def conv_decimal_vers_base(n, base):

    # vérifier que la base est valide
    if not (2 <= base <= 36):
        raise ValueError("La base doit être entre 2 et 36.")
    
    # vérifier le signe
    negatif = n < 0
    x = abs(float(n)) 

    # séparer partie entière et fractionnaire
    entier = int(x)           # partie entière
    frac = x - entier         # partie après la virgule


    # conversion de la partie entière
    tmp = int(x)
    if tmp == 0:
        partie_entiere_convertie = "0"
    else:
        acc = []
        while tmp > 0:
            tmp, reste = divmod(tmp, base)
            acc.append(entier_vers_caractere(reste))
        partie_entiere_convertie = "".join(reversed(acc))


    # conversion de la partie fractionnaire

    chiffres_frac = []
    for _ in range(8):          # max 8 chiffres
        if frac == 0:
            break
        frac *= base
        d = int(frac)           # partie entière
        chiffres_frac.append(entier_vers_caractere(d))
        frac -= d               # garder seulement la partie après la virgule

    # assembler le résultat
    if chiffres_frac:
        resultat = partie_entiere_convertie + "." + "".join(chiffres_frac)
    else:
        resultat = partie_entiere_convertie

    if negatif and resultat != "0":
        resultat = "-" + resultat

    return resultat
    

print(conv_nombre_base_vers_decimal("-1231.1201", 4))
# -109.390625

print(conv_nombre_base_vers_decimal("A00.B", 12))
# 1440.91666666

print(conv_decimal_vers_base(171.32, 8))
# "253.24365605"

print(conv_decimal_vers_base(203.75, 20))
# "A3.F"
