#Bai3
def ktra_so_nguyento(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def so_nguyento_nho_hon_n(n):
    for i in range(2, n):
        if ktra_so_nguyento(i):
            print(i, end=' ')
n = int(input("Nhập số nguyên dương n: "))
print("Các số nguyên tố nhỏ hơn", n, "là:", end=' ')
so_nguyento_nho_hon_n(n)