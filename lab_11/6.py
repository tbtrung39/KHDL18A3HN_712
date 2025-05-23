with open(r"D:\24174600126_NguyenTienLuc_DHKL18A3\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\lab_11\matrix.txt", "r") as f:
    lines = f.readlines()
    matrix = [list(map(int, line.split())) for line in lines]

print("Dòng đầu tiên:", matrix[0])
print("Dòng thứ 3:", matrix[2])
odd_matrix = []
for row in matrix:
    odd_row = [num if num % 2 == 1 else 0 for num in row]
    odd_matrix.append(odd_row)

with open("ODD.txt", "w") as f:
    for row in odd_matrix:
        f.write(" ".join(map(str, row)) + "\n")
    f.write("Dòng cuối: " + " ".join(map(str, odd_matrix[-1])))
