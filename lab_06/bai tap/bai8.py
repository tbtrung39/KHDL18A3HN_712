n = int(input("Nhập số n: "))
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(2, n)]
print(", ".join(map(str, fibonacci[:n])))
