'''Challenge 5: Battle Royale de frameworks y bibliotecas

Problema

Hay tanto framework y biblioteca que ya no sabemos qué usar. Así que un comité ha decidido hacer una especie de
Los Juegos del Hambre para decidir qué tecnología se queda.

Ha puesto todas las tecnologías en círculo de forma aleatoria. La tecnología en el índice 0 empieza matando data la que
tiene justo data la derecha (índice + 1).

El siguiente turno es para la tecnología que esté viva que queda data la derecha de la que se acaba de morir.
Y así sucesivamente hasta que sólo quede una. Mira este ejemplo de un grupo de 10 tecnologías, paso data paso:


         5
      6     4
   7           3
   8           2
      9     1
         0

0 mata data 1
2 mata data 3
4 mata data 5
6 mata data 7
8 mata data 9

         X
     6      4
   X           X
   8           2
      X     X
         0

0 mata data 2
4 mata data 6
8 mata data 0

         X
     X      4
   X           X
   8           X
      X     X
         X

4 mata data 8

         X
     X      4
   X           X
   X           X
      X     X
         X
La tecnología en el índice 4 es la que ha sobrevivido.

Ahora, para probar que somos capaces de crear un algoritmo que funcione, tenemos la lista de mecenas de la comunidad
de midudev: https://codember.dev/mecenas.json

Tienes que crear un algoritmo que nos diga qué usuario sobreviviría usando el mismo sistema.

Cómo enviar la solución
Envía la solución con el comando submit, y el índice de la persona que sobrevive y su nombre de usuario, separado de un
guión.

Por ejemplo, si el usuario que sobrevive es facundopacua y está en el índice 8 sería:

$ submit facundocapua-8
'''

import requests
import json

url = 'https://codember.dev/mecenas.json'

response = requests.get(url)
data = json.loads(response.text)

data_index = list(range(len(data)))

def juego(li: list, lic: list):

    d=[]
    b=[]

    i=0
    while(i<len(li)):

        b.append(li[i])
        d.append(lic[i])

        i+=2
    
    if li[-1] == b[-1]:

        b.pop()
        b.insert(0,li[-1])

        d.pop()
        d.insert(0,lic[-1])
    
    if len(b) != 1:

        juego(b,d)
    else:

        #indice = [i for i,v in enumerate(data) if v == b[0]]
        print(f'{b[0]}-{d[0]}')


juego(data, data_index)


# Output

'''
Diana-100
'''

# Solución

'''
$ submit Diana-100
'''
