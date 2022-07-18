def l100kmtompg():
    print ("Cuantas litros/100km avanza un automovil")
    millas_galon = float(input("Coloque las millas por galon: "))

    millas_galon = 235.21 / millas_galon 
    print ("La distancia de un automovil es ", millas_galon, " l/100km")
l100kmtompg()

def mpgtol100km():
    print("\n")
    print ("Cuantas millas por galon avanza un automovil")
    l_km = float(input("Coloque los l/100km: "))

    l_km = 235.21 / l_km 
    print ("La distancia de un automovil es ", l_km, " millas/galon")
mpgtol100km()