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
    taxaMutacao: float = 0.1
    qntExecucoes: int = 1

    bestEspeciesBinarioList: list = []
    bestEspeciesRealList: list = []

    for execucao in range(qntExecucoes):
        # Cria a população baseado na quantidade de indivíduos
        populacaoBinario: Populacao = geneticoHandler.generatePopulacaoBinario(qntIndividuos, precisaoIndividuos, taxaCrossover, taxaMutacao)
        populacaoReal: Populacao = geneticoHandler.generatePopulacaoReal(qntIndividuos, taxaCrossover, taxaMutacao)

        # Realiza a geração das espécies e pega os melhores valores de aptidão de cada geração
        bestEspeciesBinario: dict = geneticoHandler.generateNewGeracoes(populacaoBinario, qntGeracoes)
        bestEspeciesReal: dict = geneticoHandler.generateNewGeracoes(populacaoReal, qntGeracoes)
        
        #geneticoHandler.createFile(bestEspeciesBinario, qntGeracoes, qntIndividuos, execucao + 1)
        #geneticoHandler.createFile(bestEspeciesReal, qntGeracoes, qntIndividuos, execucao + 1)

        # Pega as melhores espécies com os melhores valores de aptidão
        bestEspeciesBinarioList.append(bestEspeciesBinario)
        bestEspeciesRealList.append(bestEspeciesReal)

    # Calcula a média de normalização para cada geração das execuções
    #mediaNormalizacoes: list = geneticoHandler.calcularMediaNormalizacao(bestEspeciesList, qntGeracoes)
    mediaAptidaoBinario: list = geneticoHandler.calcularMediaAptidao(bestEspeciesBinarioList, qntGeracoes)
    mediaAptidaoReal: list = geneticoHandler.calcularMediaAptidao(bestEspeciesRealList, qntGeracoes)

    # Mostra o gráfico utilizando o matplot
    #geneticoHandler.gerarGraficoNormalizacao(mediaNormalizacoes)
    geneticoHandler.gerarGraficoAptidao(mediaAptidaoBinario, "Média do fitness para espécie binária")
    geneticoHandler.gerarGraficoAptidao(mediaAptidaoReal, "Média do fitness para espécie real")

    
    return

if __name__ == "__main__":
    main()