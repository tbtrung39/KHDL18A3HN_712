s = input("Nhập chuỗi ký tự: ")
d = {}
for i in range(len(s) - 1):
    p = s[i:i+2]
    d[p] = d.get(p, 0) + 1
print("Từ điển 2 ký tự liên tiếp:", d)