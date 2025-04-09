n = int(input("Nhập số lượng sinh viên (n): "))

a = int(input("Nhập số sinh viên thi C++: "))
c_plus = set(int(input(f"Nhập số thứ tự sinh viên thi C++ (sinh viên {i+1}): ")) for i in range(a))

b = int(input("Nhập số sinh viên thi Java: "))
java = set(int(input(f"Nhập số thứ tự sinh viên thi Java (sinh viên {i+1}): ")) for i in range(b))

c = int(input("Nhập số sinh viên thi Python: "))
python = set(int(input(f"Nhập số thứ tự sinh viên thi Python (sinh viên {i+1}): ")) for i in range(c))

chi_c = c_plus - java - python
chi_java = java - c_plus - python
chi_python = python - c_plus - java

c_plus_java = c_plus & java
c_plus_python = c_plus & python
java_python = java & python

ca_3 = c_plus & java & python

print("Sinh viên chỉ thi C++: ", sorted(chi_c))
print("Sinh viên chỉ thi Java: ", sorted(chi_java))
print("Sinh viên chỉ thi Python: ", sorted(chi_python))
print("Sinh viên thi cả C++ và Java: ", sorted(c_plus_java))
print("Sinh viên thi cả C++ và Python: ", sorted(c_plus_python))
print("Sinh viên thi cả Java và Python: ", sorted(java_python))
print("Sinh viên thi cả 3 môn: ", sorted(ca_3))