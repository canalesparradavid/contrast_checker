import re

class Color:
    def __init__(self, color_text):
        if (re.search("#", color_text) and len(color_text) == 7):           # HEX
            self.r = int(color_text[1:3], 16)
            self.g = int(color_text[3:5], 16)
            self.b = int(color_text[5:7], 16)
        elif ((not re.search("\D", color_text)) and len(color_text) == 9):  # RGB
            self.r = int(color_text[0:3])
            self.g = int(color_text[3:6])
            self.b = int(color_text[6:9])
        else:                                                               # NO FORMAT
            self.r = -1
            self.g = -1
            self.b = -1

    def luminancia(self):
        # Paso 1 - Valor por unidad
        canales = [self.r/255, self.g/255, self.b/255]

        # Paso 2 - Comprobacion de criterio
        for i in range(0,len(canales)):
            # Paso 3 - Aplicacion formulas criterio
            if(canales[i] <= 0.03928):
                canales[i] = canales[i] / 12.92
            else:
                canales[i] = ((canales[i] + 0.055) / 1.055) ** 2.4

        # Paso 4 - Luminancia relativa (coeficiente de participacion)
        luminancia = canales[0] * 0.2126 + canales[1] * 0.7152 + canales[2] * 0.0722

        # Paso 5 - Suavizado
        luminancia += 0.05

        return luminancia

    @staticmethod
    def contraste(color1, color2):
        contraste = color1.luminancia() / color2.luminancia()
        if (contraste < 1):
            return 1 / contraste
        return contraste
