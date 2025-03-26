#cách 1
chuoi = input('Nhập chuỗi: ')
dem = 0
for k in chuoi:
    if not (('A' <= k <= 'Z') or ('a' <= k <= 'z') or ('0' <= k <= '9')):
        dem += 1
print("chuỗi kí tự không phải chữ cái tiếng anh và không phải chuỗi số là:", dem)

#cach 2
chuoi = input('nhập chuỗi: ')
dem = 0
for k in chuoi:
    ma = ord(k)
    if not (48 <= ma <= 57 or 65 <= ma <= 90 or 97 <= ma <= 122):
        dem += 1
print("chuỗi kí tự không phải chữ cái tiếng anh và không phải chuỗi số là:", dem)