from indiv import indiv
from torneioBinario import torneioBinario
from op import cruza
from op import req, qtdRel, rest, pMuta, pCruzamento, tamPop, nDeGer
import operator
import random

pop=[]
des=[]
proxPop=[]

for i in range(tamPop):
    pop.append(indiv(rest, req, qtdRel, 0))

for n in range (nDeGer):
    for i in range((tamPop//2)):
        paiA=torneioBinario(pop)
        paiB=torneioBinario(pop)
        sort=random.randint(1,100)
        if(sort<=pCruzamento):
            filhos=cruza(paiA,paiB)
            filhos[0].muta(pMuta)
            filhos[1].muta(pMuta)
            des.append(filhos[0])
            des.append(filhos[1])
        else:
            paiA.muta(pMuta)
            paiA.muta(pMuta)
            des.append(paiA)
            des.append(paiB)

    pop.sort(key=operator.attrgetter('fit'), reverse=1)
    des.sort(key=operator.attrgetter('fit'), reverse=1)

    for i in range(tamPop):
        if(i<=(tamPop//2)):
            proxPop.append(pop[i])
        else:
            proxPop.append(des[i-(tamPop//2)])
    proxPop.sort(key=operator.attrgetter('fit'), reverse=1)

    print('\n\n\t\t\t\t\t\t\t\tGeracao'+str(n),'\n')
    print('G atual:\t\t\t\t\t\t\t\t Descendentes:\t\t\t\t\t\t\t Proxima G:')
    for i in range(tamPop):
        print('S'+str(i),pop[i].crom,'\t\t','S'+str(i),des[i].crom,'\t\t','S'+str(i),proxPop[i].crom,
              '\nFitness:',pop[i].fit,'\t\t\t\t\t\t\t','Fitness:',des[i].fit,'\t\t\t\t\t\t\t','Fitness:',proxPop[i].fit,
              '\nCusto:',pop[i].custosRel,'\t\t\t\t','Custo:',des[i].custosRel,'\t\t\t\t','Custo:',proxPop[i].custosRel)
    pop=proxPop
    des=[]
    proxPop=[]

