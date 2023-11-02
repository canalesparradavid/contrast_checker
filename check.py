import sys
import color as co

# Compruebo si se han indicado dos colores por comando
if (len(sys.argv) > 2):
    color1 = co.Color(sys.argv[1])
    color2 = co.Color(sys.argv[2])
elif (len(sys.argv) > 1):
    color1 = co.Color(sys.argv[1])
    color2 = co.Color(input("Introduzca el color 2: "))
else:
    color1 = co.Color(input("Introduzca el color 1: "))
    color2 = co.Color(input("Introduzca el color 2: "))

# Calculo el contraste entre los dos colores
contraste = co.Color.contraste(color1, color2)

print("Ratio de contraste: {:.2f}".format(contraste))
