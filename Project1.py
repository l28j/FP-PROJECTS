
#João Lucas Morais Cardoso Tavares Rodrigues
#ist1106221
#28/10/2022
#joao.lucas.m.c.t.r@tecnico.ulisboa.pt	

###########EXERCICIO 1#################

def limpa_texto(cadeia):
    """limpa texto: cad. carateres -> cad. carateres
    Esta funcao recebe uma cadeia de carateres qualquer e devolve a cadeia de carateres
    limpa que corresponde a remocao de carateres brancos conforme descrito.""" 
    cadeia_limpa = cadeia.split()
    cadeia_resultado = (' '.join(cadeia_limpa))         #Separa a cadeia num tuplo e retorna com apneas um espaco entre caracteres
    return cadeia_resultado

def corta_texto(cadeia,largura):
    """corta texto: cad. carateres x inteiro → cad. carateres x cad. carateres 
    Recebe uma string e um inteiro positivo correspondentes a
    um texto limpo e uma largura, e devolve duas string limpas : a primeira contendo todas as palavras completas desde o inicio
    da cadeia original (incluindo os espacos separadores entre elas) com a largura, e a segunda cadeia contendo o resto do texto de
    entrada."""
    cadeia_cortada = cadeia.split()
    subcadeia_1 = ()
    subcadeia_2 = ()
    ultima_palavra = 0
    if len(cadeia) == 0:
        return ('', '')                             
    for palavra in cadeia_cortada:     
        if len(palavra) <= largura:      
            subcadeia_1 += (palavra, )         #Adiciona palavras a priemria subcadeia enquanto esta ainda for menor ou igual a largura
            largura -= (len(palavra) + 1)                  
        else:
            break
    ultima_palavra = cadeia_cortada.index(subcadeia_1[-1])      #Procura o indice da ultima palavra da subcadeia 1
    for i in range(ultima_palavra + 1, len(cadeia_cortada)):    #Procura os indices de todas as restantes palavras 
        subcadeia_2 += (cadeia_cortada[i], )                    #Soma as restantes palavras da cadeia inicial
    return (' '.join(subcadeia_1),' '.join(subcadeia_2))        #Adiciona as duas subcadeias

def insere_espacos(cadeia,largura):
    """insere espacos: cad. carateres x inteiro → cad. carateres
    Recebe uma cadeia de carateres e um inteiro positivo correspondentes a um
    texto limpo e uma largura de coluna respetivamente, e no caso da cadeia de entrada
    conter duas ou mais palavras devolve uma cadeia de carateres de comprimento igual
    a largura da coluna formada pela cadeia original com espacos entre palavras conforme
    descrito. Caso contrario, devolve a cadeia de comprimento igual a largura da coluna
    formada pela cadeia original seguida de espacos."""
    cadeia_cortada = cadeia.split()
    cadeia_resultado = cadeia_cortada
    if len(cadeia_cortada) >= 2:
        i = 0
        while i < largura - len(cadeia):       #Largura-len(cadeia) corresponde ao numero de espaços necessários a adicionar
            for palavra in cadeia_cortada:
                if not palavra == cadeia_cortada[-1]:    #Se não for a ultima palavra
                    i += 1
                    if i <= largura - len(cadeia):   
                        cadeia_resultado[cadeia_cortada.index(palavra)] = (palavra + ' ')   #Adiciona as palavras com os respetivos espaços à frente     
    else:
        for i in range(largura - len(cadeia)):
            cadeia += ' '
        return cadeia                     #Caso seja uma unica palavra o programa irá apenas adicionar espaços no fim da palavra
    return (' '.join(cadeia_resultado))

def justifica_texto(cadeia,largura):
    '''justifica texto: cad. carateres x inteiro → tuplo
    Recebe uma cadeia de carateres nao vazia e um inteiro positivo correspondentes a um texto qualquer e uma largura de coluna respetivamente, e devolve um tuplo
    de cadeias de carateres justificadas, de comprimento igual a largura da coluna
    com espacos entre palavras conforme descrito. Fazendo tambem a verificacao de argumentos.'''
    if not isinstance(largura,int): 
        raise ValueError('justifica_texto: argumentos invalidos')
    elif not isinstance(cadeia,str):
        raise ValueError('justifica_texto: argumentos invalidos')      #Erros possiveis
    elif len(limpa_texto(cadeia)) == 0:
        raise ValueError('justifica_texto: argumentos invalidos')
    
    cadeia_limpa = limpa_texto(cadeia)
    for palavra in cadeia_limpa.split():
        if len(palavra) > largura:
            raise ValueError('justifica_texto: argumentos invalidos')   #Erro caso haja uma palvra maior que a largura inserida
    cadeia_temp = cadeia_limpa
    cadeia_cortada = ()
    while True:
        subcadeia_1 = corta_texto(cadeia_temp,largura)[0]     
        subcadeia_2 = corta_texto(cadeia_temp,largura)[1]
        cadeia_cortada += (subcadeia_1, )           
        if len(subcadeia_2) > largura:          #Loop em que corta a primeira subcadeia com a respetiva largura e adiciona a cadeia cortada
            cadeia_temp = subcadeia_2           #e caso a segunda seja maior que a largura assume que a cadeia temporaria eh a segunda subcadeia
        else:                                   #retornando denovo enquanto a segunda cadeia a ser analisada for maior que a largura
            if not len(subcadeia_2) == 0:       #e adicionando a nova subcadeia1 ao cadeia cortada
                cadeia_cortada += (subcadeia_2, )
            break
    cadeia_resultado = ()
    for linha in cadeia_cortada:
        if not len(linha) == largura and not linha == cadeia_cortada[-1]:
            cadeia_resultado += (insere_espacos(linha,largura), )   #Adiciona espacos caso a largura da linha nao corresponda ao pedido
        else:
            linha_final = linha
            for i in range(largura - len(linha)):
                linha_final += ' '                     #Caso a ultima linha nao tenha a respetiva largura esta irá adicionar espacos a mesma               
            cadeia_resultado += (linha_final, )         
    return cadeia_resultado

###########EXERCICIO 2#################



def copiar_dicionarios(dic):
    """Funcao auxiliar que recebe um dicionario e cria copias do mesmo"""
    copia = {}
    for chave, valor in dic.items():   #Funcao auxiliar que cria copias do dicionario original para iteracoes no mesmo
        copia[chave] = valor
    return copia


def calcula_quocientes(votos,n_mandatos):
    '''calcula quocientes: dicionario x inteiro → dicionario
    Recebe um dicionario com os votos apurados num circulo e um inteiro positivo representando o numero de deputados; e devolve o
    dicionario com as mesmas chaves do dicionario argumento (correspondente a partidos)
    contendo a lista (de comprimento igual ao numero de deputados) com os quocientes
    calculados com o metodo de Hondt ordenados em ordem decrescente.'''
    copia_votos = copiar_dicionarios(votos)
    for partido in copia_votos:
        quocientes = []                         #Cria todos os quocientes de cada partido com os respetivos numeros de mandatos em um dicionario
        for indice in range(n_mandatos):
            quocientes.append(copia_votos[partido] / (indice + 1))
        copia_votos[partido] = quocientes
    return copia_votos


def atribui_mandatos(votos,n_mandatos):
    '''atribui mandatos: dicionario x inteiro → lista
    Recebe um dicionario com os votos apurados num circulo e um inteiro representando o numero de deputados, e devolve a lista ordenada de tamanho igual ao
    numero de deputados contendo as cadeias de carateres dos partidos que obtiveram cada
    mandato, isto e, a primeira posicao da lista corresponde ao nome do partido que obteve
    o primeiro deputado, a segunda ao partido que obteve o segundo deputado, etc. Considere que no caso de existirem dois ou mais partidos com igual quociente, os mandatos
    sao distribuidos por ordem ascendente as listas menos votadas.'''
    mandatos_final = []
    copia_votos = copiar_dicionarios(votos)  #Copia do dicionario original
    valores_iniciais = votos.values()        #Valores iniciais dos votos
    for indice in range(n_mandatos):
        mandatos = []
        valores = []
        quocientes = calcula_quocientes(votos,n_mandatos)  
        escolhido = []
        
        for partido in copia_votos:
            valores.append(copia_votos[partido]) #Valores dos votos
          
        for partido in copia_votos:
            if copia_votos[partido] == max(valores):   #Procura o valor maximo dos votos e adiciona a lista mandatos os respetivos partidos
                mandatos.append(partido)
        
        if len(mandatos) == 1:
            escolhido.append(mandatos[0])   #Caso os mandatos so tenham um partido com esse respetivo valor max esse sera o escolhido
        
        if len(mandatos) >= 2:
            for partido in mandatos:
                if votos[partido] == min(valores_iniciais): #Senao ira escolher o partido com o valor minimo para desempate
                    escolhido = [partido]

        escolhido = ''.join(escolhido)    #Adiciona o escolhido a lista esolhido
        mandatos_final.append(escolhido)  #Adiciona o escolhido a lista mandatos
        if indice < n_mandatos - 1:
            indice_quociente_atual = quocientes[escolhido].index(copia_votos[escolhido]) #Indice atual sera o do escolhido no respetivo dicionario
            copia_votos[escolhido] = quocientes[escolhido][indice_quociente_atual + 1] #Ira analisar os votos do quociente seguinte para continuar a executar no loop

    return mandatos_final


def obtem_partidos(votos):
    '''obtem partidos: dicionario → lista
    Recebe um dicionario com a informacao sobre as eleicoes num territorio
    com varios circulos eleitorais como descrito, e devolve a lista por ordem alfabetica com
    o nome de todos os partidos que participaram nas eleicoes.'''
    deputados = []
    for cirulos in votos.values():
        for letra in cirulos['votos']:   #Procura os partidos nos votos e adiciona os a uma lista
            deputados.append(letra)         
     
    deputados_filtrados = []        
    for indice in deputados:
        if not indice in deputados_filtrados:      #Adiciona apenas os partidos que nao se encontram na lista ou seja apenas uma incidencia por cada partido
            deputados_filtrados.append(indice)      
    deputados_filtrados.sort()                     #Ordena os partidos por ordem alfabetica 

    return deputados_filtrados

def levantar_erros_eleicoes(votos):
    """Funcao auxiliar para levantamento de erros possiveis"""
    if not isinstance(votos,dict) or len(votos) == 0:
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')
    
    for i in votos:
        if not isinstance(votos[i],dict) or len(votos[i]) == 0 or not isinstance(i,str):
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        elif 'votos' not in votos[i].keys() or 'deputados' not in votos[i].keys():
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        elif len(votos[i].keys()) > 2:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        elif not isinstance(votos[i]['votos'],dict) or not isinstance(votos[i]['deputados'],int):  #Funcao auxiliar criada para procura de erros
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        elif votos[i]['deputados'] < 1:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        
        votos_totais_circulo = 0
        for n in votos[i]['votos']:
            if not isinstance(n,str) or not isinstance(votos[i]['votos'][n],int):
                raise ValueError('obtem_resultado_eleicoes: argumento invalido')
            elif votos[i]['votos'][n] < 0:
                raise ValueError('obtem_resultado_eleicoes: argumento invalido')
            votos_totais_circulo += votos[i]['votos'][n]
            
        if votos_totais_circulo == 0:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')

def ordenar_resultados(resultados):
    """Funcao auxiliar para ordenar os resultados eleitorais"""
    for i in range(len(resultados) - 1):
        for j in range(len(resultados) - 1 - i):                #Funcao auxiliar para ordenar os resultados das eleicoes
            if resultados[j][1] < resultados[j + 1][1]:
                resultados[j], resultados[j + 1] = resultados[j + 1], resultados[j]
            elif resultados[j][1] == resultados[j + 1][1]:
                if resultados[j][2] < resultados[j + 1][2]:
                    resultados[j], resultados[j + 1] = resultados[j + 1], resultados[j]
    return resultados
        

def obtem_resultado_eleicoes(votos):  
    '''obtem resultado eleicoes: dicionario → lista
    Executa primeiro a funcao de levantamento de erros
    Recebe um dicionario com a informacao sobre as eleicoes num territorio com
    varios circulos eleitorais como descrito, e devolve a lista ordenada de comprimento igual
    ao numero total de partidos com os resultados das eleicoes. Cada elemento da lista e
    um tuplo de tamanho 3 contendo o nome de um partido, o numero total de deputados
    obtidos e o numero total de votos obtidos. A lista esta ordenada por ordem descendente de acordo ao numero de deputados obtidos e, em caso de empate, de acordo ao
    numero de votos.'''
    levantar_erros_eleicoes(votos) #Chamar a funcao que levanta erros, para certificar que a funcao pode ser executada
    partidos_obtidos = obtem_partidos(votos) #lista com os nomes dos partidos
    soma = {}              
    for chave in partidos_obtidos:
        soma[chave] = 0   #Criar um dicionario com os nomes dos partidos(chaves) a corresponder a 0(valores)

    mandatos = []
    circulos = []  
    for c in votos:    
        circulos.append(votos[c])  #Adicionar os valores do dicionario original a uma lista
    for circulo in circulos:
        for partido in partidos_obtidos:
            if partido in circulo['votos'].keys():
                soma[partido] = soma[partido] + circulo['votos'][partido]  #Somar os votos de cada partido em todos os circulos eleitorais
        mandatos = mandatos + atribui_mandatos(circulo['votos'],circulo['deputados'])  #Adicionar a uma lista os partidos com deputados

    resultado_eleicoes = []
    for partido in partidos_obtidos:
        n_mandatos = 0
        for indice in mandatos:
            if indice == partido:
                n_mandatos += 1  #Contar os deputados por partido
        resultado_eleicoes.append((partido,n_mandatos,soma[partido])) #Criar um tuplo por partido com as infos nome, numero de deputados e numero de votos e adicionar a uma lista  

    return ordenar_resultados(resultado_eleicoes)  #Ordenar a lista de tuplos segundo a funcao definida anteriormente


###########EXERCICIO 3#################

def produto_interno(primeiro_vetor,segundo_vetor):
    '''produto interno: tuplo x tuplo → real
    Esta funcao recebe dois tuplos de numeros (inteiros ou reais) com a mesma dimensao
    representando dois vetores e retorna o resultado do produto interno desses dois vetores.'''
    produto_interno = 0.0
    for i in range(len(segundo_vetor)):                    
        produto_interno += primeiro_vetor[i] * segundo_vetor[i]    #Executa o produto interno entre os vetores

    return produto_interno

def verifica_convergencia(matriz,constantes,lista_x,precisao):
    '''verifica convergencia: tuplo x tuplo x tuplo x real → booleano
    Recebe tres tuplos de igual dimensao e um valor real positivo. Primeiro
    tuplo e constitido por um conjunto de tuplos cada um representando uma linha da
    matriz quadrada A, e os outros dois tuplos de entrada contem valores representando
    respetivamente o vetor de constantes c e a solucao atual x. O valor real de entrada
    indica a precisao pretendida ϵ. A funcao retorna True caso o valor absoluto do
    erro de todas as equacoes seja inferior a precisao, |fi(x)-ci| < ϵ, e False caso contrario.'''
    resultado = ()
    for i in range(len(matriz)):  #por cada linha da matriz
        if abs(produto_interno(matriz[i], lista_x) - constantes[i]) < precisao: #Verificar se a diferença entre o produto interno e a variavel independente e menor que a precisao
            resultado += (True, )
        else:
            resultado += (False, )

    return all(resultado)  #Devolve o valor bool do tuplo resultado (se todos forem True devolve True, caso contrario devolve False)

def retira_zeros_diagonal(matriz,constantes):
    '''retira zeros diagonal: tuplo x tuplo → tuplo x tuplo
    Recebe um tuplo de tuplos, representando a matriz de entrada no mesmo
    formato das funcoes anteriores, e um tuplo de numeros, representando o vetor das constantes. A funcao retorna uma nova matriz com as mesmas linhas que a de
    entrada, mas com estas reordenadas de forma a nao existirem valores 0 na diagonal. O
    segundo parametro de saida e tambem o vetor de entrada com a mesma reordenacao de
    linhas que a aplicada a matriz. Para este efeito, e de forma a uniformizar o resultado,
    devera inspecionar por ordem todas as linhas da matriz a procura de um 0 na diagonal.
    Se na linha i se encontrar um 0 na diagonal, esta linha deve ser trocada pela primeira
    linha j que, procurando desde o inicio da matriz, nao contenha um 0 na coluna i, sempre
    que na linha i nao haja um 0 na coluna j.'''
    constantes_lista = list(constantes)
    matriz_lista = list(matriz)
    for i in range(len(matriz_lista)):
        if matriz_lista[i][i] == 0:  #Se o elemento da diagonal for 0
            for j in range(len(matriz_lista)):
                if not matriz_lista[i][j] == 0 and not matriz_lista[j][i] == 0 and not j == i: #Confirmar que as linhas podem ser trocadas
                    constantes_lista[i], constantes_lista[j] = constantes_lista[j], constantes_lista[i] #Trocar os valores do tuplo das constantes
                    matriz_lista[i], matriz_lista[j] = matriz_lista[j], matriz_lista[i]  #Trocar a posicao das linhas para nao haver zeros na diagonal
                    break

    return tuple(matriz_lista),tuple(constantes_lista)

def eh_diagonal_dominante(matriz):
    '''eh diagonal dominante: tuplo → booleano
    Esta funcao recebe um tuplo de tuplos representando uma matriz quadrada no mesmo
    formato das funcoes anteriores. Devera retornar True caso seja uma matriz diagonalmente dominante, e False caso contrario.'''
    for linha in range(len(matriz)):
        soma = 0
        for coluna in range(len(matriz)):
            if not linha == coluna:                          #Procura os elemetos pertencentes a diagonal principal da matriz
                soma = soma + abs(matriz[linha][coluna])     #Soma os respetivos valores absolutos
        if abs(matriz[linha][linha]) < soma:                 #Verifica se a soma dos valores absolutos e menor que o valor absoluto da entrada da diagonal principal
            return False
    return True

def resolve_sistema(matriz,constantes,precisao):
    '''resolve sistema: tuplo x tuplo x real → tuplo
    Primeiramente verifica todos o serros
    Esta funcao recebe um tuplo de tuplos representando uma matriz quadrada no mesmo
    formato das funcoes anteriores correspondente aos coeficientes das equacoes do sistema,
    um tuplo de numeros representando o vetor das constantes, e um valor real positivo
    correspondente a precisao pretendida para a solucao. Devera retornar um tuplo que e
    a solucao do sistema de equacoes de entrada aplicando o metodo de Jacobi descrito.
    Considere para este efeito que o valor inicial para todas as variaveis do sistema de
    equacoes e igual a 0.'''
    if not isinstance(matriz,tuple) or not isinstance(constantes,tuple) or not isinstance(precisao,float):
        raise ValueError('resolve_sistema: argumentos invalidos')
    elif not len(constantes) == len(matriz) or precisao <= 0 or precisao >= 1:
        raise ValueError('resolve_sistema: argumentos invalidos')
    for indice in range(len(matriz)):
        if not isinstance(matriz[indice],tuple):
            raise ValueError('resolve_sistema: argumentos invalidos')
        elif not len(matriz[indice]) == len(matriz):                                                #Erros possiveis
            raise ValueError('resolve_sistema: argumentos invalidos')
        elif not isinstance(constantes[indice],float) and not isinstance(constantes[indice],int):
            raise ValueError('resolve_sistema: argumentos invalidos')
        for k in range(len(matriz[indice])):
            if not isinstance(matriz[indice][k],int) and not isinstance(matriz[indice][k],float):
                raise ValueError('resolve_sistema: argumentos invalidos')
    matriz_resultado = retira_zeros_diagonal(matriz,constantes)[0]   #Tuplo matriz sem zeros diagonal
    const_resultado = retira_zeros_diagonal(matriz,constantes)[1]    #Tuplo constantes com as mesmas trocas que a matriz
    if not eh_diagonal_dominante(matriz_resultado):   #Verificar se a matriz e diagonal dominante
        raise ValueError('resolve_sistema: matriz nao diagonal dominante')
    lista_x = []
    ultimo_x = []
    for i in range(len(matriz)):
        lista_x.append(0)
        ultimo_x.append(0) 
      
      #Criar 2 listas com valores iguais a 0
    
    while not verifica_convergencia(matriz_resultado,const_resultado,lista_x,precisao): #O ciclo corre enquanto a solucao nao for precisa o suficiente
        for indice in range(len(lista_x)):
            ultimo_x[indice] = lista_x[indice] #Atribuir a solucao do ciclo passado como variavel para o produto interno do ciclo atual
        for linha in range(len(const_resultado)):
            lista_x[linha] = (ultimo_x[linha] + (const_resultado[linha] - produto_interno(matriz_resultado[linha],ultimo_x)) / matriz_resultado[linha][linha])
         #Atribuir um novo valor ao elemento da solucao, segundo a formula do metodo de Jacobi
    lista_x = tuple(lista_x)  #Transformar a lista das solucoes em tuplo


    return lista_x 



