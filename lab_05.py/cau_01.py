#cách 1
chuoi = input("Nhập vào một chuỗi kí tự: ")
so = 0
for ki_tu in chuoi:
    if ki_tu.isdigit():
        so += 1
print("số chữ số là:", so)
#cách 2
chuoi = input("Nhập chuỗi: ")
so = 0
for ki_tu in chuoi:
    if '0' <= ki_tu <= '9':
        so += 1
print("Số chữ số là:", so)
