doan_van=input("Nhập đoạn văn")
van=doan_van.split()
dem=0
for i in van:
    if i.isalpha():
        dem += 1
print("Số từ đơn trong đoạn văn là:",dem)