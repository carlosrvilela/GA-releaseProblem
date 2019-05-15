import random
import copy
#req[custo, risco, importancia]
class indiv:
    def __init__(self, rest, req, qtdRel, op):#op para indicar individou oriundo de cruzamneto
        self.rest = rest
        self.req = req
        self.qtdRel = qtdRel
        self.tamCrom = len(req)
        if(op==0):
            self.aux = indiv.criaCrom(self.tamCrom, self.qtdRel, self.rest, self.req)
            self.crom = self.aux[0]
            self.custosRel = self.aux[1]
        else:
            self.crom=[0]*self.tamCrom
            self.custosRel=[0]*(self.qtdRel+1)

        self.fit = indiv.score(self.tamCrom, self.crom, self.req, self.qtdRel)

    def setCrom(self, crom):
        self.crom=crom

    def setcustosRel(self, c):
        self.custosRel=c

    def criaCrom(tam, qtdR, rest, req):
        ind = [0]*tam
        somaC=[0]*(qtdR+1)
        for i in range(tam):
            a = random.randint(0, qtdR)
            if(a!=0):
                while((somaC[a]+req[i][0])>rest):
                    a = random.randint(0, qtdR)
                ind[i] = a
                somaC[a] = somaC[a] + req[i][0]
            else:
                ind[i]=a
                somaC[a]=somaC[a]+req[i][0]

        return (ind, somaC)

    def score(tam,crom,req, qtdRel):
        score=0
        for i in range(tam):
            if (crom[i] == 0):
                y = 0
            else:
                y = 1
            #score= score+((req[i][2]*(crom[i]-i+1)-(req[i][1])*i)*y)
            score = score + ((req[i][2] * (qtdRel-crom[i]+1) - (req[i][1]) * crom[i]) * y)
        return score

    def muta(self, p):
        custos = copy.deepcopy(self.custosRel)
        for i in range(self.tamCrom):
            a = random.randint(1, 100)
            if(a<=p):
                b = random.randint(0, self.qtdRel)
                if(b!=0):
                    if((custos[b] + self.req[i][0])<=self.rest):
                        custos[self.crom[i]] = custos[self.crom[i]] - self.req[i][0]
                        self.crom[i] = b
                        custos[self.crom[i]] = custos[self.crom[i]] + self.req[i][0]
                else:
                    custos[self.crom[i]] = custos[self.crom[i]] - self.req[i][0]
                    self.crom[i] = b
                    custos[self.crom[i]] = custos[self.crom[i]] + self.req[i][0]

        self.custosRel=custos
        self.fit = indiv.score(self.tamCrom, self.crom, self.req, self.qtdRel)

