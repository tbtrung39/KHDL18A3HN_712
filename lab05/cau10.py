
s1=input("nhập chuỗi 1: ")
s2=input("nhập chuỗi 2: ")
max=""
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        kt=s1[i:j]
        if kt in s2 and len(kt)>len(max):
            max=kt
if max:
    print("chuỗi con chung dài nhất là:", max)
else:
    print("không có chuỗi con chung")
