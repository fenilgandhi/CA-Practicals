{
    "Author": "Fenil Gandhi",
    "Version": "Python 3.6.2",
    "Description": "Implementation of max-heap sort algorithm",
    "Input": [87, 30, 33, 61, 75, 16, 14, 7, 35],
    "Output": [7, 14, 16, 30, 33, 35, 61, 75, 87],
}

import random 

def HeapSort(array):
    array_length = len(array)

    # Swap 2 nodes given their index
    def swap_nodes(a, b):
        array[a], array[b] = array[b], array[a]

    # Generate Heap using a recursive strategy
    def heapify(length, largest):
        new_largest = largest
        left_node = (2 * largest) + 1
        right_node = (2 * largest) + 2

        # Check if left_node exists and largest < left_node then swap
        if (left_node < length) and (array[new_largest] < array[left_node]):
            new_largest = left_node

        # Check if right_node exists and is_gt(largest) then swap_nodes
        if (right_node < length) and (array[new_largest] < array[right_node]):
            new_largest = right_node

        if new_largest != largest:
            swap_nodes(new_largest, largest)
            heapify(length, new_largest)

    # Make Initial Heap
    for i in range(array_length - 1, -1, -1):
        heapify(array_length, i)

    # Extract Last Element and Redo the process
    for i in range(array_length - 1, 0, -1):
        swap_nodes(i, 0)
        heapify(i, 0)

    return array


if __name__ == '__main__':
    # Generate random array of 100 integers
    array = [random.randint(0,10000) for _ in range(100)]
    print("Array : ", array)

    sorted_array = HeapSort(array)
    print("\nSorted Array : ", sorted_array)
