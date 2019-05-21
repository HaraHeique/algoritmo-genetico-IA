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
            novaEspecie: Especie = Especie(qtdBits)
            self.addEspecie(novaEspecie)
            nIndividuos -= 1

    # Faz a seleção de maneira aleatória dos indivíduos que serão realizados o crossover baseado nos pais correntes
    def __torneioSelection(self) -> list:
        indivuosSelected: list = []
        qntSelection: int = len(self._especies)
        
        while (qntSelection > 0):
            # Pega o indivíduo aleatoriamente com taxa de rodeio de 2
            individuo1: Especie = self._especies[randrange(0, len(self._especies))]
            individuo2: Especie = self._especies[randrange(0, len(self._especies))]

            indMelhorAptidao: float = individuo1 if (individuo1.aptidao < individuo2.aptidao) else individuo2
            indivuosSelected.append(indMelhorAptidao)
            qntSelection -= 1
        
        return indivuosSelected

    # Verifica se há mutação, com 1% de chance de acontecer
    def __hasMutacao(self) -> bool:
        randPercent: float = uniform(0, 1)

        if (randPercent <= self._taxaMutacao):
            return True
        return False

    # Verifica se cada bit tem alguma mutação, caso haja, altera o bit
    def aplicaMutacao(self) -> bool:
        '''Aplica mutação no bit correspondente para cada indivíduo da espécie caso esteja na taxa 
           definida na população e retorna True caso teve alguma mutação.'''
    
        teveMutacao: bool = False
        # Checa a mutação para cada indivíduo da espécie
        for especie in self._especies:
            individuoMutado: str = ""

            for i in range(len(especie.individuo)):

                # Caso caia na probabilidade da mutação troca o seu bit
                if (self.__hasMutacao()):
                    teveMutacao = True
                    if (especie.individuo[i] == '1'):
                        individuoMutado += '0'
                    elif (especie.individuo[i] == '0'):
                        individuoMutado += '1'
                    else:
                        raise Exception("O indivíduo não possui uma cadeia binária correta.")
                else:
                    individuoMutado += especie.individuo[i]
                
            # Altera o bit que sofreu mutação e atualiza os bits, caso tenha mutação pois aí é recalculado a aptidão
            if (teveMutacao):
                especie.individuo = individuoMutado

        return teveMutacao

    # Verifica se acontece o crossover entre os pais
    def __hasCrossover(self) -> bool:
        randPercent: float = uniform(0, 1)

        if (randPercent <= self._taxaCrossover):
            return True

        return False

    # Caso aconteça o crossover, essa função vai alterar os genes
    def __doCrossover(self, individuo1: Especie, individuo2: Especie) -> list:
        if (len(individuo1.individuo) != len(individuo2.individuo)):
            raise Exception("Espécies pais com número de bits diferentes!")
        
        # Ponto de corte escolhido de forma aleatório
        numBitsCorte: int = randint(0, len(individuo1.individuo))
        numBitsRepetidos: int = len(individuo1.individuo) - numBitsCorte
        
        # Cria os novos indivíduos e realiza o crossover de fato
        bitsIndiduo1: str = individuo1.individuo[0:numBitsRepetidos] + individuo2.individuo[-numBitsCorte:]
        bitsIndiduo2: str = individuo2.individuo[0:numBitsRepetidos] + individuo1.individuo[-numBitsCorte:]

        # Seta os valores de bits correspondente ao novo indivíduo, o que também calcula o valor de aptidão novamente
        individuo1.individuo = bitsIndiduo1
        individuo2.individuo = bitsIndiduo2

        return [individuo1, individuo2]

    #Função para usar a crossOver e alterar os genes caso os dois pais selecionados estão aptos.
    def aplicaCrossover(self) -> bool:
        '''Aplica o crossover entre dois pais com seleção por torneio = 2 e caso aplique o crossover
           dentro da taxa definida retorna True.'''

        # Faz a seleção por torneio e já insere na lista de espécies quais serão definidos para seleção
        teveCrossover: bool = False
        filhos: list = []
        pais: list = self.__torneioSelection()

        while (len(filhos) < len(pais)):
            # Pega o indivíduo aleatoriamente
            individuo1: Especie = pais[randrange(0, len(pais))]
            individuo2: Especie = pais[randrange(0, len(pais))]

            # Caso a taxa de crossover esteja dentro do determinado realiza o crossover
            if (self.__hasCrossover()):
                teveCrossover = True

                # Faz o crossover nos indivíduos recuperados na lista de especies da população
                filhos += self.__doCrossover(individuo1, individuo2)
            else:
                filhos += [individuo1, individuo2]

        # Substitui a nova espécie com os novos filhos
        self._especies = filhos

        return teveCrossover

    def bestAptidaoIndividuo(self):
        '''Pega o indivíduo de um população com melhor valor de aptidão/fitness'''
        return min(self._especies, key = lambda x: x.aptidao)

# Testes unitário do módulo
if __name__ == "__main__":
    populacao: Populacao = Populacao()
    print(populacao)