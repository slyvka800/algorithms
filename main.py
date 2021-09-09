import time, sys, os
from merge_sort import merge_sort, SortOrder

arr = []

if __name__ == "__main__":

    terminal_args = sys.argv
    sort_order = terminal_args[1]
    if sort_order == "asc":
        sort_order = SortOrder.ASC
    else:
        sort_order = SortOrder.DESC

    arr = terminal_args[2].split(",")
    arr = [int(i) for i in arr]

    start = time.time()
    comparisons = merge_sort(arr, sort_order)
    end = time.time()
    time_elapsed = (end - start) * 1000

    print("Comparisons: ", comparisons)
    print("Execution time: ", time_elapsed, "ms")
    print(arr)

    command = "python3 -m unittest test_merge_sort.py"
    os.system(command)

