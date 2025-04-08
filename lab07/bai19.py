employees = {}

# Nhập danh sách nhân viên
n = int(input("Nhập số nhân viên: "))
for _ in range(n):
    code = input("Mã nhân viên (4 chữ số): ")
    name = input("Họ tên nhân viên (tối đa 20 ký tự): ")
    birth_year = int(input("Năm sinh: "))
    salary = int(input("Lương: "))
    employees[code] = {"name": name, "birth_year": birth_year, "salary": salary}

# Tìm kiếm nhân viên theo mã
x = input("Nhập mã nhân viên cần tìm: ")
if x in employees:
    print(f"Thông tin: {employees[x]}")
else:
    print("Không tìm thấy nhân viên.")

# Tăng lương
y = input("Nhập mã nhân viên cần tăng lương: ")
if y in employees:
    employees[y]["salary"] += 1000000
    print(f"Lương mới: {employees[y]['salary']}")

# Xoá nhân viên
z = input("Nhập mã nhân viên cần xoá: ")
if z in employees:
    del employees[z]
    print(f"Đã xoá nhân viên có mã {z}")

# Sắp xếp theo năm sinh giảm dần
sorted_employees = sorted(employees.items(), key=lambda x: x[1]["birth_year"], reverse=True)

print("Danh sách nhân viên sắp xếp theo năm sinh giảm dần:")
for code, info in sorted_employees:
    print(f"Mã: {code}, Tên: {info['name']}, Năm sinh: {info['birth_year']}, Lương: {info['salary']}")
