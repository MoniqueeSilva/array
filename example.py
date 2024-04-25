import sort_algorithms as sort_algorithms # renomeia permitindo acessar funções
import aux_functions as aux # renomeia permitindo acessar funções
from timeit import default_timer as timer # medir o tempo de execução dos algoritmos

# Definição/nomes dos algoritmos a serem comparados
alg_names = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Quick Sort", "Merge Sort"]

n_experiments = 100  # Número de experimentos para cada tamanho de array

# Lista dos tamanhos dos arrays (N)
N_values = list(range(1, 11)) + list(range(20, 260, 10))

# Número total de diferentes tamanhos de array
len_n_samples = len(N_values)

# Lista para armazenar os tempos de execução de cada algoritmo para cada tamanho de array
time_samples = [[] for _ in range(len(alg_names))]

# Loop iterativo para cada tamanho de array
for i in range(len_n_samples):
    elapsed_time = [[] for _ in range(len(alg_names))]  # Lista para armazenar os tempos de execução de cada algoritmo para o tamanho de array atual
    
    # Loop iterativo para cada experimento
    for j in range(n_experiments):
        array = aux.create_array(N_values[i])  # Cria um array aleatório com o tamanho de array atual
        
        # Exibe o array gerado
        print("Array (primeiros 5 elementos): ", array[:5])
         # Medição do tempo de execução de cada algoritmo
        for k, alg_name in enumerate(alg_names):
            start = timer()  # Marca o tempo de início
            if alg_name == "Bubble Sort":
                sort_algorithms.bubbleSort(array.copy())  # Executa o algoritmo de ordenação
            elif alg_name == "Insertion Sort":
                sort_algorithms.insertionSort(array.copy())  # Executa o algoritmo de ordenação
            elif alg_name == "Selection Sort":
                sort_algorithms.selectionSort(array.copy())  # Executa o algoritmo de ordenação
            elif alg_name == "Quick Sort":
                sort_algorithms.quickSort(array.copy())  # Executa o algoritmo de ordenação
            else:
                sort_algorithms.mergeSort(array.copy())  # Executa o algoritimo de ordenação
            elapsed_time[k].append(timer() - start)  # Calcula o tempo de execução e armazena na lista
    
    # Calcula a média dos tempos de execução para cada algoritmo e tamanho de array
    for k in range(len(alg_names)):
        time_samples[k].append(sum(elapsed_time[k]) / n_experiments)

# Plotagem dos resultados
aux.plot_results(N_values, time_samples, alg_names)

# Encerrar o programa
exit()