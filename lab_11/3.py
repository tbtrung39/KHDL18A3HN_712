with open(r"D:\24174600126_NguyenTienLuc_DHKL18A3\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\lab_11\f_in.dat", "r") as file:
    a = list(map(int, file.read().split()))

maxima = []
minima = []

for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        maxima.append(a[i])
    if a[i - 1] > a[i] < a[i + 1]:
        minima.append(a[i])

with open("f_out.dat", "w") as file:
    file.write(" ".join(map(str, maxima)) + "\n")
    file.write(" ".join(map(str, minima)))
