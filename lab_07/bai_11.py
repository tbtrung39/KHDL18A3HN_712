n = int(input("Nhap so luong sinh vien n: "))
c_plus = set(map(int, input("Nhap danh sach sinh vien thi C++: ").split()))
java = set(map(int, input("Nhap danh sach sinh vien thi Java: ").split()))
python = set(map(int, input("Nhap danh sach sinh vien thi Python: ").split()))

mot_ngon_ngu = (c_plus - java - python) | (java - c_plus - python) | (python - c_plus - java)
hai_ngon_ngu = ((c_plus & java) - python) | ((c_plus & python) - java) | ((java & python) - c_plus)
ba_ngon_ngu = c_plus & java & python

print("Sinh vien chi thi 1 ngon ngu:", sorted(mot_ngon_ngu))
print("Sinh vien thi 2 ngon ngu:", sorted(hai_ngon_ngu))
print("Sinh vien thi ca 3 ngon ngu:", sorted(ba_ngon_ngu))