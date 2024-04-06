
#João Lucas Morais Cardoso Tavares Rodrigues
#ist1106221
#01/11/2022
#joao.lucas.m.c.t.r@tecnico.ulisboa.pt	

##############TAD GERADOR##################

######CONSTRUTORES#######

def cria_gerador(b,s):
    
    '''int x int → gerador'''
    '''cria_gerador: recebe um inteiro b correspondente aos (bits) 
    e um inteiro s correspondente a (seed) e devolve um gerador.
    Verifica se os argumentos são válidos, caso contrário devolve um ValueError.'''
    
    if not (isinstance(b,int) and (b == 32 or b==64)):
        raise ValueError('cria_gerador: argumentos invalidos')
    if not (isinstance(s,int) and 0<s<=2**b):
        raise ValueError('cria_gerador: argumentos invalidos')
    gerador=[b,s]                                               #GERADOR = [BITS,SEED]
    return gerador

def cria_copia_gerador(g):
    
    '''gerador → gerador'''
    '''cria_copia_gerador: recebe um gerador e devolve uma cópia do mesmo.'''
    copia=[i for i in g]
    return copia
######SELETORES########

def obtem_estado(g):
    
    '''obtem estado: gerador → int'''
    '''obtem_estado: recebe um gerador e devolve o seu estado sem o alterar.'''
    return g[1]

######MODIFICADORES#######

def define_estado(g,s):

    '''define_estado: gerador x int → int'''
    '''define_estado: recebe um gerador e um inteiro e 
        devolve o novo estado do gerador depois de o atualizar.'''
    if eh_gerador(g) and isinstance(s,int):
        g[1]=s
        return s

def atualiza_estado(g):

    '''atualiza_estado: gerador → int'''
    '''atualiza_estado: recebe um gerador e devolve o seu novo estado de acordo
        com o gerador xorshift.'''
        
    if eh_gerador(g):
        if g[0]==64:
            g[1] ^= ( g[1] << 13 ) & 0xFFFFFFFFFFFFFFFF
            g[1] ^= ( g[1] >> 7 ) & 0xFFFFFFFFFFFFFFFF
            g[1]^= ( g[1] << 17 ) & 0xFFFFFFFFFFFFFFFF
        elif g[0]==32:
            g[1] ^= ( g[1] << 13 ) & 0xFFFFFFFF
            g[1] ^= ( g[1] >> 17 ) & 0xFFFFFFFF
            g[1] ^= ( g[1] << 5 ) & 0xFFFFFFFF

        return g[1]

#######RECONHECEDOR#######

def eh_gerador(arg):

    '''eh_gerador: universal → booleano'''
    '''eh_gerador: recebe um argumento e devolve True
         caso o argumento seja um gerador e False caso contrário.'''

    return (isinstance(arg,list) and len(arg) == 2 
            and (isinstance(arg[0],int) and (arg[0] == 32 or arg[0]==64))
            and (isinstance(arg[1],int) and 0<arg[1]<=2**arg[0]))

######TESTES######

def geradores_iguais(g1,g2):
    
    '''geradores_iguais: gerador x gerador → booleano'''
    '''geradores_iguais: recebe dois geradores e devolve True 
        caso sejam iguais e False caso contrário.'''
    if eh_gerador(g1) and eh_gerador(g2):
        return g1[0]==g2[0] and g1[1]==g2[1]
    

######TRANSFORMADOR#######

def gerador_para_str(g):

    '''gerador_para_str: gerador → str'''
    '''gerador_para_str: recebe um gerador e devolve uma string que o representa.'''

    return 'xorshift%s(s=%s)'%(g[0],g[1])


#####FUNCOES ALTO NIVEL#####

def gera_numero_aleatorio(g,n):

    '''gera_numero_aleatorio: gerador x int → int'''
    '''gera_numero_aleatorio: recebe um gerador ,um insteiro,
        e atualiza o estado do mesmo e devolve um inteiro'''
    
    if eh_gerador(g) and isinstance(n,int):
        return (atualiza_estado(g)%n)+1

def gera_carater_aleatorio(g,c):

    '''gera_carater_aleatorio: gerador x str → str'''
    '''gera_carater_aleatorio: recebe um gerador e uma string 
        e devolve um carater aleatorio da string'''

    if eh_gerador(g) and 'A'<=c<='Z':
        l=ord(c)-ord('A')+1
        v=atualiza_estado(g)%l
        return chr(ord('A')+v)

##############TAD GERADOR##################


######CONSTRUTORES#######

def cria_coordenada(col,lin):

    '''cria_coordenada: str x int → coordenada'''
    '''cria_coordenada: recebe uma string e um inteiro e devolve uma coordenada
        caso os argumentos sejam válidos, caso contrário devolve um ValueError.'''
   
    if not(isinstance(col,str) and len(col)==1 and 'A'<=col<='Z'):
        raise ValueError('cria_coordenada: argumentos invalidos')
    if not(isinstance(lin,int) and 1<=lin<=99 ):
        raise ValueError('cria_coordenada: argumentos invalidos')
    cordenadas=(col,lin)                                #CORDENADAS = (COLUNA,LINHA)    
    return cordenadas

########SELETORES######

def obtem_coluna(c):

    '''obtem_coluna: coordenada → str'''
    '''obtem_coluna: recebe uma coordenada e devolve a sua coluna.'''
    return c[0]

def obtem_linha(c):

    '''obtem_linha: coordenada → int'''
    '''obtem_linha: recebe uma coordenada e devolve a sua linha.'''
    return c[1]

######RECONHECEDOR######

def eh_coordenada(arg):

    '''eh_coordenada: universal → booleano'''
    '''eh_coordenada: recebe um argumento e devolve True se o argumento for uma coordenada
        e False caso contrário.'''
    
    return (isinstance(arg,tuple) and len(arg) == 2 
            and (isinstance(arg[0],str) and len(arg[0])==1 and  'A'<=arg[0]<='Z' )
            and (isinstance(arg[1],int) and 1<=arg[1]<=99))

########TESTE#######

def coordenadas_iguais(c1,c2):

    '''coordenadas_iguais: coordenada x coordenada → booleano'''
    '''coordenadas_iguais: recebe duas coordenadas e devolve True caso sejam iguais
        e False caso contrário.'''

    if eh_coordenada(c1) and eh_coordenada(c2):
        return c1==c2
    return False

########TRANSFORMADORES######

def coordenada_para_str(c):

    '''coordenada_para_str: coordenada → str'''
    '''coordenada_para_str: recebe uma coordenada e devolve uma string que a representa.'''

    if eh_coordenada(c):
        if 1<=c[1]<=9:
            return '%s0%s'%(c[0],c[1])
        elif 10<=c[1]<=99:
            return '%s%s'%(c[0],c[1])

def str_para_coordenada(s):

    '''str_para_coordenada: str → coordenada'''
    '''str_para_coordenada: recebe uma string e devolve uma coordenada'''
    
    return cria_coordenada(s[0],int(s[1:]))
        
 
#####FUNCOES ALTO NIVEL######
def obtem_coordenadas_vizinhas(c):

    '''obtem_coordenadas_vizinhas: coordenada → tuplo'''
    '''obtem_coordenadas_vizinhas: recebe uma coordenada e devolve um tuplo com as coordenadas vizinhas'''

    if eh_coordenada(c): 
        resultado=()
                            #Verifica se as coordenadas em volta da coordenada
                            #dada são válidas e caso sejam 
                            #adiciona-as ao tuplo resultado.
        
        if 'A'<=chr(ord(obtem_coluna(c))-1)<='Z' and 1<=(obtem_linha(c)-1)<=99:                                    
            resultado+=(cria_coordenada(chr(ord(obtem_coluna(c))-1),obtem_linha(c)-1), )
        if 'A'<=chr(ord(obtem_coluna(c)))<='Z' and 1<=(obtem_linha(c)-1)<=99:
            resultado+=(cria_coordenada(chr(ord(obtem_coluna(c))),obtem_linha(c)-1), )
        if 'A'<=chr(ord(obtem_coluna(c))+1)<='Z' and 1<=(obtem_linha(c)-1)<=99:
            resultado+=(cria_coordenada(chr(ord(obtem_coluna(c))+1),obtem_linha(c)-1), ) 
        if 'A'<=chr(ord(obtem_coluna(c))+1)<='Z' and 1<=(obtem_linha(c))<=99:
            resultado+=(cria_coordenada(chr(ord(obtem_coluna(c))+1),obtem_linha(c)), )  
        if 'A'<=chr(ord(obtem_coluna(c))+1)<='Z' and 1<=(obtem_linha(c)+1)<=99:
            resultado+=(cria_coordenada(chr(ord(obtem_coluna(c))+1),obtem_linha(c)+1), )
        if 'A'<=chr(ord(obtem_coluna(c)))<='Z' and 1<=(obtem_linha(c)+1)<=99:
            resultado+=(cria_coordenada(chr(ord(obtem_coluna(c))),obtem_linha(c)+1), )
        if 'A'<=chr(ord(obtem_coluna(c))-1)<='Z' and 1<=(obtem_linha(c)+1)<=99:
            resultado+=(cria_coordenada(chr(ord(obtem_coluna(c))-1),obtem_linha(c)+1), )
        if 'A'<=chr(ord(obtem_coluna(c))-1)<='Z' and 1<=(obtem_linha(c))<=99:
            resultado+=(cria_coordenada(chr(ord(obtem_coluna(c))-1),obtem_linha(c)), )
        
        return resultado

def obtem_coordenada_aleatoria(c,g):

    '''obtem_coordenada_aleatoria: coordenada x gerador → coordenada'''
    '''obtem_coordenada_aleatoria: recebe uma coordenada e um gerador e devolve uma coordenada aleatória'''

    if eh_coordenada(c) and eh_gerador(g):
        return cria_coordenada(gera_carater_aleatorio(g,obtem_coluna(c)),gera_numero_aleatorio(g,obtem_linha(c)))


##############TAD PARCELA##################

########CONSTRUTOR######

def cria_parcela():

    '''cria_parcela: {} → parcela'''
    '''cria_parcela: devolve uma parcela tapada e sem mina.'''

    parcela=['tapada','s_mina']
    return parcela

def cria_copia_parcela(p):

    '''cria_copia_parcela: parcela → parcela'''
    '''cria_copia_parcela: recebe uma parcela e devolve uma cópia da mesma.'''
    copia=[i for i in p]
    return copia

########MODIFICADORES#######

def limpa_parcela(p):

    '''limpa_parcela: parcela → parcela'''
    '''limpa_parcela: recebe uma parcela e devolve a mesma parcela limpa.'''
    p[0]='limpa'
    return p

def marca_parcela(p):

    '''marca_parcela: parcela → parcela'''
    '''marca_parcela: recebe uma parcela e devolve a mesma parcela marcada.'''
    p[0]='marcada'
    return p

def desmarca_parcela(p):

    '''desmarca_parcela: parcela → parcela'''
    '''desmarca_parcela: recebe uma parcela e desmarca a mesma.'''
    p[0]='tapada'
    return p

def esconde_mina(p):

    '''esconde_mina: parcela → parcela'''
    '''esconde_mina: recebe uma parcela e esconde uma mina na mesma.'''
    p[1]='c_mina'
    return p

########RECONHECEDOR#######

def eh_parcela(arg):

    '''eh_parcela: universal → booleano'''
    '''eh_parcela: recebe um argumento e verifica se é uma parcela.'''
    
    return (type(arg)==list and len(arg)==2 
            and arg[0] in ['tapada','marcada','limpa'] and arg[1] in ['s_mina','c_mina']
            and len(arg)==2 and isinstance(arg,list)
            and isinstance(arg[0],str) and isinstance(arg[1],str) 
            and ('tapada'in arg[0] or 'marcada'in arg[0] or 'limpa' in arg[0])
            and ('c_mina'in arg[1] or 's_mina'in arg[1]))

def eh_parcela_tapada(p):

    '''eh_parcela_tapada: parcela → booleano'''
    '''eh_parcela_tapada: recebe uma parcela e verifica se a mesma está tapada.'''

    return (eh_parcela(p) and len(p)==2 and isinstance(p,list)
            and isinstance(p[0],str) and isinstance(p[1],str) 
            and 'tapada'in p[0] and ('c_mina'in p[1] or 's_mina'in p[1]))

def eh_parcela_marcada(p):

    '''eh_parcela_marcada: parcela → booleano'''
    '''eh_parcela_marcada: recebe uma parcela e verifica se a mesma está marcada.'''

    return (eh_parcela(p) and len(p)==2 and isinstance(p,list)
            and isinstance(p[0],str) and isinstance(p[1],str) 
            and 'marcada'in p[0] and ('c_mina'in p[1] or 's_mina'in p[1]))

def eh_parcela_limpa(p):

    '''eh_parcela_limpa: parcela → booleano'''
    '''eh_parcela_limpa: recebe uma parcela e verifica se a mesma está limpa.'''

    return ( eh_parcela(p) and len(p)==2 and isinstance(p,list)
            and isinstance(p[0],str) and isinstance(p[1],str) 
            and 'limpa' in p[0] and ('c_mina'in p[1] or 's_mina'in p[1]))

def eh_parcela_minada(p):

    '''eh_parcela_minada: parcela → booleano'''
    '''eh_parcela_minada: recebe uma parcela e verifica se a mesma esta minada.'''

    return ( eh_parcela(p) and len(p)==2 and isinstance(p,list)
            and isinstance(p[0],str) and isinstance(p[1],str) 
            and ('tapada'in p[0] or 'marcada'in p[0] or 'limpa' in p[0]) 
            and 'c_mina' in p[1])

########TESTE#######

def parcelas_iguais(p1,p2):

    '''parcelas_iguais: parcela x parcela → booleano'''
    '''parcelas_iguais: recebe duas parcelas e verifica se são iguais.'''

    if eh_parcela(p1) and eh_parcela(p2):
        return p1[0]==p2[0] and p1[1]==p2[1]
    return False

#######TRANSFORMADORES#######

def parcela_para_str(p):

    '''parcela_para_str: parcela → cadeia de caracteres'''
    '''parcela_para_str: recebe uma parcela e devolve uma cadeia de caracteres que representa a mesma.'''
    if p[0]=='tapada':
        return '#'
    if p[0]=='marcada':
        return '@'
    if p[0]=='limpa' and p[1]=='s_mina':
        return '?'
    if p[0]=='limpa' and p[1]=='c_mina':
        return 'X'

######FUNCOES ALTO NIVEL#######

def alterna_bandeira(p):

    '''alterna_bandeira: parcela → parcela'''
    '''alterna_bandeira: recebe uma parcela e alterna a bandeira da mesma.'''

    if eh_parcela(p):
        if eh_parcela_marcada(p):
            desmarca_parcela(p)
            return True
        elif eh_parcela_tapada(p):
            marca_parcela(p)
            return True
        else:
            return False


##################TAD CAMPO#################

#########CONSTRUTOR#######

def cria_campo(c,l):

    '''cria_campo: caracter x inteiro → campo'''
    '''cria_campo: recebe um caracter e um inteiro e cria um campo com o caracter e o inteiro dados
        verificando se os dados introduzidos são válidos.'''

    if not(isinstance(c,str) and isinstance(l,int) and len(c)==1):
        raise ValueError('cria_campo: argumentos invalidos')
    if not('A'<=c<='Z' and 1<=l<=99):
        raise ValueError('cria_campo: argumentos invalidos')
    campo=[]
    for linhas in range(l):              
        linha=[]                                #CRIACAO DAS LINHAS EM FUNCAO DE O NUMERO DAS MESMAS FORNECIDO
        for letra in range(ord('A'),ord(c)+1):
            linha+=[[cria_coordenada(chr(letra),linhas+1),cria_parcela()]]  #CRIACAO DAS COORDENADAS E DAS PARCELAS
        campo+=[linha]                                                      #ADICIONA AS LINHAS AO CAMPO
    return campo

def cria_copia_campo(m):

    '''cria_copia_campo: campo → campo'''
    '''cria_copia_campo: recebe um campo e cria uma cópia do mesmo.'''
    
    copia=[]
    for linhas in m:
        copia_linhas=[]                                             #PERCORRE O CAMPO E CRIA UMA COPIA DE CADA LINHA
        for colunas in linhas:
            copia_linhas+=[[colunas[0],cria_copia_parcela(colunas[1])]] #CRIA UMA COPIA DE CADA PARCELA E COORDENADA
        copia+=[copia_linhas]                               #ADICIONA AO CAMPO CADA COPIA DE LINHA
    return copia

########SELETORES#######

def obtem_ultima_coluna(m):

    '''obtem_ultima_coluna: campo → caracter'''
    '''obtem_ultima_coluna: recebe um campo e devolve o caracter da última coluna do mesmo.'''
    
    return obtem_coluna(m[-1][-1][0])

def obtem_ultima_linha(m):

    '''obtem_ultima_linha: campo → inteiro'''
    '''obtem_ultima_linha: recebe um campo e devolve o inteiro da última linha do mesmo.'''
    
    return obtem_linha(m[-1][-1][0])


def obtem_parcela(m,c):

    '''obtem_parcela: campo x coordenada → parcela'''
    '''obtem_parcela: recebe um campo e uma coordenada e devolve a parcela que se encontra na coordenada dada.'''
   
    for linhas in m:
        for colunas in linhas:          
            if coordenadas_iguais(colunas[0],c):  #PERCORRE O CAMPO E VERIFICA SE A COORDENADA DADA 
                    return colunas[1]             #É IGUAL A CADA COORDENADA DO CAMPO E RETORNA A SUA PARCELA



def obtem_coordenadas(m,s):

    '''obtem_coordenadas: campo x cadeia de caracteres → tuplo de coordenadas'''
    '''obtem_coordenadas: recebe um campo e uma cadeia de caracteres e devolve um tuplo de coordenadas que representa a mesma.'''
    
    resultado=()
    if s=='limpas':
        for linhas in m:                                #PERCOORE O CAMPO E DEVOLVE AS COORDENADAS DAS PARCELAS LIMPAS
            for colunas in linhas:
                if eh_parcela_limpa(colunas[1]):
                    resultado+=(colunas[0],)
    if s=='tapadas':
        for linhas in m:                                #PERCOORE O CAMPO E DEVOLVE AS COORDENADAS DAS PARCELAS TAPADAS
            for colunas in linhas:
                if eh_parcela_tapada(colunas[1]):
                    resultado+=(colunas[0],)                
    if s=='marcadas':
        for linhas in m:                                #PERCOORE O CAMPO E DEVOLVE AS COORDENADAS DAS PARCELAS MARCADAS
            for colunas in linhas:
                if eh_parcela_marcada(colunas[1]):
                    resultado+=(colunas[0],)
    if s=='minadas':
        for linhas in m:                                #PERCOORE O CAMPO E DEVOLVE AS COORDENADAS DAS PARCELAS MINADAS  
            for colunas in linhas:
                if eh_parcela_minada(colunas[1]):
                    resultado+=(colunas[0],)
    return resultado


def obtem_numero_minas_vizinhas(m,c):

    '''obtem_numero_minas_vizinhas: campo x coordenada → inteiro'''
    '''obtem_numero_minas_vizinhas: recebe um campo e uma coordenada e devolve 
        o número de minas que se encontram nas coordenadas vizinhas da coordenada dada.'''
    resultado=0
    tuplo=obtem_coordenadas_vizinhas(c)  #TUPLO DE COORDENADAS VIZINHAS                     
    for coordenada in tuplo:
        if eh_coordenada_do_campo(m,c) and eh_parcela_minada(obtem_parcela(m,coordenada)):
            resultado+=1    #CONTADOR DE MINAS VIZINHAS
    return resultado


########RECONHECEDORES#######

def eh_campo(arg):

    '''eh_campo: universal → booleano'''
    '''eh_campo: recebe um argumento e verifica se o mesmo é um campo.'''

    erros=0
    if isinstance(arg,list) and len(arg)!=0:
        if  len(arg)==obtem_ultima_linha(arg) and len(arg[0])==(ord(obtem_ultima_coluna(arg))-64):
            for linhas in arg:
                if isinstance(linhas,list):
                    for colunas in linhas:
                        if not(isinstance(colunas,list) and len(colunas)==2 and eh_coordenada(colunas[0]) \
                            and eh_parcela(colunas[1])):
                            erros+=1
                else:  
                    erros+=1
        else:
            erros+=1        #FUNCAO QUE PERCORRE TODOS OS ERROS POSSIVEIS NO CAMPO E ADICIONA-OS A UMA VARIAVEL
    else:
        erros+=1

    return erros==0


def eh_coordenada_do_campo(m,c):

    '''eh_coordenada_do_campo: campo x coordenada → booleano'''
    '''eh_coordenada_do_campo: recebe um campo e uma coordenada e verifica se a coordenada dada pertence ao campo.'''
    validade=0
    for linhas in m: 
        for colunas in linhas:
            if coordenadas_iguais(colunas[0],c):        #PERCORRE AS LINHAS E AS COLUNAS DO CAMPO 
                validade+=1                             #E VERIFICA SE A COORDENADA DADA É IGUAL A ALGUMA COORDENADA DO CAMPO
    return validade==1

#######TESTE########

def campos_iguais(m1,m2):

    '''campos_iguais: campo x campo → booleano'''
    '''campos_iguais: recebe dois campos e verifica se os mesmos são iguais.'''
    if eh_campo(m1) and eh_campo(m2):
        if not isinstance(m1,list) and not isinstance(m2,list):  #VERIFICA SE OS DOIS ARGUMENTOS SÃO LISTAS
            return False                            
        if len(m1)!=len(m2) :
            return False
        for linhas in range(len(m1)):                   #VERIFICA SE AS DUAS LISTAS TEM O MESMO TAMANHO
            if len(m1[linhas])!=len(m2[linhas]):
                return False
            for colunas in range(len(m1[linhas])):                              #VERIFICA SE TODAS AS COORDENADAS E AS PARCELAS SÃO IGUAIS
                if not coordenadas_iguais(m1[linhas][colunas][0],m2[linhas][colunas][0])\
                    or not parcelas_iguais(m1[linhas][colunas][1],m2[linhas][colunas][1]):  
                    return False
        return True
                
########TRANSFORMADOR#########

def campo_para_str(m):

    '''campo_para_str: campo → cadeia de caracteres'''
    '''campo_para_str: recebe um campo e devolve uma cadeia de caracteres que representa o mesmo.'''

    resutado=''
    tracos=''      #VARIAVIES AUXILIARES
    letras=' '*3
    campo=''
    
    for ord_letra in range(ord('A'),ord(obtem_ultima_coluna(m))+1) :
        letras+=chr(ord_letra)
        tracos+='-'                         #CRIAÇÃO DA PRIMEIRA LINHA

    barreira_sup_inf=' '*2+'+'+tracos+'+'       #CRIAÇÃO DA BARRA SUPERIOR E INFERIOR
    
    for linha in range(len(m)):
        
        line_meio=''                                #CRIAÇÃO DAS LINHAS DO MEIO
        
        for colunas in range(len(m[linha])):                     
            if not eh_parcela_limpa(m[linha][colunas][1]):   #SE A PARCELA NÃO FOR LIMPA
                line_meio+=parcela_para_str(obtem_parcela(m,m[linha][colunas][0]))
            
            else:           #SE A PARCELA FOR LIMPA
                
                if eh_parcela_limpa(m[linha][colunas][1]) and eh_parcela_minada(m[linha][colunas][1]):  #SE A PARCELA FOR LIMPA E MINADA
                    line_meio+=parcela_para_str(obtem_parcela(m,m[linha][colunas][0]))
                
                elif obtem_numero_minas_vizinhas(m,m[linha][colunas][0])==0:    #SE A PARCELA FOR LIMPA E NÃO TIVER MINAS VIZINHAS
                    line_meio+=' '
                
                else:
                    line_meio+=str(obtem_numero_minas_vizinhas(m,m[linha][colunas][0])) #SE A PARCELA FOR LIMPA E TIVER MINAS VIZINHAS
                
        if linha<9:
            line='0'+str(linha+1)+'|'+line_meio+'|'+'\n'   
                                                            #CRIAÇÃO DAS LINHAS DO MEIO COM O NÚMERO DA LINHA
        else:
            line=str(linha+1)+'|'+line_meio+'|'+'\n'
        campo+=line

    resutado=letras+'\n'+barreira_sup_inf+'\n'+campo+barreira_sup_inf   #CRIAÇÃO DO CAMPO COMPLETO
    
    return resutado

###########FUNCOE AUXILIARE###########

def verifica_coordenada(m):

    '''verifica_coordenada: campo → coordenada'''
    '''verifica_coordenada: recebe um campo e devolve uma coordenada válida.'''
    
    coordenada=str(input('Escolha uma coordenada:'))
    
    while not len(coordenada)==3:                           #VERIFICAR SE A COORDENADA TEM 3 CARACTERES
        coordenada=str(input('Escolha uma coordenada:'))
    
    while  not coordenada[0]==coordenada[0].upper() and not(eh_coordenada(str_para_coordenada(coordenada))) \
        and not(eh_coordenada_do_campo(m,str_para_coordenada(coordenada))): #VERIFICAR SE A COORDENADA É VÁLIDA
        coordenada=str(input('Escolha uma coordenada:'))
    
    return str_para_coordenada(coordenada)

######FUNCOES ALTO NIVEL#######

def coloca_minas(m,c,g,n):

    '''coloca_minas: campo x coordenada x gerador_de_aleatorios x inteiro → campo'''
    '''coloca_minas: recebe um campo, uma coordenada, um gerador de aleatórios e um inteiro e coloca n minas no campo.'''
    if eh_coordenada_do_campo(m,c) :
            while n>0:
                
                c_aleatoria=obtem_coordenada_aleatoria(cria_coordenada(obtem_ultima_coluna(m),obtem_ultima_linha(m)),g)
                
                if not eh_parcela_minada(obtem_parcela(m,c_aleatoria)) and c_aleatoria not in obtem_coordenadas_vizinhas(c)\
                    and not coordenadas_iguais(c_aleatoria,c):
                    esconde_mina(obtem_parcela(m,c_aleatoria))  #SE A COORDENADA ALEATORIA NAO FOR MINADA E NAO FOR VIZINHA DA COORDENADA DADA 
                                                                #E NAO FOR IGUAL A COORDENADA DADA, ENTÃO A COORDENADA ALEATORIA VIRA MINADA
                    n-=1
            return m
    
def limpa_campo(m,c):

    '''limpa_campo: campo x coordenada → campo'''
    '''limpa_campo: modifica destrutivamente o campo limpando a parcela na coordenada c e o devolvendo-a.
         Se nao houver nenhuma mina vizinha escondida, limpa
        iterativamente todas as parcelas vizinhas tapadas. Caso a parcela se encontre ja
        limpa, a operacaoo nao tem efeito.'''

    if eh_campo(m) and eh_coordenada_do_campo(m,c):
       
        if eh_parcela_minada(obtem_parcela(m,c)):           #SE A COORDENADA FOR MINADA
            limpa_parcela(obtem_parcela(m,c))       
            return m
       
        elif not eh_parcela_minada(obtem_parcela(m,c)) and obtem_numero_minas_vizinhas(m,c)==0: 
            limpa_parcela(obtem_parcela(m,c))                       
            for coordenada in obtem_coordenadas_vizinhas(c):              ##SE A COORDENADA NAO FOR MINADA E NAO TIVER MINAS VIZINHAS
                if not eh_parcela_minada(obtem_parcela(m,coordenada)) \
                    and eh_parcela_tapada(obtem_parcela(m,coordenada))\
                    and eh_coordenada_do_campo(m,coordenada):
                        limpa_parcela(obtem_parcela(m,coordenada)) and limpa_campo(m,coordenada) #LIMPA A COORDENADA E CHAMA A FUNCAO NOVAMENTE
      
        elif not eh_parcela_minada(obtem_parcela(m,c)) and obtem_numero_minas_vizinhas(m,c)!=0:
            limpa_parcela(obtem_parcela(m,c))   #SE A COORDENADA NAO FOR MINADA E TIVER MINAS VIZINHAS
    return m

def jogo_ganho(m):

    '''jogo_ganho: campo → booleano'''
    '''jogo_ganho: recebe um campo e devolve True se o jogo foi ganho e False caso contrario.'''
  
    lista=[]        #OBTEM UMA LISTA COM TODAS AS COORDENADAS DO CAMPO
    coordenadas_lista=list(obtem_coordenadas(m,'tapadas'))+list(obtem_coordenadas(m,'marcadas'))\
                    +list(obtem_coordenadas(m,'limpas'))
    coordenadas_lista_minadas=list(obtem_coordenadas(m,'minadas')) #OBTEM UMA LISTA COM TODAS AS COORDENADAS MINADAS
    for coordenada in coordenadas_lista:
        if coordenada not in coordenadas_lista_minadas:     
            lista.append(coordenada)                            #OBTEM UMA LISTA COM TODAS AS COORDENADAS NAO MINADAS
    resultado=0
    for coordenada in lista:
        if not eh_parcela_limpa(obtem_parcela(m,coordenada)):    #VERIFICA SE TODAS AS COORDENADAS NAO MINADAS ESTAO LIMPAS
            resultado+=1
    return resultado==0

def turno_jogador(m):

    '''turno_jogador: campo → campo'''
    '''turno_jogador: recebe um campo e devolve o campo com a jogada do jogador.'''
 
    decisao=str(input('Escolha uma ação, [L]impar ou [M]arcar:'))
    while decisao!='L' and decisao!='M':                                #VERIFICA SE A DECISAO E VALIDA
        decisao=str(input('Escolha uma ação, [L]impar ou [M]arcar:'))
    else:
        
        coordenada=verifica_coordenada(m)               #VERIFICA SE A COORDENADA E VALIDA
        
        if decisao=='L':                        #SE A DECISAO FOR LIMPAR
            if eh_parcela_minada(obtem_parcela(m,coordenada)):      #VERIFICA SE A COORDENADA E MINADA
                    return False
            else:
                limpa_campo(m,coordenada)       #SE NAO FOR MINADA LIMPA O CAMPO
                return True 
        elif decisao=='M':                                      #SE A DECISAO FOR MARCAR    
            alterna_bandeira(obtem_parcela(m,coordenada))
    return True

def minas(c,l,n,d,s):

    '''minas: caracter x inteiro x inteiro x inteiro x inteiro → booleano'''
    '''minas: A funcao recebe uma cadeia de carateres e 4 valores inteiros correspondentes, respetivamente, a:
        ultima coluna c; ultima linha l; numero de parcelas com minas n; dimensao do gerador
        de numeros d; e estado inicial ou seed s para a geracao de numeros aleatorios. A funcao
        devolve True se o jogador conseguir ganhar o jogo, ou False caso contrario
        Fazendo tambem verificações de erros.'''
    
    if not(isinstance(c,str) and len(c)==1 and isinstance(l,int)):
        raise ValueError('minas: argumentos invalidos')
    if not('A'<=c<='Z' and 1<=l<=99):
        raise ValueError('minas: argumentos invalidos')
    if not(isinstance(n,int)):
        raise ValueError('minas: argumentos invalidos')
    if not (isinstance(d,int) and (d == 32 or d==64)):   #LEVANTAMENTO DE ERROS
        raise ValueError('minas: argumentos invalidos') 
    if not (isinstance(s,int) and 0<s<=2**d):
        raise ValueError('minas: argumentos invalidos')
    if not(n<(l*(ord(c)-ord('A')+1)-9) and n>0):
        raise ValueError('minas: argumentos invalidos')
    
    m=cria_campo(c,l)         
    g=cria_gerador(d,s)                                 #CRIAÇÃO DO CAMPO E DO GERADOR
    
    numero_bandeiras=obtem_coordenadas(m,'marcadas')
    print('   [Bandeiras %s/%s]' %(len(numero_bandeiras),n))    #IMPRIME A PRIMEIRA INTERFACE DO JOGO
    print(campo_para_str(m))
    
    coordenada_inicial=verifica_coordenada(m)                   #PEDIR COORDENADA INICIAL

    coloca_minas(m,coordenada_inicial,g,n)
    limpa_campo(m,coordenada_inicial)
    print('   [Bandeiras %s/%s]' %(len(numero_bandeiras),n))        #IMPRIME A SEGUNDA INTERFACE DO JOGO COM AS MINAS COLOCADAS
    print(campo_para_str(m))                                        # E O CAMPO LIMPO EM RELACAO A COORDENADA INICIAL

    while not jogo_ganho(m):             #ESTRUTURA DE VITORIA E DERROTA DO JOGO
        
        if turno_jogador(m)==False:                                 #CASO O JOGADOR PERCA
            numero_bandeiras=obtem_coordenadas(m,'marcadas')
            print('   [Bandeiras %s/%s]' %(len(numero_bandeiras),n))        
            print(campo_para_str(m))
            print('BOOOOOOOM!!!')
            return False
        
        numero_bandeiras=obtem_coordenadas(m,'marcadas')
        print('   [Bandeiras %s/%s]' %(len(numero_bandeiras),n))        #IMPRIME A INTERFACE DO JOGO A CADA TURNO
        print(campo_para_str(m))                                        # CASO NAO TENHA PERDIDO NEM GANHO
        
    if jogo_ganho(m):
        print('VITORIA!!!')         #VITORIA DO JOGO
        return True
