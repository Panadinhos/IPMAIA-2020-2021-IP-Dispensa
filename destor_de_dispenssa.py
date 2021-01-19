import os
# import only system from os
from os import system, name

class fonts: #criar a classe fonts para atribuir cores ao texto apresentado no terminal
    ROXO = '\033[95m'
    AZUL = '\033[94m'
    CIANO = '\033[96m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    BRANCO = '\033[0m'
    NEGRITO = '\033[1m'
    SUBLINHADO = '\033[4m'

class produto(): #criar classe produto
    def __init__(self,nome='',quant=0,desc=''): #iniciar variaveis da classe
        self.nome=nome
        self.quant=quant
        self.desc=desc

    def __str__(self): # formatar como é feito o print da class
        return "***************************\n"+str(self.nome)+" - "+str(self.quant)+" uni.\n"+self.desc
    def save(self):# formatar como é gravada a class
        return str(self.nome)+"/"+str(self.quant)+"/"+self.desc+"/"+str(maxi)+"\n"

# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

prods=[] #declarar a array prods, onde serão guardados os produtos na dspensa
f=11 #declarar variavel que será usada pelo utilizador para selecionar uma opção
spa=0 ## capacidade max=30
maxi=30 #espaço máximo da despensa
try:
    file=open("dispensa.txt","r") # abre o ficheiro list.txt e para ler o seu conteúdo
    r=file.readline() #lê o ficheiro linha a linha e atribui esse valor à variavel r
    while r != "": #repete enquanto r não estiver vazio
        x=produto() #atribui a x as propriedades da classe produtos
        z=r.split('/') #separa os valores no r em '/' e atribui esses valores a z
        x.nome  = z[0] #atribui o valor em z[0]
        x.quant  = int(z[1]) #atribui o valor em z[1]
        x.desc  = z[2] #atribui o valor em z[2]
        maxi = int(z[3]) #atribui o valor em z[3]
        prods.append(x) #une os valores em x à lista prods
        spa=spa+x.quant #adiciona à variavel spa a quantidade introduzida
        r=file.readline() #lê o ficheiro linha a linha e atribui esse valor à variavel r
except FileNotFoundError: #em caso de o ficheiro não existir, esta função permite ao programa que continue a funcionar
    a=1


while f!= "0":
    print(fonts.CIANO+"***************"+fonts.NEGRITO+fonts.SUBLINHADO+fonts.AZUL+"MENU DA DISPENSA"+fonts.BRANCO+fonts.CIANO+"**************")
    print(fonts.VERDE+'1) Produtos')
    print('2) Capacidade da dispensa')
    print('3) Listar encomendas')
    print('4) Gravar registo')

    print('0 - Sair') ##V
    print(fonts.CIANO+"*********************************************"+fonts.BRANCO)

    f=input('Selecionar Opção:') # variavel f recebe o valor introduzido introduzido pelo utilizador

    if f == "1": #se f é igual a 1
        clear()

        print(fonts.CIANO+"***************"+fonts.NEGRITO+fonts.SUBLINHADO+fonts.AZUL+"PRODUTO"+fonts.BRANCO+fonts.CIANO+"***************")
        print(fonts.VERDE+'1 - Adicionar produto')
        print('2 - Adicionar a produto existente')
        print('3 - Ver lista de produtos') ##V
        print('4 - Retirar produto')##V
        print('5 - Procurar produto')
        print('0 - Sair')
        print(fonts.CIANO+"*************************************"+fonts.BRANCO)

        fE = input('Selecionar Opção:')

        if fE == "1":
            clear()
            i=0 # iniciar a variavel i em 0 para verificar que não há conflitos entre opções diferentes
            try:
                n=int(input('Quantos produtos diferentes vai introduzir? ')) #n recebe o valor introduzido pelo utilizador

                for i in range(n): #este ciclo irá repetir o número de vezesinserido pelo utilizador
                    aux=produto() # criar uma variavel auxiliar a que está atribuido a classe produto. esta variavel ira permitir ao utilizador adicionar produtos
                    aux.nome=input('Nome do produto: ') # recebe o nome do produto, introduzido pelo utilizador

                    pos=None # criar a variavel pos, vazia
                    for k in range(len(prods)): #o ciclo percorre os nomes no array prods
                        if aux.nome in prods[k].nome: # verifica se o nome já se encontra no array
                            pos=k #se encontrar um nome que já se encontre na lista,atribui à variavel pos, o valor de k, que representa a posição onde se encontra o nome repetido
                            break #se encontrar um nome que já se encontre na lista, pára o ciclo

                    if pos != None:
                        print('Este produto já está na despensa.')
                        quant=int(input('Quantidade a adicionar: ')) #se o utlizador introduz um nome que já está na lista, pergunta apenas quanto quer adicionar
                        quanti=prods[pos].quant+quant# atribui a variavel quanti a soma da quantidade de produto e a quantidade adicionada pelo utlizador
                        if spa+quant > maxi: #verifica se a variavel spa com a variavel quant ultrapassa o espaço máximo da despensa maxi
                            print('Não tem espaço suficiente na dispensa.')
                            print('Espaço restante:',maxi-spa) #mostra o espaço restante na despensa
                        else:
                            prods[pos].quant=quanti #se a condição não se verificar, a quantidade introduzida pelo utilizador é somada à quantidade existente
                            spa=spa+quant #adiciona à variavel spa a quantidade introduzida
                    else: #se o produto é novo
                        aux.quant=int(input('Quantidade: '))# recebe a quantidade do produto, introduzido pelo utilizador
                        aux.desc=input('Descrição: ') # recebe a descriçao do produto, introduzido pelo utilizador
                        if aux.quant+spa > maxi: #verifica se a variavel spa com a variavel quant ultrapassa o espaço máximo da despensa maxi
                            print('Não tem espaço suficiente na dispensa.')
                            print('Espaço restante:',maxi-spa) #mostra o espaço restante na despensa
                        else:
                            spa=spa+aux.quant #adiciona à variavel spa a quantidade introduzida
                            prods.append(aux) #adiciona as variaveis com a info do produto à array
            except ValueError: #em caso dos inputs do utlizador estarem incorretos, esta função permite ao programa que continue a funcionar
                    print(fonts.SUBLINHADO+fonts.VERMELHO+'ERRO devido a input do utilizador. Por favor introduza o que lhe é pedido'+fonts.BRANCO)
        elif fE == "2":
            clear()
            i=0 # iniciar a variavel i em 0 para verificar que não há conflitos entre opções diferentes
            print('')
            if len(prods) == 0: #verifica se a variavel está vazia
                print('A despensa está vazia')
            else:
                try:
                    for i in range(len(prods)): #o ciclo percorre a lista
                        print(i+1) #escreve a soma da variavel i com 1
                        print(prods[i]) #escreve a lista prods
                        print(fonts.CIANO+'********************'+fonts.BRANCO)
                    print('')
                    p=int(input('Selecione o produto a editar: ')) # recebe o valor introduzido pelo utilizador
                    p=p-1 #subtrai 1 a p
                    q=int(input('Quantas unidades pretende adicionar?')) # recebe o valor introduzido pelo utilizador
                    quanti=prods[p].quant+q# atribui a variavel quanti a soma da quantidade de produto e a quantidade adicionada pelo utlizador
                    if spa+q > maxi: #verifica se a variavel spa com a variavel quant ultrapassa o espaço máximo da despensa maxi
                        print(fonts.AMARELO+'Não tem espaço suficiente na dispensa.')
                        print('Espaço restante:',maxi-spa+fonts.BRANCO) #mostra o espaço restante na despensa
                    else:
                        spa=spa+q #adiciona o espaço a ser ocupado pelo produto
                        prods[p].quant=quanti #se a condição não se verificar, a quantidade introduzida pelo utilizador é somada à quantidade existente
                except ValueError: #em caso dos inputs do utlizador estarem incorretos, esta função permite ao programa que continue a funcionar
                    print(fonts.SUBLINHADO+fonts.VERMELHO+'ERRO devido a input do utilizador. Por favor introduza o que lhe é pedido'+fonts.BRANCO)

        elif fE =="3":
            clear()
            i=0 # iniciar a variavel i em 0 para verificar que não há conflitos entre opções diferentes
            print('')
            print('Despensa')

            if len(prods) == 0: #verifica se a variavel está vazia
                print('A despensa está vazia')
            else: #se não estiver vazia
                for i in range(len(prods)):
                    print(prods[i]) #escreve a array
                print('')
                print('Espaço ocupado:',spa)
                print('Espaço restante:',maxi-spa)

        elif fE == "4":
            clear()
            i=0 # iniciar a variavel i em 0 para verificar que não há conflitos entre opções diferentes
            print('')
            if len(prods) == 0: #verifica se a variavel está vazia
                print(fonts.AMARELO+'A despensa está vazia'+fonts.BRANCO)
            else:
                try:
                    for i in range(len(prods)): #o ciclo percorre a lista
                        print(i+1) #escreve a soma da variavel i com 1
                        print(prods[i]) #escreve a lista prods
                        print(fonts.CIANO+'********************'+fonts.BRANCO)
                    print('')
                    p=eval(input('Selecione o produto a retirar: ')) # recebe o valor introduzido pelo utilizador
                    p=p-1 #subtrai 1 a p
                    q=eval(input('Quantos pretende retirar?')) # recebe o valor introduzido pelo utilizador
                    if prods[p].quant == q: # verifica se a variavel q é igual à quantidade do produto selecionado
                        prods.pop(p) #verifica-se, elemina o registo da array prods
                        spa=spa-q #remove o espaço a ser ocupado de spa
                    elif prods[p].quant < q:
                        print(fonts.AMARELO+'O valor que introduzui é maior que a quantidade na despensa')
                    else:
                        prods[p].quant = prods[p].quant - q #subtrai a quantidade introduzida da quantidade do produto
                        spa=spa-q #remove o espaço a ser ocupado de spa
                except Exception: #em caso dos inputs do utlizador estarem incorretos, esta função permite ao programa que continue a funcionar
                    print(fonts.SUBLINHADO+fonts.VERMELHO+'ERRO devido a input do utilizador. Por favor introduza o que lhe é pedido'+fonts.BRANCO)

        elif fE == "5":
            clear()
            pos=None
            i=0 # iniciar a variavel i em 0 para verificar que não há conflitos entre opções diferentes
            n=input('Introduzir nome:') # n recebe o valor introduzido
            for i in range(len(prods)): #o ciclo percorre a array prods
                if n in prods[i].nome: #verifica se a variavel n se encontra na array
                    pos=i #se encontrar um nome que já se encontre na lista,atribui à variavel pos, o valor de k, que representa a posição onde se encontra o nome repetido
                    break #se encontrar um nome que já se encontre na lista, pára o ciclo

            if pos != None: # verifica se pos tem um valor
                print(prods[i]) # se tem, escreve o produto nessa posição
            else:
                print(fonts.AMARELO+'Produto não encontrado'+fonts.BRANCO) #se pos está vazio, escreva uma mensagem

        elif fE == "0":
            clear()



    elif f == "2":
        clear()
        print(fonts.CIANO+"*********"+fonts.NEGRITO+fonts.SUBLINHADO+fonts.AZUL+"CAPACIDADE DA DISPENSA"+fonts.BRANCO+fonts.CIANO+"*********")
        print(fonts.VERDE+'1 - Espaço restante na dispensa')
        print('2 - Mudar capacidade da despensa')
        print('0 - Sair')
        print(fonts.CIANO+"****************************************"+fonts.BRANCO)

        fE2 = input("Selecionar Opção:")

        if fE2 == "1":
            clear()
            print(fonts.AMARELO+'Restam ',maxi-spa,' unidades de espaço na despensa'+fonts.BRANCO) #escreve no ecrã o espaço restanto na despensa

        elif fE2 == "2":
            clear()
            try:
                esp=int(input('Introduza a nova capacidade: ')) #o utilizador insere a nova capacidade da despensa
                if esp < spa: #se a nova capacidade for menor do que está a ser ocupado
                    print(fonts.SUBLINHADO+fonts.VERMELHO+'ERRO O tamanho da despensa não pode ser menor que o espaço a ser ocupado.'+fonts.BRANCO)
                    print(fonts.AMARELO+'Tem de retirar produtos da despensa.') #informa o utlizador que o valor que introduzui é inválido
                    print('Espaço a ser ocupado: ',spa+fonts.BRANCO) #escreve no ecra o espaço a ser ocupado
                else:
                    maxi=esp
            except ValueError: #em caso dos inputs do utlizador estarem incorretos, esta função permite ao programa que continue a funcionar
                print(fonts.SUBLINHADO+fonts.VERMELHO,'ERRO devido a input do utilizador. Por favor introduza o que lhe é pedido'+fonts.BRANCO)

        elif fE2 == "0":
            clear()

    elif f == "3":
        clear()
        i=0 # iniciar a variavel i em 0 para verificar que não há conflitos entre opções diferentes
        for i in range(len(prods)):
            if prods[i].quant <= 2: #verifica se a quantidade do produto é menor ou igual a 2
                print(prods[i].nome) #escreve o nome do produto na posição i
                print(fonts.CIANO+'********************'+fonts.BRANCO)


    elif f == "4":
        clear()
        i=0 # iniciar a variavel i em 0 para verificar que não há conflitos entre opções diferentes
        file=open('dispensa.txt','w') #abre o ficheiro list.txt para escrever informação
        for i in range(len(prods)): #o ciclo percorre a lista prods
            file.write(prods[i].save()) #executa a função save e grava o output no ficheiro
        file.close() #feicha o ficheiro
        print(fonts.AMARELO+'A gravar...'+fonts.BRANCO)


    elif f == "0":
        clear()
        i=0 # iniciar a variavel i em 0 para verificar que não há conflitos entre opções diferentes
        file=open('dispensa.txt','w') #abre o ficheiro list.txt para escrever informação
        for i in range(len(prods)): #o ciclo percorre a lista prods
            file.write(prods[i].save()) #executa a função save e grava o output no ficheiro
        file.close() #feicha o ficheiro
        print(fonts.AMARELO+'A gravar...')
        print('A encerrar')

    else:
        clear()
        print(fonts.AMARELO+'Opção inválida. Tente novamente')
