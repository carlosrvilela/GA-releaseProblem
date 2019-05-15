from indiv import indiv
from torneioBinario import torneioBinario
from op import cruza
from op import req, qtdRel, rest, pMuta, pCruzamento, tamPop, nDeGer
import operator
import random

'''
s1=indiv(rest, req, qtdRel, 0)
print('S1',s1.crom)
print('custo das releases S1',s1.custosRel)
print ('apitidao S1',s1.fit)

s2=indiv(rest, req, qtdRel, 0)
print('S2', s2.crom)
print('custo das releases S2',s2.custosRel)
print ('apitidao S2',s2.fit)

#s1.muta(pMuta)
#print('indiduo',s1.crom)
#print ('apitidao',s1.fit)
#print('custo das releases',s1.custosRel)


f=cruza(s1, s2)
s3=f[0]
s4=f[1]
print("S3", s3.crom)
print('custo das releases S3',s3.custosRel)
print ('apitidao S3',s3.fit)
print("S4", s4.crom)
print('custo das releases S4',s4.custosRel)
print ('apitidao S4',s4.fit)

pop=[]
for i in range(tamPop):
    pop.append(indiv(rest, req, qtdRel, 0))

pop.sort(key=operator.attrgetter('fit'), reverse=1)

for i in range(len(pop)):
    print('\nS'+str(i),pop[i].crom,'\nFitness:',pop[i].fit,'\nCusto:',pop[i].custosRel)

a=torneioBinario(pop)
print("mio", a.fit)
'''

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

