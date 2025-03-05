h = int(input("Nhập giá trị chiều cao tam giác cân: ")) 
k = 2 * h - 2

for dong in range(1, h + 1):
    print(" " * k, end="")  
    
    if dong == 1 or dong == h:
        for cot in range(dong):
            print("*", end=" ")
        print()
    else:
        print("*", end="")
        for cot in range(dong - 2):
            print("  ", end="")
        print(" *")
    
    k -= 1
