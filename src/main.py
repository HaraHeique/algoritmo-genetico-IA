import userInput
import geneticoHandler
from Populacao import Populacao

def main():
    # Entrada de dados do usuário com a cerca do estudo dos indivíduos da espécie de uma dada população
    qntIndividuos: int = userInput.qntIndividuos()
    precisaoIndividuos: int = userInput.precisaoIndividuos()
    qntGeracoes: int = userInput.qntGeracoes()
    taxaCrossover: float = userInput.taxaCrossoverPopulacao() / 100
    taxaMutacao: float = userInput.taxaMutacaoPopulacao() / 100
    qntExecucoes: int = userInput.qntExecucoesAlgoritmo()

    for execucao in range(qntExecucoes):
        # Cria a população baseado na quantidade de indivíduos
        populacao: Populacao = geneticoHandler.generatePopulacao(qntIndividuos, precisaoIndividuos, taxaCrossover, taxaMutacao)
        
        # Realiza a geração das espécies e pega os melhores valores de aptidão de cada geração
        bestAptidoes: dict = geneticoHandler.generateNewGeracoes(populacao, qntGeracoes)
        geneticoHandler.createFile(bestAptidoes, qntGeracoes, qntIndividuos, execucao + 1)

    return

if __name__ == "__main__":
    main()