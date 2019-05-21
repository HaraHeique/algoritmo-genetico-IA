# -*- coding: utf-8 -*-

"""
    Classe que representa a população que contém um conjunto de espécies.
"""

from random import uniform, randint, randrange
from Especie import Especie

class Populacao:
    '''Classe que representa a população que contém um conjunto de espécies.'''
    def __init__(self, lstEspecies: list = None, taxaCrossover: float = None, taxaMutacao: float = None):
        self._especies: list = lstEspecies if lstEspecies != None else []
        self._taxaCrossover: float = taxaCrossover if taxaCrossover != None else 0.6
        self._taxaMutacao: float = taxaMutacao if taxaMutacao != None else 0.01

    def addEspecie(self, especie: Especie) -> None:
        '''Adiciona um indivíduo da espécie a população.'''
        self._especies.append(especie)

    def addRangeEspecies(self, especies: list) -> None:
        '''Adiciona uma lista de indivíduos da espécie a população.'''
        self._especies.append(especies)

    # Cria indivíduos de uma dada espécie da população passando como argumento o número de indivíduos
    def criaIndividuos(self, nIndividuos: int, qtdBits: int) -> None:
        '''Cria indivíduos de uma dada espécie da população passando como argumento o 
           número de indivíduos.'''
        while (nIndividuos > 0):
            novaEspecie = Especie(qtdBits)
            self.addEspecie(novaEspecie)
            nIndividuos -= 1

    # Verifica se há mutação, com 1% de chance de acontecer
    def __hasMutacao(self) -> bool:
        randPercent: float = uniform(0, 1)

        if (randPercent <= self._taxaMutacao):
            return True
        return False

    # Verifica se cada bit tem alguma mutação, caso haja, altera o bit
    def aplicaMutacao(self, especie: Especie) -> bool:
        '''Aplica mutação no bit correspondente caso esteja na taxa definida na população e retorna 
           True caso teve alguma mutação.'''
        individuoMutado: str = ""
        teveMutacao: bool = False

        for i in range(len(especie._binario)):

            # Caso caia na probabilidade da mutação troca o seu bit
            if (self.__hasMutacao()):
                teveMutacao = True
                if (especie._binario[i] == '1'):
                    individuoMutado += '0'
                elif (especie._binario[i] == '0'):
                    individuoMutado += '1'
                else:
                    raise Exception("O indivíduo não possui uma cadeia binária correta.")
            else:
                individuoMutado += especie._binario[i]
            
        # Altera o bit que sofreu mutação e atualiza os bits
        especie.individuo = individuoMutado

        return teveMutacao

    # Verifica se acontece o crossover entre os pais
    def __hasCrossOver(self) -> bool:
        randPercent: float = uniform(0, 1)

        if (randPercent <= self._taxaCrossover):
            return True

        return False

    # Caso aconteça o crossover, essa função vai alterar os genes
    def __doCrossover(self, individuo1: Especie, individuo2: Especie) -> None:
        if (len(individuo1) != len(individuo2)):
            raise Exception("Espécies com número de bits diferentes!")
        
        # Ponto de corte escolhido de forma aleatório
        numBitsCorte: int = randint(0, len(individuo1))
        numBitsRepetidos: int = len(individuo1) - numBitsCorte
        
        # Cria os novos indivíduos e realiza o crossover de fato
        newIndiduo1: str = individuo1.individuo[0:numBitsRepetidos] + individuo2.individuo[-numBitsCorte:]
        newIndiduo2: str = individuo2.individuo[0:numBitsRepetidos] + individuo1.individuo[-numBitsCorte:]

        # Seta os novos indivíduos com o crossover realizado
        individuo1.individuo = newIndiduo1
        individuo2.individuo = newIndiduo2

    #Função para usar a crossOver e alterar os genes caso os dois pais selecionados estão aptos.
    def aplicaCrossover(self, porcentagemCromossosmos: int) -> bool:
        '''Aplica o crossover entre dois pais com seleção por torneio = 2 e caso aplique o crossover
           dentro da taxa definida retorna True.'''
        teveCrossover: bool = False

        # Caso a taxa de crossover esteja dentro do determinado realiza o crossover
        if (self.__hasCrossOver()):
            teveCrossover = True
            
            # Pega o indivíduo aleatoriamente com taxa de rodeio de 2
            individuo1: Especie = self._especies[randrange(0, len(self._especies))]
            individuo2: Especie = self._especies[randrange(0, len(self._especies))]

            # Faz o crossover nos indivíduos recuperados na lista de especies da população
            self.__doCrossover(individuo1, individuo2)

        return teveCrossover


# Testes unitário do módulo
if __name__ == "__main__":
    populacao: Populacao = Populacao()
    print(populacao)