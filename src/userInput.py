# -*- coding: utf-8 -*-

"""
    Responsável por lidar com a entrada de dados do usuário especificamente para o algoritmo genético
"""

# Determina o número de indivíduos da população de uma da espécie que é fornecida pelo usuário
def qntIndividuos() -> int :
    while (True) :
        numIndividuosInput: str = input("Insira o número de indivíduos da população a ser estudada: ")

        if (__tryParseIntPositive(numIndividuosInput)) :
            return int(numIndividuosInput)

# Determina o número de gerações da população de uma da espécie que é fornecida pelo usuário
def qntGeracoes() -> int :
    while (True) :
        numGeracoesInput: str = input("Insira o número de gerações da população a ser estudada: ")

        if (__tryParseIntPositive(numGeracoesInput)) :
            return int(numGeracoesInput)

# Determina o número de bits/precisão da população de uma da espécie que é fornecida pelo usuário
def precisaoIndividuos() -> int :
    while (True) :
        numBits: str = input("Insira a precisão(número de bits) da população a ser estudada: ")

        if (__tryParseIntPositive(numBits)) :
            return int(numBits)

# Pega a taxa de crossover que é fornecida pelo usuário
def taxaCrossoverPopulacao() -> float :
    while (True) :
        taxaDeCrossover: str = input("Insira a taxa de crossover da população(60% a 90%): ")

        if (__tryParseIntPositive(taxaDeCrossover) and __isBetweenValues(60, 90, float(taxaDeCrossover))) :
            return float(taxaDeCrossover)

# Pega a taxa de crossover que é fornecida pelo usuário
def taxaMutacaoPopulacao() -> float :
    while (True) :
        taxaMutacao: str = input("Insira a taxa de mutação da população(até 10%): ")

        if (__tryParseIntPositive(taxaMutacao) and __isBetweenValues(0, 10, float(taxaMutacao))) :
            return float(taxaMutacao)

# Determina o número de execuções do algoritmo
def qntExecucoesAlgoritmo() -> int :
    while (True) :
        numExecucoes: str = input("Insira o número de execuções do algoritmo: ")

        if (__tryParseIntPositive(numExecucoes)) :
            return int(numExecucoes)

# Checa se a string passa é possível de converter para um inteiro positivo
def __tryParseIntPositive(strInt: str) -> bool :
    if (not strInt.isdigit() or int(strInt) < 0) :
        print("Favor digite um valor inteiro válido e positivo!")
        return False

    return True

def __isBetweenValues(minValue: float, maxValue: float, value: float) -> bool :
    if (value <= maxValue and value >= minValue):
        return True

    return False