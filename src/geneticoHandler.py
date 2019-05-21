# -*- coding: utf-8 -*-

"""
    Lida com a lógica de geração dos indivíduos da população e cálculos do algoritmo usando
    as classes Especie e Populacao.
"""

from Especie import Especie
from Populacao import Populacao

def generatePopulacao(numIndividuos: int, numBits: int, taxaCrossover: float, taxaMutacao: float) -> Populacao:
    '''Cria a população baseado no número de indivíduos e número de bits.'''

    populacao: Populacao = Populacao(None, taxaCrossover, taxaMutacao)
    populacao.criaIndividuos(numIndividuos, numBits)
    
    return populacao

def generateNewGeracoes(populacao: Populacao, numGeracoes: int) -> dict:
    '''Gera as novas espécies baseado em diversos fatores tais como: crossover entre pais e
       mutações pegando seu melhor valor de aptidão para cada geração'''

    bestAptidoes: dict = {}

    for i in range(numGeracoes):
        # Aplica o crossover entre os pais baseado no seleção de torneio e valor de aptidão de cada invíduo da espécie
        teveCrossover: bool = populacao.aplicaCrossover()

        # Aplica a mutação para cada invidíduo da população
        teveMutacao: bool = populacao.aplicaMutacao()

        # Pega o melhor valor de aptidão dentre todos da espécies e armazena
        bestAptidoes[i+1] = populacao.bestAptidaoIndividuo().aptidao

    return bestAptidoes
        
    
    