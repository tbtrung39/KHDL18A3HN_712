n = int(input("Nhap so luong so Fibonacci can in: "))
fib = [0, 1] if n > 1 else ([0] if n == 1 else []) 
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
ket_qua = ", ".join(map(str, fib))
print("Day Fibonacci:", ket_qua)
