'''
Reto 3: La zebra de colores

Problema

TMChein ya se está preparando para las fiestas y quiere empezar a decorar la casa con las luces de navidad.

Quiere comprar una pero sus favoritas son las que tienen dos colores que se van alternando. Como una zebra de dos colores.

Ha hecho que las luces sean Arrays y cada posición un color. Y quiere saber qué luces tienen las zebras más largas y cuál es el último color de esa sucesión de colores. Por ejemplo:

['red', 'blue', 'red', 'blue', 'green'] -> 4, blue
['green', 'red', 'blue', 'gray'] -> 2, gray
['blue', 'blue', 'blue', 'blue'] -> 1, blue
['red', 'green', 'red', 'green', 'red', 'green'] -> 6, green
['blue', 'red', 'blue', 'red', 'gray'] -> 4, red
['red', 'red', 'blue', 'red', 'red', 'red', 'green'] -> 3, red
['red', 'blue', 'red', 'green', 'red', 'green', 'red', 'green'] -> 6, green

Fíjate que sólo quiere saber la longitud de cuando dos colores se van alternando. Una vez que se rompe la alternancia de los dos colores, deja de contar.

Ahora que ya sabes esto, https://codember.dev/colors.txt

Recuerda que una zebra de colores es cuando dos colores se alternan una y otra vez. Si se repite un color en la posición siguiente o es un tercer color, entonces se deja de contar.
Lo que queremos calcular es la tira de colores más larga en forma de zebra y el último color de esa tira de colores.

Cómo enviar la solución
Usa el comando "submit" para enviar tu solución. Por ejemplo:

$ submit 62@red
'''
import requests
import json

url = 'https://codember.dev/colors.txt'

def read_txt():
    response = requests.get(url)
    txt_reader = json.loads(response.text)

    #txt_reader = ['green', 'red', 'blue', 'gray']
    #txt_reader = ['blue', 'blue', 'blue', 'blue']
    #txt_reader = ['red', 'green', 'red', 'green', 'red', 'green']
    #txt_reader = ['red', 'blue', 'red', 'blue', 'green']
    #txt_reader = ['blue', 'red', 'blue', 'red', 'gray']
    #txt_reader = ['red', 'red', 'blue', 'red', 'red', 'red', 'green']
    #txt_reader = ['red', 'blue', 'red', 'green', 'red', 'green', 'red', 'green']

    a = []
    b = []

    for index, i in enumerate(txt_reader):

        if len(a) < 1 or (len(a) == 1 and a[0] != i):

            a.append(i)
        elif len(a) >= 2:
            
            if a[-1] != i and a[-2] == i:

                a.append(i)
            else:

                if len(b) <= len(a):

                    b = a

                a = []
                a.append(txt_reader[index-1])
                a.append(i)
        
        if index == len(txt_reader) - 1:

            if len(b) <= len(a):
                
                    b = a

    
    '''print(a)
    print(b)'''

    print(f'{len(b)}@{b[-1]}')


read_txt()

# Output

'''
30@red
'''

# Solución
'''
$ submit 30@red
'''
