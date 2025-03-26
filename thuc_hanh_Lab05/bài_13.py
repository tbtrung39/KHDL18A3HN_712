A = input("Nhập chuỗi số A: ").strip()
B = input("Nhập chuỗi số B: ").strip()

if not A or not B:
    print("Không tồn tại cách đặt!")
else:
    biểu_thức_A = ""
    số_trước = A[0]  
    for i in range(1, len(A)):
        if A[i] == số_trước[-1]: 
            số_trước += A[i]       
        else:
            biểu_thức_A += số_trước + " + "
            số_trước = A[i]  
    biểu_thức_A += số_trước  
    biểu_thức_B = ""
    số_trước = B[0]
    for i in range(1, len(B)):
        if B[i] == số_trước[-1]:
            số_trước += B[i]
        else:
            biểu_thức_B += số_trước + " + "
            số_trước = B[i]
    biểu_thức_B += số_trước
    tổng_A = sum(int(x) for x in biểu_thức_A.replace(" + ", " ").split())
    tổng_B = sum(int(x) for x in biểu_thức_B.replace(" + ", " ").split())
    if tổng_A == tổng_B:
        print(f"{biểu_thức_A} = {biểu_thức_B}")
    else:
        print("Không tồn tại cách đặt!")
