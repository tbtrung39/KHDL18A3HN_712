#câu c
h = int(input("Nhập giá trị chiều cao tam giác đều: ")) 

k = 2 * h - 2  
print("Tam giác đêu :")
for dong in range(1, h + 1):  
    print(" " * k, end="")  
    for cot in range(1, dong + 1):  
        print("* ", end="")  
    k -= 1  
    print('')

#câu b
h = int(input("Nhập giá trị chiều cao tam giác: ")) 

print("Tam giác đều:")
for i in range(h):
    if i == 0:
        print(" " * (h - 1) + "*")
    elif i == h - 1:
        print("* " * h)
    else:
        print(" " * (h - i - 1) + "*" + " " * (2 * i - 1) + "*")
#câu a
m = int(input("Nhập chiều cao tam giác : "))  
n = int(input("Nhập độ dài đáy tam giác : "))
if n % 2 == 0:
    print("nhập lại")
else:
    print("Tam giác đều:")
    for i in range(m):  
        for j in range(1, 2 * m):
            if j == m - i or j == m + i or (i == m - 1 and m - (n // 2) <= j <= m + (n // 2)):  
                print("*", end="")
            else:
                print(" ", end="")
        print() 



