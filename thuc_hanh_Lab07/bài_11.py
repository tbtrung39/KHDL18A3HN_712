n = int(input("Nhập số sinh viên: "))
t = list(map(int, input("Nhập sinh viên thi C++: ").split()))
k = list(map(int, input("Nhập sinh viên thi Java: ").split()))
h = list(map(int, input("Nhập sinh viên thi Python: ").split()))
dem = {}  
for sv in t + k + h:
    if sv in dem:
        dem[sv] += 1
    else:
        dem[sv] = 1
chi_1_ngon_ngu = []
dung_2_ngon_ngu = []
ca_3_ngon_ngu = []

for sv in range(1, n+1):
    if dem.get(sv, 0) == 1:
        chi_1_ngon_ngu.append(sv)
    elif dem.get(sv, 0) == 2:
        dung_2_ngon_ngu.append(sv)
    elif dem.get(sv, 0) == 3:
        ca_3_ngon_ngu.append(sv)
print("Sinh viên chỉ thi 1 ngôn ngữ:", chi_1_ngon_ngu)
print("Sinh viên thi đúng 2 ngôn ngữ:", dung_2_ngon_ngu)
print("Sinh viên thi cả 3 ngôn ngữ:", ca_3_ngon_ngu)
