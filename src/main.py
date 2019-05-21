import userInput
import geneticoHandler
from Populacao import Populacao

def main():
    # Entrada de dados do usuário com a cerca do estudo dos indivíduos da espécie de uma dada população
    # qntIndividuos: int = userInput.qntIndividuos()
    # precisaoIndividuos: int = userInput.precisaoIndividuos()
    # qntGeracoes: int = userInput.qntGeracoes()
    # taxaCrossover: float = userInput.taxaCrossoverPopulacao() / 100
    # taxaMutacao: float = userInput.taxaMutacaoPopulacao() / 100

    # Cria a população baseado na quantidade de indivíduos
    populacao: Populacao = geneticoHandler.generatePopulacao(4, 10, 0.6, 0.01)
    
    # Realiza a geração das espécies e pega os melhores valores de aptidão de cada geração
    bestAptidoes: dict = geneticoHandler.generateNewGeracoes(populacao, 5)
    print(bestAptidoes)

    return

if __name__ == "__main__":
    main()