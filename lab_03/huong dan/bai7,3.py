h=int(input('Nhập chiều cao tam giác số :'))
num = 1
for dong in range(1, h+1):
    num = 1
    for cot in range(1, dong+1):
        print(num, end=" ")
    num = num + 1
print("\r")