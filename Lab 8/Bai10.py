#Bai10
def uoc_so(n):
    print("Cac uoc so cua", n, "la:", end=' ')
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=' ')
n = int(input("Nhap so nguyen duong: "))
uoc_so(n)