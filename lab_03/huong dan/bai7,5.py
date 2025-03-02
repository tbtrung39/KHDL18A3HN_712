num = 65
h=int(input('Nhập chiều cao tam giác ký tự: ') )
for i in range(0, h):
    for j in range(0, i+1):
        ch = chr(num)
        print(ch, end=" ")
    num = num + 1 
    print("\r")