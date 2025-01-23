def juegos():

    puntos=0

    print ("que tienes que hacer con tu bausra?")

    respuesta = input("tirarla o reciclarla:  ")

    if respuesta == "reciclarla" :
        print("muy bien tienes un punto")
        puntos = puntos + 1

    elif respuesta == "tirarla" : 
        print("respuesta incorrecta no tienes puntos")


    print ("siguiente pregunta, como puedes ayudar al ambiente ?")

    ayudar = input("comprando mas bolsas o llevar una bolsa de tela ?:    ")

    if ayudar == "llevar una bolsa de tela" :
        print("repuesta correcta tienes un punto")
        puntos = puntos + 1

    elif ayudar == "comprando mas bolsas" :
        print("muy mal no obtienes ningun punto")

    print("ultima pregunta como adolescente puedes hacer algo al respecto")

    hello = input("si o no :    ")

    if hello == "si":
        print("muy bien como adolescente puedes ayudar a reciclar y guardar tu basura y crear conciencia ")
        puntos = puntos + 1

    elif hello == "no" :
        print("si puedes creando conciencia con tus compañeros de la escuela y reciclando tu basura y no haciendo mas basura y reutilizar tus cuadernos")


    print("tus puntos:",puntos)