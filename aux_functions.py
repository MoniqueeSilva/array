import random # gerar números aleatórios
import matplotlib.pyplot as plt # plotar gráfico

# Cria um array de n elementos aleatórios
# n_elements: tamanho do array (número de elementos)
def create_array(n_elements):
    return random.sample(range(1, (n_elements + 1) * 10), n_elements)

# Traça o gráfico de comparação de algoritmos de ordenação
# N_values: lista de tamanhos de array
# time_elapsed: lista de médias de tempo decorrido para cada algoritmo e tamanho de array N
# alg_names: lista de nomes de algoritmos
def plot_results(N_values, time_elapsed, alg_names):
    for i, alg_name in enumerate(alg_names):
        plt.plot(N_values, time_elapsed[i], label=alg_name, lw=2) # plotar os resultados
    
    plt.grid(True)                                  # Mostra as grades
    plt.title("Comparação de Algoritmos de Ordenação")     # Define o título
    plt.legend(loc="upper left")                    # Posiciona a legenda
    plt.xlabel("Tamanho da Entrada (N)")            # Rótulo do eixo x 
    plt.ylabel("Tempo decorrido (segundos)")        # Rótulo do eixo y
    plt.show()                                      # Mostra o gráfico
