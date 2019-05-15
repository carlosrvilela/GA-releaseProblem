from indiv import indiv
import random


'''
requisito: custo, risco, importacia
r1, r2...
individuo vetor cada index uma relese
restricao orcamento da release
qtdReg=tamnho do cramossomo
indice i da lista de solucao = req i da lista de req
'''
pesoCliente=[3, 4, 2]
C0=[10, 10, 5]
C1=[8, 10, 6]
C2=[6, 4, 8]
C3=[5, 9, 1]
C4=[7, 7, 5]
C5=[8, 6, 2]
C6=[6, 6, 4]
C7=[9, 8, 3]
C8=[6, 7, 5]
C9=[10,10, 7]
C=[C0, C1, C2, C3, C4, C5, C6, C7, C8, C9]
relevancia=[]
a=0
for k in range (len(C)):
    for i in range(len(pesoCliente)):
        a=a+pesoCliente[i]*C[k][i]
    relevancia.append(a)
    a=0
#ri[custo, risco, importancia]
r0=[60, 3]
r1=[40, 6]
r2=[40, 2]
r3=[30, 6]
r4=[20, 4]
r5=[20, 8]
r6=[15, 9]
r7=[70, 7]
r8=[50, 6]
r9=[20, 6]
req = [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9]
for i in range(len(req)):
    req[i].append(relevancia[i])

qtdRel=3 #qauntidade de releases
rest=125 #resricao de valor para as releases

tamPop=200#tamanho da populacao
nDeGer=250#quantidade de geracoes
pMuta=5#taxa de mutacao de um gene 0 a 100
pCruzamento=90#taxa de cruzamento 0 a 100


def cruza(paiA,paiB):
    quebra=random.randint(1,(paiA.tamCrom-1))
    #print("Q",quebra)
    vetA=[]
    vetB=[]
    for i in range(paiA.tamCrom):
        if (i < quebra):
            vetA.append(paiA.crom[i])
        else:
            vetA.append(paiB.crom[i])
            vetB.append(paiA.crom[i])

    for i in range(quebra):
        vetB.append(paiB.crom[i])

    #print('A',vetA)
    #print('B',vetB)

    filhoA=indiv(rest, req, qtdRel, 1)
    filhoA.setCrom(vetA)
    repara(filhoA)
    filhoA.fit = indiv.score(filhoA.tamCrom, filhoA.crom, filhoA.req, filhoA.qtdRel)
    filhoA.setcustosRel(calCustos(filhoA))

    filhoB=indiv(rest, req, qtdRel, 1)
    filhoB.setCrom(vetB)
    repara(filhoB)
    filhoB.fit = indiv.score(filhoB.tamCrom, filhoB.crom, filhoB.req, filhoB.qtdRel)
    filhoB.setcustosRel(calCustos(filhoB))

    return ([filhoA, filhoB])

def calCustos(ind):
    custosR=[0]*(ind.qtdRel+1)
    for i in range (ind.tamCrom):
        custosR[ind.crom[i]]=custosR[ind.crom[i]]+ind.req[i][0]
    return (custosR)

def repara(ind):
    custosR=[0]*(ind.qtdRel+1)
    vetA = []
    for i in range (ind.tamCrom):
        if(ind.crom[i]!=0):
            #print(custosR[ind.crom[i]],"+",ind.req[i][0],"<=",ind.rest)
            if(custosR[ind.crom[i]]+ind.req[i][0]<=ind.rest):
                #print('banana')
                vetA.append(ind.crom[i])
            else:
                '''
                #print('fakeBanana0')
                a = random.randint(0, ind.qtdRel)
                while ((custosR[ind.crom[a]]+ind.req[i][0] > ind.rest) & a!=0):
                    #print(custosR[ind.crom[a]], "+", ind.req[i][0], ">", ind.rest)
                    a = random.randint(0, ind.qtdRel)
                    #print(a)
                '''
                vetA.append(0)
        else:
            #print('banana0')
            vetA.append(ind.crom[i])
        custosR[ind.crom[i]]=custosR[ind.crom[i]]+ind.req[i][0]

    #print('ind', vetA)
    ind.setCrom(vetA)