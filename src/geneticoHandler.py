# -*- coding: utf-8 -*-

"""
    Lida com a lógica de geração dos indivíduos da população e cálculos do algoritmo usando
    as classes Especie e Populacao.
"""

from Especie import Especie
from Populacao import Populacao
from matplotlib import pyplot
import os

# Variável global que armazena o local/diretório onde é guardado os arquivos
STORE_FILES_PATH: str = os.path.dirname(os.path.abspath(__file__)) + "/files/"

def generatePopulacao(numIndividuos: int, numBits: int, taxaCrossover: float, taxaMutacao: float) -> Populacao:
    '''Cria a população baseado no número de indivíduos e número de bits.'''

    populacao: Populacao = Populacao(None, taxaCrossover, taxaMutacao)
    populacao.criaIndividuos(numIndividuos, numBits)
    
    return populacao

def generateNewGeracoes(populacao: Populacao, numGeracoes: int) -> dict:
    '''Gera as novas espécies baseado em diversos fatores tais como: crossover entre pais e
       mutações pegando seu melhor valor de aptidão para cada geração'''

    bestEspeciesByGeneration: dict = {}

    for i in range(numGeracoes):
        # Aplica o crossover entre os pais baseado no seleção de torneio e valor de aptidão de cada invíduo da espécie
        teveCrossover: bool = populacao.aplicaCrossover()

        # Aplica a mutação para cada invidíduo da população
        teveMutacao: bool = populacao.aplicaMutacao()

        # Pega o melhor valor de aptidão dentre todos da espécies e armazena
        bestEspeciesByGeneration[i+1] = populacao.bestAptidaoIndividuo()

    return bestEspeciesByGeneration
        
def createFile(bestEspecies: dict, numGeracoes: int, numIndividuos: int, execucao: int) -> None:
    '''Cria o arquivo CSV com as informações dos melhores valores de aptidão para
       cada geração'''
    try:
        filename: str = "{0}_geracoes_{1}_individuos_{2}_execucao.csv".format(numGeracoes, numIndividuos, execucao)
        with open(STORE_FILES_PATH + filename, "wt") as outfile:
            outfile.write("Geração;Aptidão(f(x))\n")
            for key in sorted(bestEspecies.keys()):
                outfile.write("%d;%.10f\n" %(key, bestEspecies[key].aptidao))

    except IOError:
        raise Exception("Não foi possível abrir o arquivo.")
    
def calcularMediaNormalizacao(bestEspecies: list) -> list:
    numIndividuosPorGeracao: int = len(bestEspecies[0]) if len(bestEspecies) > 0 else 0
    normalizadoValuesPorExecutions: list = []

    # Pega valor de normalização na lista dicionários de espécie para realizar o cálculo da média de cada um
    for i in range(numIndividuosPorGeracao):
        # Pega uma lista de floats com os valores da normalização
        normalizacoesList: list = list(map(lambda d: d[i+1].normalizado, bestEspecies))
        normalizadoValuesPorExecutions.append(normalizacoesList)

    # Calcula a média dos valores na lista de normalização e adiciona na lista
    numExecucoes: int = len(bestEspecies)
    somaNormalizacaoPorExecucao: list = [sum(y) for y in zip(*normalizadoValuesPorExecutions)]
    mediaNormalizacoesPorExecucao: list = [y/numExecucoes for y in somaNormalizacaoPorExecucao]

    return mediaNormalizacoesPorExecucao

def gerarGraficoNormalizacao(mediaNormalizacao: list) -> None:
    geracoes: list = [(i+1) for i in range(len(mediaNormalizacao))]

    # Nomeando os eixos x e y
    pyplot.xlabel("Geração")
    pyplot.ylabel("Valor de normalização")

    # Plotando e construindo o gráfico
    pyplot.plot(geracoes, mediaNormalizacao)

    # Mostrando o gráfico na tela
    pyplot.show()

