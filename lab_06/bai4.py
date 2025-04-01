numbers=[]
while True:
    n=int(input("Nhập số 0 để dừng:"))
    if n==0:
        break
    numbers.append(n)
numbers.insert(1,[1,2,3])
numbers.insert(5,5)
xoa=int(input("Nhập vị trí cần xóa:"))
if 0<= xoa<=len(numbers):
    numbers.pop(xoa)
tang_dan=sorted(numbers)
giam_dan=sorted(numbers,reverse=True)
print("Dánh sách thứ tự tăng dần:",tang_dan)
print("Danh sách thứ tự giảm dần",giam_dan)