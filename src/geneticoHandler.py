# -*- coding: utf-8 -*-

"""
    Lida com a lógica de geração dos indivíduos da população e cálculos do algoritmo usando
    as classes Especie e Populacao.
"""

from Especie import Especie
from Populacao import Populacao

def generatePopulacao(numIndividuos: int, numBits: int) -> Populacao:
    '''Cria a população baseado no número de indivíduos e número de bits.'''

    populacao: Populacao = Populacao().criaIndividuos(numIndividuos, numBits)
    return populacao


    