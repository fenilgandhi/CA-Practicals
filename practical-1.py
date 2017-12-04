{
    "Author": "Fenil Gandhi",
    "Version": "Python 3.6.2",
    "Description": "Implementation and Time analysis of sorting algorithms",
    "Algorithms": ["Bubble Sort", "Selection Sort", "Merge Sort", "Insertion Sort", "Quick Sort"],
    "Input Sizes": [10, 50, 100, 500, 1000, 5000, 10000, 25000],
    "Output" : {
        "Bubble Sort" : "",
        "Selection Sort" : "",
        "Merge Sort" : "",
        "Insertion Sort" : "",
        "Quick Sort" : "",
    }
}

import random
import time


def timeit(func):
    def decorated_function(*args):
        a = time.time()
        func(*args)
        b = time.time()
        return (b - a)
    return decorated_function


def generate_sorted_array(size):
    return [i for i in range(size)]


def generate_reverse_sorted_array(size):
    return [i for i in range(size, 0, -1)]


def generate_random_array(size):
    return [random.randint(0, size) for i in range(size)]


@timeit
def BubbleSort(input):
    for i in range(len(input) - 1, 0, -1):
        for j in range(i):
            if (input[j] > input[j + 1]):
                input[j], input[j + 1] = input[j + 1], input[j]
    return input


@timeit
def SelectionSort(input):
    for i in range(len(input)):
        min = i
        for j in range(i, len(input)):
            if (input[j] < input[min]):
                min = j
        input[i], input[min] = input[min], input[i]
    return input


@timeit
def MergeSort(input):

    def sort(input):
        if len(input) > 1:
            mid = len(input) // 2

            left = sort(input[:mid])
            right = sort(input[mid:])

            result = []
            i, j = 0, 0
            len_l, len_r = len(left), len(right)
            while (i < len_l) and (j < len_r):
                if (left[i] <= right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result += left[i:] + right[j:]

            return result
        else:
            return input
    return sort(input)


@timeit
def InsertionSort(input):
    for i in range(len(input)):
        while ((i > 0) and (input[i] < input[i - 1])):
            input[i], input[i - 1] = input[i - 1], input[i]
            i -= 1
    return input


@timeit
def QuickSort(array):
    subarrays = [(0, len(array) - 1)]

    def sort(start, end):
        if ((end - start) < 1):
            return

        pivot = array[start]
        lt = []
        equal = [pivot]
        gt = []
        for i in array[start + 1:end + 1]:
            if (i < pivot):
                lt.append(i)
            elif(i > pivot):
                gt.append(i)
            else:
                equal.append(i)

        array[start:end + 1] = lt + equal + gt
        subarrays.append((start, start + len(lt) - 1))
        subarrays.append((end - len(gt) + 1, end))

    for each_subarray in subarrays:
        sort(*each_subarray)

    return array


def print_formatted(name, input_sizes, sorted_array_time, random_sorted_time, reverse_sorted_time):
    print(" " * 60, "{0:^50s}".format(name), "-" * 55, sep="\n")
    print("| {0:^10s} | {1:^10s} | {2:^10s} | {3:^10s} |".format("Input", "Sorted", "R-Sorted", "Random"))
    print("-" * 55)
    for i in range(len(input_sizes)):
        print("| {0:>10d} | {1:>10f} | {2:>10f} | {3:>10f} |" .format(input_sizes[i], sorted_array_time[i], random_sorted_time[i], reverse_sorted_time[i]))
    print("-" * 55, end="\n\n")


if __name__ == '__main__':
    input_sizes = [10, 50, 100, 500, 1000, 5000, 10000, 25000]

    # Insertion Sort
    sorted_array_time, random_sorted_time, reverse_sorted_time = [], [], []
    for each_input in input_sizes:
        sorted_array = generate_sorted_array(each_input)
        reverse_sorted = generate_reverse_sorted_array(each_input)
        random_sorted = generate_random_array(each_input)

        sorted_array_time.append(InsertionSort(sorted_array))
        reverse_sorted_time.append(InsertionSort(reverse_sorted))
        random_sorted_time.append(InsertionSort(random_sorted))
    print_formatted("Insertion Sort", input_sizes, sorted_array_time, random_sorted_time, reverse_sorted_time)

    # Selection Sort
    sorted_array_time, random_sorted_time, reverse_sorted_time = [], [], []
    for each_input in input_sizes:
        sorted_array = generate_sorted_array(each_input)
        reverse_sorted = generate_reverse_sorted_array(each_input)
        random_sorted = generate_random_array(each_input)

        sorted_array_time.append(SelectionSort(sorted_array))
        reverse_sorted_time.append(SelectionSort(reverse_sorted))
        random_sorted_time.append(SelectionSort(random_sorted))
    print_formatted("Selection Sort", input_sizes, sorted_array_time, random_sorted_time, reverse_sorted_time)

    # Quick Sort
    sorted_array_time, random_sorted_time, reverse_sorted_time = [], [], []
    for each_input in input_sizes:
        sorted_array = generate_sorted_array(each_input)
        reverse_sorted = generate_reverse_sorted_array(each_input)
        random_sorted = generate_random_array(each_input)

        sorted_array_time.append(QuickSort(sorted_array))
        reverse_sorted_time.append(QuickSort(reverse_sorted))
        random_sorted_time.append(QuickSort(random_sorted))
    print_formatted("Quick Sort", input_sizes, sorted_array_time, random_sorted_time, reverse_sorted_time)

    # Merge Sort
    sorted_array_time, random_sorted_time, reverse_sorted_time = [], [], []
    for each_input in input_sizes:
        sorted_array = generate_sorted_array(each_input)
        reverse_sorted = generate_reverse_sorted_array(each_input)
        random_sorted = generate_random_array(each_input)

        sorted_array_time.append(MergeSort(sorted_array))
        reverse_sorted_time.append(MergeSort(reverse_sorted))
        random_sorted_time.append(MergeSort(random_sorted))
    print_formatted("Merge Sort", input_sizes, sorted_array_time, random_sorted_time, reverse_sorted_time)

    # Bubble Sort
    sorted_array_time, random_sorted_time, reverse_sorted_time = [], [], []
    for each_input in input_sizes:
        sorted_array = generate_sorted_array(each_input)
        reverse_sorted = generate_reverse_sorted_array(each_input)
        random_sorted = generate_random_array(each_input)

        sorted_array_time.append(BubbleSort(sorted_array))
        reverse_sorted_time.append(BubbleSort(reverse_sorted))
        random_sorted_time.append(BubbleSort(random_sorted))
    print_formatted("Bubble Sort", input_sizes, sorted_array_time, random_sorted_time, reverse_sorted_time)
