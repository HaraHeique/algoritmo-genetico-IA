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
    # qntExecucoes: int = userInput.qntExecucoesAlgoritmo()

    qntIndividuos: int = 100
    precisaoIndividuos: int = 10
    qntGeracoes: int = 10
    taxaCrossover: float = 0.6
    taxaMutacao: float = 0.01
    qntExecucoes: int = 1

    bestEspeciesList: list = []

    for execucao in range(qntExecucoes):
        # Cria a população baseado na quantidade de indivíduos
        populacao: Populacao = geneticoHandler.generatePopulacao(qntIndividuos, precisaoIndividuos, taxaCrossover, taxaMutacao)
        
        # Realiza a geração das espécies e pega os melhores valores de aptidão de cada geração
        bestEspecies: dict = geneticoHandler.generateNewGeracoes(populacao, qntGeracoes)
        geneticoHandler.createFile(bestEspecies, qntGeracoes, qntIndividuos, execucao + 1)

        # Pega as melhores espécies com os melhores valores de aptidão
        bestEspeciesList.append(bestEspecies)

    # Calcula a média de normalização para cada geração das execuções
    mediaNormalizacoes: list = geneticoHandler.calcularMediaNormalizacao(bestEspeciesList, qntGeracoes)
    mediaAptidao: list = geneticoHandler.calcularMediaAptidao(bestEspeciesList, qntGeracoes)

    # Mostra o gráfico utilizando o matplot
    geneticoHandler.gerarGraficoAptidao(mediaAptidao)
    geneticoHandler.gerarGraficoNormalizacao(mediaNormalizacoes)

    
    return

if __name__ == "__main__":
    main()