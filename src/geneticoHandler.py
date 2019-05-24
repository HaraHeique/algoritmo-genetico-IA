# -*- coding: utf-8 -*-

"""
    Lida com a lógica de geração dos indivíduos da população e cálculos do algoritmo usando
    as classes Especie e Populacao.
"""

from Especie import Especie
from Populacao import Populacao
from matplotlib import pyplot
import os, copy

# Variável global que armazena o local/diretório onde é guardado os arquivos
STORE_FILES_PATH: str = os.path.dirname(os.path.abspath(__file__)) + "/files/"

# Cria o diretório onde armazena a partir da quantidade de iterações
if not os.path.exists(STORE_FILES_PATH):
    os.makedirs(STORE_FILES_PATH)

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
        bestEspeciesByGeneration[i+1] = copy.deepcopy(populacao.bestAptidaoIndividuo())

    return bestEspeciesByGeneration
        
def createFile(bestEspecies: dict, numGeracoes: int, numIndividuos: int, execucao: int) -> None:
    '''Cria o arquivo CSV com as informações dos melhores valores de aptidão para
       cada geração'''
    try:
        filename: str = "{0}_geracoes_{1}_individuos_{2}_execucao.csv".format(numGeracoes, numIndividuos, execucao)
        with open(STORE_FILES_PATH + filename, "wt") as outfile:
            outfile.write("Geração;Normalizado(x);Aptidão(f(x))\n")
            for key in sorted(bestEspecies.keys()):
                outfile.write("%d;%.10f;%.10f\n" %(key, bestEspecies[key].normalizado,bestEspecies[key].aptidao))

    except IOError:
        raise Exception("Não foi possível abrir o arquivo.")
    
def calcularMediaNormalizacao(bestEspecies: list, numGeracoes: int) -> list:
    mediaNormalizacoes: list = []

    # Pega valor de normalização na lista dicionários de espécie para realizar o cálculo da média de cada um
    for i in range(numGeracoes):
        # Pega uma lista de floats com os valores da normalização
        normalizacoesList: list = list(map(lambda d: d[i+1].normalizado, bestEspecies))
        
        # Faz o cálculo da normalização de acordo com o número de execuções e adiciona na lista de médias por cada geração
        mediaNormalizacaoCorrente: float = sum(normalizacoesList) / len(normalizacoesList)
        mediaNormalizacoes.append(mediaNormalizacaoCorrente)
    
    return mediaNormalizacoes


def calcularMediaAptidao(bestEspecies: list, numGeracoes: int) -> list:
    mediaAptidoes: list = []

    # Pega valor de normalização na lista dicionários de espécie para realizar o cálculo da média de cada um
    for i in range(numGeracoes):
        # Pega uma lista de floats com os valores da normalização
        aptidaoList: list = list(map(lambda d: d[i + 1].aptidao, bestEspecies))

        # Faz o cálculo da normalização de acordo com o número de execuções e adiciona na lista de médias por cada geração
        mediaAptidaoCorrente: float = sum(aptidaoList) / len(aptidaoList)
        mediaAptidoes.append(mediaAptidaoCorrente)

    return mediaAptidoes

def gerarGraficoNormalizacao(mediaNormalizacao: list) -> None:
    geracoes: list = [(i+1) for i in range(len(mediaNormalizacao))]

    # Nomeando os eixos x e y
    pyplot.xlabel("Geração")

    pyplot.ylabel("Valor de normalização")

    # Plotando e construindo o gráfico
    pyplot.plot(geracoes, mediaNormalizacao, marker='.')

    # Mostrando o gráfico na tela
    pyplot.show()

def gerarGraficoAptidao(mediaAptidao: list) -> None:
    geracoes: list = [(i+1) for i in range(len(mediaAptidao))]

    # Nomeando os eixos x e y
    pyplot.xlabel("Geração")
    pyplot.ylabel("Valor de fitness")

    # Plotando e construindo o gráfico
    pyplot.plot(geracoes, mediaAptidao, marker='.')

    # Mostrando o gráfico na tela
    pyplot.show()
