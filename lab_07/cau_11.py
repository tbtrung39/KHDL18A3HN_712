C = set(map(int, input("Nhập danh sách sinh viên thi C++: ").split()))
J = set(map(int, input("Nhập danh sách sinh viên thi Java: ").split()))
P = set(map(int, input("Nhập danh sách sinh viên thi Python: ").split()))
chi_C = C - J - P
chi_J = J - C - P
chi_P = P - C - J
C_and_J = (C & J) - P
C_and_P = (C & P) - J
J_and_P = (J & P) - C
C_and_J_and_P = C & J & P
print(f"Các sinh viên chỉ thi C++: {chi_C if chi_C else 0}")
print(f"Các sinh viên chỉ thi Java: {chi_J if chi_J else 0}")
print(f"Các sinh viên chỉ thi Python: {chi_P if chi_P else 0}")
print(f"Các sinh viên thi C++ và Java: {C_and_J if C_and_J else 0}")
print(f"Các sinh viên thi C++ và Python: {C_and_P if C_and_P else 0}")
print(f"Các sinh viên thi Java và Python: {J_and_P if J_and_P else 0}")
print(f"Các sinh viên thi cả 3 ngôn ngữ: {C_and_J_and_P if C_and_J_and_P else 0}")
#####
# print(f"Các sinh viên chỉ thi C++: {chi_C}")
# print(f"Các sinh viên chỉ thi Java: {chi_J}")
# print(f"Các sinh viên chỉ thi Python: {chi_P}")
# print(f"Các sinh viên thi C++ và Java: {C_and_J}")
# print(f"Các sinh viên thi C++ và Python: {C_and_P}")
# print(f"Các sinh viên thi Java và Python: {J_and_P}")
# print(f"Các sinh viên thi cả 3 ngôn ngữ: {C_and_J_and_P}")
