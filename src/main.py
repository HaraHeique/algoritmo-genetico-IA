import userInput
import geneticoHandler
from Populacao import Populacao

def main():
    # Entrada de dados do usuário com a cerca do estudo dos indivíduos da espécie de uma dada população
    qntIndividuos: int = userInput.qntIndividuos()
    precisaoIndividuos: int = userInput.precisaoIndividuos()
    qntGeracoes: int = userInput.qntGeracoes()
    taxaCrossover: float = userInput.taxaCrossoverPopulacao()
    taxaMutacao: float = userInput.taxaMutacaoPopulacao()

    # Cria a população baseado na quantidade de indivíduos
    populacao: Populacao = geneticoHandler.generatePopulacao(qntIndividuos, precisaoIndividuos)

    return

if __name__ == "__main__":
    main()