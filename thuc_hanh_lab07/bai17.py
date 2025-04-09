ds = {}
n = int(input("Nhập số sinh viên là: "))
for i in range(n):
    ma = input("Mã SV là: ")
    ten = input("Họ tên là: ")
    diem = float(input("Điểm là: "))
    ds[ma] = (ten, diem)
print("\nTheo thứ tự nhập là:")
for ma in ds:
    print(ma, ds[ma][0], ds[ma][1])
print("\nTheo điểm giảm dần là:")
for ma in sorted(ds, key=lambda x: ds[x][1], reverse=True):
    print(ma, ds[ma][0], ds[ma][1])