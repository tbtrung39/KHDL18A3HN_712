ds = {}
n = int(input("Nhập số sinh viên: "))
for i in range(n):
    ma = input("Mã SV: ")
    ten = input("Họ tên: ")
    diem = float(input("Điểm: "))
    ds[ma] = (ten, diem)

print("\nTheo thứ tự nhập:")
for ma in ds:
    print(ma, ds[ma][0], ds[ma][1])

print("\nTheo điểm giảm dần:")
for ma in sorted(ds, key=lambda x: ds[x][1], reverse=True):
    print(ma, ds[ma][0], ds[ma][1])
