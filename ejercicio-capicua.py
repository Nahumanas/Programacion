#Palabras Capicua 
def palabras_espacio(texto):
    words_inspace = "" #se genera el espacio para que al leerlo no produzca incovenientes 
    for chain in texto:
        if chain != " ":
            words_inspace += chain 
    return words_inspace


def palabra_reversa(texto):
    words_reversa = ""
    for chain in texto: 
        words_reversa = chain + words_reversa #lo igualo al reves para que se pueda leer en reversa
    return words_reversa
       
def palabras_capicuas(texto):
    words_inspace = palabras_espacio(texto)
    words_reversa = palabra_reversa(texto)
    return words_inspace.lower() == words_reversa.lower() #lower es para que siempre python lo pase a minuscula asi,
                                                           #no hay incovenientes.

print("amor de palo" , palabras_capicuas("amor de palo"))

