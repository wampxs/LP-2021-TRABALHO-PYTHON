import sys

''' 
    AUTORES:
    Andre F. Maia
    João Paulo S. de Mendonça
    Diogo Barros de Rezende
'''

'''     #PARADIGMAS#      '''

'''     IMPERATIVO      '''


def paradigmaImperativo():
    x = int(input("Digite um número: "))
    print("O x foi declarado: " + str(x))
    x += 5
    print("Acrescentamos 5 ao valor de x: " + str(x))
# O Paradigma Imperativo consiste em ser capaz de dar instruções ao computador.

'''     FUNCIONAL       '''


def func(x):
    y = x ** 2 + 3 * x
    return y


def paradigmaFuncional():
    x = int(input("Digite um número: "))
    print("Passando x como " + str(x) + " na função 'x^2 + 3x' resulta em: " + str(func(x)))

# O Paradigma Funcional consiste em utilizar funções assim como na matemática.
# Ou seja, são caixas pretas que recebem e retornam valores conforme uma equação.

'''     ORIENTADO A OBJETOS     '''


class triangulo: # criação de uma classe "triangulo"
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # A construtora da classe é dada pela função __init__ (initializer).
    # Todos os métodos de uma classe recebem o argumento 'self', que aponta ao objeto instanciado que o invocou.
    # Aqui, serão recebidos os valores de cada lado (a,b e c). Em seguida, serão atribuídos aos elementos da classe.

    def imprimeLados(self):
        print("Lado A: " + str(self.a) + " Lado B: " + str(self.b) + " Lado C: " + str(self.c))

    # Este método simples irá imprimir cada lado do objeto que o chamou.

    def isEquilatero(self):
        return(self.a==self.b and self.b==self.c and self.a==self.c)

    # Este método irá verificar se o triângulo que o chama é equilátero (se a == b == c) e retorna a resposta (bool)

def paradigmaPOO():
    x = triangulo(3, 3, 3) # É passado o valor 3 para os lados a, b e c
    y = triangulo(5, 5, 2) # São passados os valores 5 (a e b) e 2 (c)
    print("Imprimindo os lados do triângulo x: ")
    x.imprimeLados()
    print("Imprimindo os lados do triângulo y: ")
    y.imprimeLados()
    print("X é Equilátero? = " + str(x.isEquilatero()))
    print("Y é Equilátero? = " + str(y.isEquilatero()))


'''     PROCEDURAL      '''


def HW(): # Função que imprime 2 strings
    print("Hello World!")
    print("Now, Goodbye!")


def paradigmaProcedural():
    x = 5
    print("A cada passo que afetarmos a variável x, vamos chamar a função HW().")
    x += 1
    print("x+=1 = " + str(x))
    HW()
    x += 4
    print("x+=4 = " + str(x))
    HW()
    x = 0
    print("x = " + str(x))
    print(x)
    HW()

# O Paradigma Procedural envolve chamar funções que desviam a sequência de execução do código.
# Em Python, o código sempre é lido do começo até o fim, mas procedimentos causam uma mudança na ordem de forma segura.

'''     #TIPOS#     '''


def tipoIntFloat():
    x = 5 # Um valor inteiro infere o tipo int
    y = 5.5 # Um valor racional infere o tipo float
    print("x = 5")
    print("y = 5.5")
    print("Tipo de X: " + str(type(x)))
    print("Tipo de Y: " + str(type(y)))


def tipoString():
    s = 'Hello World!' # Caracteres expressados entre aspas inferem o tipo string
    print("print(s) = " + s)
    print("print(s[0:5]) = " + s[0:5])
    # Aqui, é usado o operador slice para obter o trecho de caracteres de 0 a 5 na string.
    print("print(s[::-1]) = " + s[::-1])
    # O operador slice também permite um intervalo na exibição da string.
    # Neste caso, um intervalo de -1 imprime a string ao contrário.

def tipoBool():
    x = True
    y = False
    # Os termos 'True' e 'False' inferem o tipo bool.
    print("x = True")
    print("y = False")
    print("x and y = " + str(x and y)) # Aqui, é feito um AND entre x e y
    print("x or y = " + str(x or y)) # Aqui, é feito um OR entre x e y


def tipoList():
    x = [1, 2, 3] # O tipo list é inferido com uma lista de elementos separados por vírgulas, e entre colchetes [].
    print("x = " + str(x))
    print(type(x))
    x[1] = 4 # Aqui, o elemento na posição 1 (2) é substituído pelo número 4.
    print("Após alterar a posição '1' para 4: " + str(x))


def tipoTuple():
    x = (1, 2, 3) # O tipo tuple é inferido com uma lista de elementos separados por vírgulas, e entre parênteses ().
    y = (4, 'cinco', 6.6, True)
    print("x = " + str(x))
    print("y = " + str(y))
    print(type(x))
    print("x + y = " + str(x + y)) # Concatenação dos elementos de x com y.
    print("4 in x = " + str(4 in x)) # Verificando se '4' está na tupla x.


def tipoDict():
    x = {'Nome': 'Roberto', 'Idade': 47}
    # O Dict é inferido com pares de chaves e elementos (separados por :), separados por vírgulas, e entre chaves {}.
    print("x = " + str(x))
    print(type(x))
    print("x['Nome'] = " + x['Nome']) # É feita a recuperação do elemento identificado pela chave 'Nome'.
    print("x.keys() = " + str(x.keys())) # Recupera-se todas as chaves do dict x


def tipoSet():
    x = {'a', 'b', 'c'}
    # O tipo set é inferido com uma lista de elementos separados por vírgulas, e entre chaves {}.
    # Também pode ser inferido com: x = set(['a','b','c'])
    y = frozenset(['b', 'c', 'd'])
    # O tipo frozenset (set imutável) é inferido com a função frozenset(), recebendo um array de elementos.
    print("x = " + str(x))
    print("y = " + str(y))
    print("'b' in x = " + str('b' in x)) # Verificando se 'b' está em x
    print("'d' in x = " + str('d' in x)) # Verificando se 'd' esta´em x
    print("x.union(y) = " + str(x.union(y))) # Fazendo a união de x com y (não repete valores)
    print("x.difference(y) = " + str(x.difference(y)))
    # Extraindo a diferença de x com y (qual elemento de x não está em y)


def tipoComplex():
    x = 3 + 2j
    # O tipo complex é inferido com uma atribuição de um número complexo (número real + número imaginário).
    # O número imaginário é acompanhado por um 'j'.
    y = complex(3, 2)
    # Também pode-se usar a função complex(), que recebe o real e imaginário, respectivamente.
    print("x = 3+2j")
    print("y = complex(3,2)")
    print("x == y = " + str(x == y))
    print("x = " + str(x))
    print(type(x))
    print("x.real = " + str(x.real)) # Imprimindo o número real
    print("x.imag = " + str(x.imag)) # Imprimindo o número imaginário


'''     #ESTRUTURAS#     '''

'''     CONDICIONAL     '''


def condicional():
    numero = 1
    if numero == 1: # O if recebe uma condição para verificar. Se a condição é 'True', irá executar o bloco indentado.
        print('Numero 1')
    elif numero == 2: # Caso a condição do if seja False, o elif irá realizar outro if em seguida, com outra condição.
        print('Numero 2')
    else: # Se nenhum if/elifs forem executados, o bloco do else será executado.
        print('Não é 1, nem 2')


'''     REPETIÇÃO     '''


def repeticao():
    Lista = ['Banana', 'Arroz', 'Manteiga'] # Declaração de uma lista
    for item in Lista:
        print(item, end=', ')
    # Aqui, o for irá resgatar cada valor da 'Lista' e atribuí-los ao 'item', até que alcance o fim da Lista.
    # A cada item resgatado, o bloco indentado será resgatado.
    a = 5
    for i in range(5):
        print(i, end=', ')
    # Este for irá atribuir a i, a cada iteração, os valores de 0 até 5-1 (0,1,2,3,4).
    while a != 0:
        print(a, end=', ')
        a -= 1
    # O while irá executar o bloco indentado em loop até que a condição seja cumprida.

'''     EXCEÇÃO     '''


def excecoes():
    x = 1
    try:
        print(x) # O programa lerá x normalmente
        print(y) # Aqui ocorrerá um erro, já que y não foi declarado nesse escopo.
    except:
        print("Alguma coisa deu errado!") # Ao passar por um erro, esse bloco será executado.
    finally:
        print("Finalização de estrutura") # Após a execução do try/except, esse bloco será executado.

    # Na estrutura de exceção, o bloco indentado após o try será rodado normalmente
    # Caso ele encontre um erro durante a execução, o programa irá passar para o bloco do except.
    # Por fim, se houver um finally, seu bloco será executado após ambos try e except.


'''     #RECURSIVIDADE#     '''

'''     CONTAGEM REGRESSIVA     '''

# A recursividade consiste em chamar uma função dentro de si mesma, passando valores diferentes para alguma finalidade.
# Isso irá resultar em um loop recursivo, que será parado quando um if for cumprido e a função não for mais chamada.

def contagemRegressiva(n): # A função recebe um valor n
    if n == 0: # Caso o valor recebido seja 0, a recursão será parada.
        print('Terminou!')
    else:
        print(n)
        contagemRegressiva(n - 1)
        # Aqui é passado o valor de n-1, ou seja, a cada chamada da função haverá uma subtração em n
        # Eventualmente, n chegará a 0 e a recursão será interrompida pelo if.


'''     FIBONACCI       '''


def recur_fibo(n):  # Declaração da função
    if n <= 1: # Caso n <= 1...
        return n # Retorna n, encerrando o loop
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)
        # Retorna n-1 + n-2, que através da recursão gerará o número correspondente na sequência de Fibonacci


def fibonacci():
    nterms = int(input("Inserir um numero positivo: "))
    print("Sequência de Fibonacci = ")
    for i in range(nterms): # Realizar a recursão n vezes, obtendo n termos da sequência de Fibonacci
        print(recur_fibo(i), end=' ')  # chamada da função


'''     #REFERENCE COUNTING#     '''

# No Python, todos os objetos possuem um valor que indica quantas vezes aquele objeto é apontado no programa.
# Isso é utilizado para que o Garbage Collector possa desalocar a variável da memória quando não possui mais referências

def refcount():
    var1 = 10 # A variável var1 é criada.
    var2 = var1 # A variável var2 é apontada para o valor de var1, criando uma referência.
    var3 = var1 # A variável var3 cria mais uma referência a var1.
    print("Numero de referencias =", sys.getrefcount(var1))
    # A função retorna a quantidade de referências do objeto, através do módulo 'sys'.


'''     MAIN        '''
# Menu para a seleção de exemplos na execução.
sel = -1
sel2 = -1
while sel != 0:
    try:
        sel = int(input("\n[1] PARADIGMAS\n[2] TIPOS\n[3] ESTRUTURAS\n[4] RECURSIVIDADE\n[5] REFERENCE COUNTING\n[0] ENCERRAR\n"))
    except:
        print("Erro!")
    if sel == 1:
        try:
            sel2 = int(input("Escolha um Exemplo:\n[1] PARADIGMA IMPERATIVO\n[2] PARADIGMA FUNCIONAL\n[3] PARADIGMA ORIENTADO A OBJETOS\n[4] PARADIGMA PROCEDURAL\n"))
        except:
            print("Erro!")
        if sel2 == 1:
            print("\nPARADIGMA IMPERATIVO:\n ")
            paradigmaImperativo()
            print("\nAperte ENTER...")
            input()
        elif sel2 == 2:
            print("\nPARADIGMA FUNCIONAL:\n ")
            paradigmaFuncional()
            print("\nAperte ENTER...")
            input()
        elif sel2 == 3:
            print("\nPARADIGMA ORIENTADO A OBJETOS:\n ")
            paradigmaPOO()
            print("\nAperte ENTER...")
            input()
        elif sel2 == 4:
            print("\nPARADIGMA PROCEDURAL:\n ")
            paradigmaProcedural()
            print("\nAperte ENTER...")
            input()
        else:
            print("Inválido!")
    elif sel == 2:
        try:
            sel2 = int(input("Escolha um Exemplo:\n[1] INT/FLOAT\n[2] STRING\n[3] BOOL\n[4] LIST\n[5] TUPLE\n[6] DICT\n[7] SET/FROZENSET\n[8] COMPLEX\n"))
        except:
            print("Erro!")
        if sel2 == 1:
            print("\nTIPO INT/FLOAT:\n ")
            tipoIntFloat()
            print("\nAperte ENTER...")
            input()
        elif sel2 == 2:
            print("\nTIPO STRING:\n ")
            tipoString()
            print("\nAperte ENTER...")
            input()
        elif sel2 == 3:
            print("\nTIPO BOOL:\n ")
            tipoBool()
            print("\nAperte ENTER...")
            input()
        elif sel2 == 4:
            print("\nTIPO LIST:\n ")
            tipoList()
            print("\nAperte ENTER...")
            input()
        elif sel2 == 5:
            print("\nTIPO TUPLE:\n ")
            tipoTuple()
            print("\nAperte ENTER...")
            input()
        elif sel2 == 6:
            print("\nTIPO DICT:\n ")
            tipoDict()
            print("\nAperte ENTER...")
            input()
        elif sel2 == 7:
            print("\nTIPO SET/FROZENSET:\n ")
            tipoSet()
            print("\nAperte ENTER...")
            input()
        elif sel2 == 8:
            print("\nTIPO COMPLEX:\n ")
            tipoComplex()
            print("\nAperte ENTER...")
            input()
        else:
            print("Inválido!")
    elif sel == 3:
        try:
            sel2 = int(input("Escolha um Exemplo:\n[1] CONDICIONAL\n[2] REPETIÇÃO\n[3] EXCEÇÃO\n"))
        except:
            print("Erro!")
        if sel2 == 1:
            print("\nESTRUTURA CONDICIONAL:\n ")
            condicional()
            print("\nAperte ENTER...")
            input()
        elif sel2 == 2:
            print("\nESTRUTURA DE REPETIÇÃO:\n ")
            repeticao()
            print("\nAperte ENTER...")
            input()
        elif sel2 == 3:
            print("\nESTRUTURA DE EXCEÇÃO:\n ")
            excecoes()
            print("\nAperte ENTER...")
            input()
        else:
            print("Inválido!")
    elif sel == 4:
        try:
            sel2 = int(input("Escolha um Exemplo:\n[1] CONTAGEM REGRESSIVA\n[2] SEQUÊNCIA DE FIBONACCI\n"))
        except:
            print("Erro!")
        if sel2 == 1:
            print("\nCONTAGEM REGRESSIVA RECURSIVA:\n ")
            contagemRegressiva(10)
            print("\nAperte ENTER...")
            input()
        elif sel2 == 2:
            print("\nSEQUÊNCIA DE FIBONACCI REGRESSIVA:\n ")
            fibonacci()
            print("\nAperte ENTER...")
            input()
        else:
            print("Inválido!")
    elif sel == 5:
        print("\nEXEMPLO DE REFERENCE COUNTING:\n ")
        refcount()
        print("\nAperte ENTER...")
        input()
    else:
        sel = 0
