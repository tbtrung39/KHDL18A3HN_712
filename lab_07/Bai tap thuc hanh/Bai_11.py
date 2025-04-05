n = int(input("Nhập số lượng sinh viên n: "))
c_plus = set(map(int, input("Nhập danh sách sinh viên thi C++: ").split()))
java = set(map(int, input("Nhập danh sách sinh viên thi Java: ").split()))
python = set(map(int, input("Nhập danh sách sinh viên thi Python: ").split()))

mot_ngon_ngu = (c_plus - java - python) | (java - c_plus - python) | (python - c_plus - java)
hai_ngon_ngu = ((c_plus & java) - python) | ((c_plus & python) - java) | ((java & python) - c_plus)
ba_ngon_ngu = c_plus & java & python

print("Sinh viên chỉ thi 1 ngôn ngữ:", sorted(mot_ngon_ngu))
print("Sinh viên thi 2 ngôn ngữ:", sorted(hai_ngon_ngu))
print("Sinh viên thi cả 3 ngôn ngữ:", sorted(ba_ngon_ngu))
