#reverse



def bubble_sort_right_to_left(arr):
    n = len(arr) 
    for i in range(n):
        swapped = False
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr




nums = [5, 10, 14, 21, 38]
print(bubble_sort_right_to_left(nums))