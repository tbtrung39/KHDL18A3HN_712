import random
A = [random.randint(1, 99999) for _ in range(1000)]
A_sorted = sorted(A)
print("Danh sách sau khi sắp xếp (sử dụng sorted):", A_sorted[:10])
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]  
                swapped = True
        if not swapped:
            break


A = [random.randint(1, 99999) for _ in range(1000)]
A_copy = A[:]
bubble_sort(A_copy)
print("Danh sách sau khi sắp xếp (Bubble Sort):", A_copy[:10])