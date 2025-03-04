basic_salary = 1350000
tnct = float(input("Nhập thâm niên công tác (năm): "))
if tnct < 1:
    salary_coefficient = 1.0
elif tnct >= 1 and tnct < 3:
    salary_coefficient = 1.2
elif tnct >= 3 and tnct < 5:
    salary_coefficient = 1.5
else:
    salary_coefficient = 2.0
salary = salary_coefficient * basic_salary
print(f"Lương của nhân viên là: {salary} đồng.")