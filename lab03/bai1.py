n = int(input("Nhập giá trị n: "))
ket_qua = 1.0
for i in range(0, n + 1):
    phan_so = 1  
    for j in range(0, i + 1):
        tu_so = 2 * (j+1)             
        mau_so = 2 * j + 3       
        phan_so *= tu_so / mau_so    
    ket_qua += phan_so  
ket_qua = round(ket_qua, 3)
print(f"Kết quả của phép toán là: {ket_qua}")