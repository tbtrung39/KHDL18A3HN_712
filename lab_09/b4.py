def swap(arr, i, j):
    # Hàm để hoán đổi hai phần tử trong danh sách
    arr[i], arr[j] = arr[j], arr[i]

def generate_permutations(arr, start, end):
    if start == end:
        print(arr)  # In ra hoán vị hiện tại
    else:
        for i in range(start, end + 1):
            swap(arr, start, i)  # Hoán đổi phần tử
            generate_permutations(arr, start + 1, end)  # Gọi đệ quy
            swap(arr, start, i)  # Hoán đổi lại để khôi phục trạng thái ban đầu

# Nhập số tự nhiên n từ bàn phím
n = int(input("Nhập một số tự nhiên n: "))

# Tạo dãy [1, 2, ..., n]
sequence = list(range(1, n + 1))

# In ra tất cả các hoán vị
print(f"Tất cả các hoán vị của dãy {sequence} là:")
generate_permutations(sequence, 0, n - 1)