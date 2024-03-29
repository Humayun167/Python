def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


try:
    input_list = input("Enter a list of integers separated by spaces: ").split()
    input_list = [int(x) for x in input_list]
except ValueError:
    print("Please enter integers only, separated by spaces.")
else:
    print("Original List:", input_list)

    bubble(input_list)

    print("Sorted List:", input_list)
