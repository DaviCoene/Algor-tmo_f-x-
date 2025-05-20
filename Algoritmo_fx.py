import random

## Parametros     
def algoritmo_(qtdexpoentesMax = 3, complexidade = 1):
    ## Quantidade Máxima do Grau do Expoente


    ## Grau de complexidade do algorítmo


    ## ----------------------ALGORITMO------------------------ ##

    função = [] # Quantidade de Elementos 
    exp = []  # Expoente das Funções

    constante = 0 # Valores com grau Zero

    for x in range(random.randint(2,complexidade*5)): # Sorteio aleatório para os graus
        expo = random.randint(0,qtdexpoentesMax) 
        função.append(chr(65 + x))  # Adionando quantidade de elementos
        exp.append(expo)

    valorX = [i for i in range(6)] # Valores do domínio

    for x, y in zip(função, exp):   # Percorre as duas listas para transformar valores em variáveis
        if y == 0:
            constante = constante + random.randint(0, complexidade*5)

        globals()[x] = y

    listtemp = [] # Lista para agrupar graus repetidos

    for i in range(len(exp)): # Algoritmo para agrupar graus repetidos
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

    listadelete = [] # Lista para deletar Valores repetidos
    if listtemp:    # Adiciona valores para deletar
        for i in listtemp:  
            for j in i[1]:
                listadelete.append(j)

    valores = [x for x in função if x not in listadelete] # Adiciona valores que serão usados na função

    for i in listadelete:   #Deleta variaveis repetídas
        del globals()[i]

    Funcao_armazenada = []
    for f in valorX:    #Calcula a função
        valorfuncao = 0
        for x in range(qtdexpoentesMax):
            if x == 0:
                valorfuncao = valorfuncao + constante
                Funcao_armazenada.append(str(valorfuncao))
            else:
                for i in valores:
                    if globals()[i] == x:
                        valorconst = random.randint(1,2*complexidade)
                        Funcao_armazenada.append(" + ")
                        Funcao_armazenada.append(str(valorconst) +"x"+"^"+str(f))
                        
                        valorfuncao = valorfuncao + valorconst*f**x
        print("Domínio: ",f," Imagem: ",valorfuncao) # Imprime o domínio e Imagem da função.

    Funcao_armazenada.reverse()
    print(Funcao_armazenada)
pass
pass

    