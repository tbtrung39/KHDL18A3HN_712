doan_van=input("Nhập đoạn văn")
words=doan_van.split()
dem=0
for word in words:
    if word.isalpha():
        dem += 1
print("Số từ đơn trong đoạn văn là:",dem)