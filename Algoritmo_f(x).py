import math
import random

## Parametros     

qtdexpoentesMax = 3
## complexidade de 1 a 10
complexidade = 1

## ----------------------ALGORITMO------------------------ ##

função = []
exp = []

constante = 0

for x in range(random.randint(2,complexidade*5)):
    expo = random.randint(0,qtdexpoentesMax)
    função.append(chr(65 + x))  
    exp.append(expo)

valorX = [i for i in range(6)]

for x, y in zip(função, exp):
    if y == 0:
        constante = constante + random.randint(0, complexidade*5)

    globals()[x] = y
    print(x)
print(constante)

listtemp = []

for i in range(len(exp)):
    valor1 = chr(i + 65)
    for j in range(len(exp)):
        valor2 = chr(j + 65)
        if (globals()[valor1] == globals()[valor2]) & (valor1 != valor2) & (globals()[valor1] != 0):
            ok = True
            if listtemp:
                for i in listtemp:
                    if i == [valor2, valor1]:
                        ok = False
                    if ok == False:
                        break
                if ok == False:
                    break
                else:
                    listtemp.append([valor1, valor2])
                    break
            else:
                listtemp.append([valor1, valor2])

listadelete = []
if listtemp:
    for i in listtemp:
        for j in i[1]:
            listadelete.append(j)

valores = [x for x in função if x not in listadelete]

for i in listadelete:
    del globals()[i]

for f in valorX:
    valorfuncao = 0
    for x in range(qtdexpoentesMax):
        if x == 0:
            valorfuncao = valorfuncao + constante
        else:
            for i in valores:
                if globals()[i] == x:
                    valorfuncao = valorfuncao + f**x
    print("Domínio: ",f," Imagem: ",valorfuncao)



pass
pass

    