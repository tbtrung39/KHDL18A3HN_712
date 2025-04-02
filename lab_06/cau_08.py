n = int(input("Nhập n: "))
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(n - 1)]
print(", ".join(map(str, fibonacci[:n+1])))
