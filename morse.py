#-------------------------------------------------------------------------------
# Règles d'utilisation du traducteur : 
#   
#   - '_' = long    ///    '.' = court    (exemple : maison => __ ._ .. ... ___ _.)

#   - Quand traduction 'morse ==> alphabet', chaques symboles Morse représentant une lettre possède un espace entre elle pour créer un mot      (exemple : V(..._) O(___) I(..) T(_) U(.._) R(._.) E(.) => ..._ ___ .. _ .._ ._. .) 

#   - Quand traduction 'morse ==> alphabet', à la fin de chaque mot il faut mettre un ' / '     (exemple : la maison grise => ._.. ._ / __ ._ .. ... ___ _. / __. ._. .. ... .)


#-------------------------------------------------------------------------------



#Alphabets  (alphabet[i] = morse[i])

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, ",", "?", "!", ":", "=", "+", "-", " ", ".", "  "]

morse = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "._..", "__", "_.", "___", ".__.", "__._", "._.", "...", "_", ".._", "..._", ".__", "_.._", "_.__", "__..", ".____", "..___", "...__", "...._", ".....", "_....", "__...", "___..", "____.", "_____", "__..__", "..__..", "_._.__", "___...", "_..._", "._._.", "_...._", "/", "._._._", "  "]


trad = []

selection = input(print("Alphabet vers Morse ==> 1 /// Morse vers alphabet ==> 2"))


# ------------------------------------------------------
if selection == "1":     # morse ==> alphabet
    z = input(print("Ecris ton code Morse pour le traduire en texte :"))

    x = z.split("  ")
    
    for i in range(0, len(x)):
        p = x[i].split()
        p.append(" / ")
        for i in p:
            if i in morse:
                trad.append(alphabet[morse.index(i)])
            # else : 
            #     print("index:", p.index(i), 'Il y a une erreur dans le formatage du code')

    print("Le texte est :", "[", "".join(trad), "]")

elif selection == "2":       #alphabet ==> morse
    z = input(print("Ecris ton mot pour le traduire en morse :"))

    x = list(z)

    for i in x:
        if i in alphabet:
            trad.append(morse[alphabet.index(i)])
        else : 
            print('Il y a une erreur dans le texte')

    print("Le code en Morse est :", "[", " ".join(trad), "]")

else:
    print("Vous avez saisie une valeur différente de 1 ou 2")

#-------------------------------------------------------




