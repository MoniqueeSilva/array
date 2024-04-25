# Algoritmo de ordenação Insertion Sort
# Array: array a ser classificado (ordem crescente)
def insertionSort(array):
    for i in range(1, len(array)):
        chave = array[i]
        j = i-1
        while j >= 0 and chave < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = chave 

# Algoritmo de ordenação Bubble Sort
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

# Algoritmo de ordenação Selection Sort
def selectionSort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

# Algoritmo de Ordenação Quick Sort
def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        meio = len(array) // 2
        pivot = array[meio]
        menores = [x for x in array if x < pivot]
        iguais = [x for x in array if x == pivot]
        maiores = [x for x in array if x  > pivot]
        return quickSort(menores) + iguais + quickSort(maiores)

# Algoritmo de ordenação Marge Sort
def mergeSort(array):
    if len(array) <= 1:
        return array
    meio = len(array) // 2
    esquerda = array[:meio]
    direita = array[meio:]

    esquerda = mergeSort(esquerda)
    direita = mergeSort(direita)

    return merge(esquerda, direita)
def merge(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado