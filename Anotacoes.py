n = input("Digite algo: ")
print(type(n))
print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())

# Ordem de precedência dos operadores aritméticos
# 1-Parênteses ()
# 2-Potências **
# 3-Multiplicação *, Divisão /, Divisão inteira //, Resto da Divisão % (na ordem de aparecimento da esquerda-direita)
# 4-Mais e Menos (na ordem de aparecimento da esquerda-direita)

#Para limitar casas decimais num format - {:.Xf} sendo o X o número de casas decimais que eu quero {:.2f} mostrará duas casas flutuantes

#Para não quebrar a linha e juntar dois prints, colocar end=''

#Fatiamento de string

print('''Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(), upper(),
lower(), capitalize(), title(), strip(), junção com join().''')
# Usar três aspas no início e fim da frase, ela sera mostrada conforme está no código, pulando linhas

frase = 'Curso em Vídeo Python'

print(frase[9]) #Mostra somente o décimo caractere da string (contagem começa em zero)
print(frase[9:13]) #Range - Mostra do décimo caractere da string até do décimo terceiro, o caractere número 13 ele não mostra
print(frase[9:21:2]) #Mostra do número nove até o número 21, pulando dois e mostrando o segundo caractere
print(frase[:5]) #Mostra do zero até o cinco
print(frase[15:]) #Mostra do caractere 15 até o último caractere da string
print(frase[9::3]) #Começa no nove, vai até o último char., pulando três

len(frase) #Retorna o comprimento da str
frase.count('o') #Conta a quantidade de letras 'o' na str e retorna o total
frase.count('o',0,13) #Conta a quantidade de letras 'o' da posição 0 até a 12
frase.find('deo') #Retorna em qual posição inicia a frase 'deo'
frase.find('Android') #Como não existe a frase 'Android' dentro da string, ele retorna o valor '-1'
'Curso' in frase #Retorna True, ou False se não encontrar a frase 'Curso' dentro da str
frase.replace('Python','Android') #Troca a frase Python pela frase Android dentro da str
frase.upper() #Coloca toda a str em maiúscula
frase.lower() #Coloca toda a str em minúcula
frase.capitalize() #Joga TUDO para minúsculo e depois somente a primeira letra da str para maiúsculo
frase.title() #Coloca todas as palavras com a primeira letra em maiúscula
frase.strip() #Remove todos os espaços inúteis na str, mas mantém um espaço aonde se separa as palavras
frase.rstrip() #Remove os espaços inúteis na Direita da str
frase.lstrip() #Remove os epaços inúteis na Esquerda da str
frase.split() #Separa a str em palavras, usando os espaços como divisor (Curso)(em)(Vídeo)(Python)
'-'.join(frase) #Após sofre split, uma str pode ser conectada através do Join, nesse caso será com o traço '-' (Curso-em-Vídeo-Python)
    
#Dicionários - abrem e fehcam com chaves {}
filme = {'título':'Star Wars',
        'ano':1977,
        'diretor':'George Lucas'}

print(filme.values()) #Mostra todos os valores no dicionário filme
print(filme.keys()) #Mostra o nome das chaves do dicionário filme
print(filme.items()) #Mostra tanto os valores quanto as chaves

pessoas ={'nome':'Gustavo', 'sexo':'M', 'idade':22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos. ' )

for key, value in pessoas.items():
    print(f'{key} = {value}')

pessoas['nome'] = 'Leandro' #Modifica o valor da chave nome no dicionário
pessoas['peso'] = 85 #Adiciona uma chave e um valor no dicionário já criado

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input("Unidade Fderativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy()) #Copia o dicionário para dentro da lista, no dicionário não funciona o fatiamento [:]

def contador(*num):
    print(num)

contador(2,1,8,5)

def dobra(lst):
    """
    Pega uma lista de qualquer tamanho e dobra cada valor dela
    """
    pos = 0
    while pos < lst(len):
        lst[pos] *=2
        pos += 1

help(dobra) 

valores=[6,3,9,1,0,2]
dobra(valores)
print(valores)

print(print.__doc__)