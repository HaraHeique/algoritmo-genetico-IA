# -*- coding: utf-8 -*-

"""
    Classe que representa o indivíduo da espécie.
"""

from random import randrange

class Especie:
    '''Classe que representa o indivíduo da espécie.'''
    def __init__(self, nBits: int, dominioX: tuple = None):
        self._binario: str = self.__geraNumeroBinario(nBits)
        self._dominio: tuple = dominioX if dominioX != None else (-10,10)
        self._aptidao: float = self.calculaAptidao()

    @property
    def individuo(self):
        return self._binario

    @property
    def aptidao(self):
        return self._aptidao

    @individuo.setter
    def individuo(self, value: str):
        self._binario = value
        self._aptidao = self.calculaAptidao()

    # Cria o indivíduo da espécie de forma aleatória de acordo com o número de bits
    def __geraNumeroBinario(self, numBits: int) -> str:
        individuoBin: str = ''

        while (numBits > 0):
            individuoBin += str(randrange(0,2))
            numBits -= 1

        return individuoBin

    # Calcula o vetor de bits, transformando-os em um número inteiro na base decimal
    def __converteBaseDecimal(self) -> int:
        tam: int = len(self._binario)
        count: int = 0
        b10: int = 0

        while tam > 0:
            if(self._binario[tam-1]=='1'):
                b10 += 2 ** count
            count += 1
            tam -= 1

        return b10

    # Calcula o número real normalizado
    def __calculaNormalizacao(self) -> float:
        min: int = self._dominio[0]
        max: int = self._dominio[1]
        base10: int = self.__converteBaseDecimal()
        l: int = len(self._binario)

        # Realiza o cálculo da normalização
        x: float = min + (max - min) * (base10 / (2**l) - 1)

        return x

    # Calcula a aptidão do indivíduo da espécie
    def calculaAptidao(self) -> float:
        '''Calcula a aptidão/fitness do indivíduo da espécie baseado em seu cálculo de normalização.'''
        x: float = self.__calculaNormalizacao()
        fx: float = (x**2) - (3 * x) + 4
        
        return fx