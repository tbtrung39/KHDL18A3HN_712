# bai 11
n = int(input("Hay nhap so sinh vien tham gia: "))

print("Hay nhap ds sinh vien thi C++:")
ds_cpp = input().split()
cpp = set()
for x in ds_cpp:
    cpp.add(int(x))

print("Hay nhap ds sinh vien tham gia thi java=:")
ds_java = input().split()
java = set()
for x in ds_java:
    java.add(int(x))

print("Hay nhap ds cac nhan vien =:")
ds_py = input().split()
python = set()
for x in ds_py:
    python.add(int(x))

tat_ca = set(range(1, n+1))

dem = {}
for sv in tat_ca:
    dem[sv] = 0
    if sv in cpp:
        dem[sv] += 1
    if sv in java:
        dem[sv] += 1
    if sv in python:
        dem[sv] += 1

chi_1 = []
chi_2 = []
ca_3 = []

for sv in dem:
    if dem[sv] == 1:
        chi_1.append(sv)
    elif dem[sv] == 2:
        chi_2.append(sv)
    elif dem[sv] == 3:
        ca_3.append(sv)

print("sinh vien chi thi 1 ngon ngu la =", sorted(chi_1))
print("sinh vien thi dung 2 ngon ngu la=", sorted(chi_2))
print("sinh vien thi 3 ngon ngu:", sorted(ca_3))
