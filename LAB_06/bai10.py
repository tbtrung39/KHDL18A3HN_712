n = int(input("Nhap so phan tu: "))
a = [int(input(f"Nhap phan tu thu {i + 1}: ")) for i in range(n)]
frequency = {}
for value in a:
    frequency[value] = frequency.get(value, 0) + 1
max_freq = max(frequency.values())
most_frequent = [key for key, val in frequency.items() if val == max_freq]
print("So xuat hien nhieu nhat la:", most_frequent, "voi tan suat", max_freq)
