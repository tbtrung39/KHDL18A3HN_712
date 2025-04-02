n = int(input("Nhập số n: "))
if n <= 0:
    print("Nhập số n lớn hơn 0.")
elif n == 1:
    fibonacci = [0]
else:
    fibonacci = [0, 1]
    for i in range(2, n + 1):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(", ".join(map(str, fibonacci)))