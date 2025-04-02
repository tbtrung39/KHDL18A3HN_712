n = int(input("Nhập số phần tử n: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
C = [x**2 for x in A]
D = [x for x in A if x % 3 == 0]
print("Danh sách A:", A)
print("Danh sách B:", B)
print("Danh sách C:", C)
print("Danh sách D:", D)
