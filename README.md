# Contrast Checker
Este proyecto consiste en un script que comprueba el inidice de contraste entre dos colores; el algoritmo esta basado en las operaciones indicadas en esta guia:
[https://aprenderuxui.com/ratio-de-contraste/aprender/uidesign/](https://aprenderuxui.com/ratio-de-contraste/aprender/uidesign/)

El funcionamiento de este programa es mediante consola de comandos, en la cual se introducirá el siguiente comando:

    python3 check.py [color1 color2]

si no se introduce alguno de los dos colores por terminal este se pedirá por teclado al usuario.

El programa acepta tanto valores en RGB con en Hexadecimal; pero si se va a introducir un color en exadecimal este requerirá de `#` al pricipio de este y en caso de ser pasado por por parametro al programa deberá ir rodeado por comillas dobles.

Ejemplo:
```
usuario:ruta$ python3 check.py "#123456" 123255100
Ratio de contraste: 9.89
```
```
usuario:ruta$ python3 check.py
Introduzca el color 1: #123456
Introduzca el color 2: 123255100
Ratio de contraste: 9.89
```
```
usuario:ruta$ $ python3 check.py "#123456"
Introduzca el color 2: 123255100
Ratio de contraste: 9.89

```
