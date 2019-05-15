import random

def torneioBinario(pop):
    a=random.randint(0, (len(pop)-1))
    b=random.randint(0, (len(pop)-1))
    if(pop[a].fit<pop[b].fit):
        return pop[b]
    else:
        return pop[a]