'''
Reto 2: ¡Atrapa a esos ciber criminales!

Problema

Un grupo de ciber criminales están usando mensajes encriptados para comunicarse. El FBI nos ha pedido ayuda para descifrarlos.

Los mensajes son cadenas de texto que incluyen números enteros muy largos y espacios en blanco. Aunque los números no parecen tener sentido... una chica llamada Alice ha descubierto que podrían usar el código ASCII de las letras en minúscula.

Con su método ha conseguido descifrar estos mensajes:

"109105100117" -> midu
"9911110010110998101114" -> codember
"9911110010110998101114 109105100117" -> codember midu
"11210897121 116101116114105115" -> play tetris
Pero han interceptado un mensaje más largo que no han podido y nos han dicho que es muy importante que lo descifremos:

11610497110107115 102111114 11210897121105110103 9911110010110998101114 11210810197115101 11510497114101

Ahora que ya sabes esto, https://codember.dev/encrypted.txt

Pistas
Recuerda que los mensajes son cadenas de texto conformadas por números y espacios en blanco.
Parece que los números tienen algo que ver con el código ASCII.
Los espacios en blanco parece que son simplemente espacios...

Cómo enviar la solución
Usa el comando "submit" para enviar tu solución con la frase descifrada, en minúsculas y respetando los espacios en blanco. Por ejemplo:

submit this is fine
'''

def read_txt():

    with open('C:\\Users\\garce\\Desktop\\Escritorio\\Programs\\Python\\Codember\\encrypted.txt', 'r') as f:

        txt_reader = f.readlines()

    words = []
    letter = []
    cont = 0

    for v in txt_reader[0]:

        if v == ' ':

            words.append(' ')
            cont = 0
            letter = []
        elif cont < 2:

            letter.append(v)
            cont +=1
        elif cont == 2:

            x = ''.join(letter)
            
            if int(x) < 97:

                letter.append(v)
                words.append(chr(int(''.join(letter))))
                letter = []
                cont = 0
            else:

                words.append(chr(int(''.join(letter))))
                letter = []
                letter.append(v)
                cont = 1

    print(''.join(words))


read_txt()

# Output

'''
thanks for playing codember please share
'''

# Solución
'''
$ submit thanks for playing codember please share
'''
